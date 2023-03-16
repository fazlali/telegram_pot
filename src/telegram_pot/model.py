import builtins
import io
import sys
import typing
from types import GenericAlias, UnionType
from typing import Any, Union, get_args, get_origin

import requests


def populate_value(_type, _value):
    if _value is None:
        return None

    if isinstance(_type, UnionType) or get_origin(_type) == Union:
        for arg in _type.__args__:
            try:
                return populate_value(arg, _value)
            except ValueError:
                pass
    if _type in [str, bool, int, float, dict, io.BytesIO]:
        if isinstance(_value, _type):
            return _value
    elif issubclass(_type, Model):
        if isinstance(_value, dict):
            return _type.from_dict(_value)
        elif isinstance(_value, _type):
            return _value
    elif get_origin(_type) == list:
        if isinstance(_value, list):
            return [populate_value(_type.__args__[0], v) for v in _value]

    raise ValueError()


def get_type(name, module=None, raise_on_fail=True):
    if isinstance(name, GenericAlias):
        if get_origin(name) == list:
            return list[get_type(name.__args__[0], module, raise_on_fail)]
        if get_origin(name) == dict:
            return dict[get_type(name.__args__[0], module), get_type(name.__args__[1], module, raise_on_fail)]
    elif isinstance(name, type) or name == typing.Any:
        return name
    elif isinstance(name, str):
        if hasattr(builtins, name):
            return getattr(builtins, name)

        try:
            ns = {}
            module = module.__dict__ if module else {}
            exec(f'def __parse_field__(): return {name}', module, ns)
            return ns['__parse_field__']()
        except NameError:
            pass
    elif isinstance(name, UnionType) or get_origin(name) == Union:
        return Union[tuple(get_type(arg, module, raise_on_fail) for arg in name.__args__)]

    if raise_on_fail:
        raise TypeError()
    else:
        return name


class BaseModel(type):

    TYPES = {}

    class Field:

        def __init__(self, name: str, field_type: str | type, default=None, module=None) -> None:
            self.__type = get_type(field_type, module, False)
            self.name = name
            # if isinstance(field_type, GenericAlias):
            #     self._type = field_type
            #     self.type_name = str(field_type)
            # if isinstance(field_type, UnionType):
            #     self._type = field_type
            #     self.type_name = str(field_type)
            # elif isinstance(field_type, type):
            #     self._type = field_type
            #     self.type_name = field_type.__name__
            # elif isinstance(field_type, str):
            #     self._type = None
            #     self.type_name = field_type
            # elif field_type == typing.Any:
            #     self._type = typing.Any
            #     self.type_name = 'Any'
            # else:
            #     raise TypeError()
            # self._type = field_type
            self._type = None
            self.default = default
            self.module = module
            self.private = self.name.startswith('_')
            self.alias = self.name.rstrip('_') if self.name.endswith('_') else None

        @property
        def type(self):
            if self._type is None:
                self._type = get_type(self.__type, self.module)
            return self._type

    def __new__(mcs, name, parent, attrs, **kwargs):
        annotations = attrs.get('__annotations__', {})
        # new_attrs = dict((k, v) for k, v in attrs.items() if k not in annotations)
        # new_class = super().__new__(mcs, name, parent, new_attrs, **kwargs)
        new_class = super().__new__(mcs, name, parent, attrs, **kwargs)
        mcs.TYPES[name] = new_class
        module = sys.modules[attrs['__module__']]
        __fields__: list[BaseModel.Field] = []
        setattr(new_class, '__fields__', __fields__)

        # args = ['self']
        # body = []
        for field_name, annotation in annotations.items():
            __fields__.append(
                BaseModel.Field(
                    name=field_name,
                    field_type=annotation,
                    default=getattr(new_class, field_name, None),
                    module=module
                )
            )
            if not hasattr(new_class, field_name):
                setattr(new_class, field_name, None)

        # for field in __fields__:
        #     if not field.private:
        #         default = f'"{field.default}"' if isinstance(field.default, str) else str(field.default)
        #         args.append(f'{field.name}: "{field.type_name}" = {default}')
        #         body.append(f'    self.{field.name} = {field.name}')
        #
        # if len(body):
        #     args = ', '.join(args)
        #     body = '\n'.join(body)
        #     init_function = f'  def __init__({args}) -> None:\n{body}'
        #     init_function_generator = f'def __init_function_generator__():\n{init_function}\n  return __init__'
        #     ns = {}
        #     exec(init_function_generator, module.__dict__, ns)
        #     setattr(new_class, '__init__', ns['__init_function_generator__']())

        setattr(new_class, '__fields__', __fields__)
        setattr(new_class, '__slots__', tuple(field.name for field in __fields__))
        # new_class.__doc__ = '%s(%s)' % (name, ', '.join([field.name for field in __fields__ if not field.private]))
        return new_class


class Model(metaclass=BaseModel):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__()
        for key, value in kwargs.items():
            field = next((field for field in self.__fields__ if field.name == key or field.alias == key), None)
            if field:
                setattr(self, field.name, value)
        for field in self.__fields__:
            if field.name not in kwargs and (not field.alias or field.alias not in kwargs):
                setattr(self, field.name, field.default)

    def __setattr__(self, key, value):
        field = next((field for field in self.__fields__ if field.name == key or field.alias == key), None)
        if not field:
            raise ValueError()
        value = populate_value(field.type, value)
        super().__setattr__(key, value)

    @classmethod
    def from_dict(cls, attributes: dict):
        instance = cls()
        for key, value in attributes.items():
            field = next((field for field in cls.__fields__ if field.name == key or field.alias == key), None)
            if field:
                setattr(instance, field.name, value)
        return instance

    def to_dict(self):
        result = {}

        def recursive(v):
            if isinstance(v, Model):
                return v.to_dict()
            if isinstance(v, list):
                return [recursive(i) for i in v]
            return v

        for filed in self.__fields__:
            value = getattr(self, filed.name, None)
            if value is not None:
                result[filed.name] = recursive(value)
        return result


class API(Model):
    _result: Any = None
    METHOD: str = None

    @property
    def result(self):
        return self._result

    def get_request(self) -> requests.Request:
        from .models import InputFile
        data = self.to_dict()
        files = {k: v.to_tuple() for k, v in data.items() if isinstance(v, InputFile)}
        for k in files:
            data.pop(k)
        return requests.Request(
            method='POST',
            url=self.METHOD or self.__class__.__name__.lower(),
            data=data if files else {},
            json=None if files else data,
            files=files
        )

    def set_result(self, result: Any):
        if self._result is not None:
            raise ValueError()
        self._result = result

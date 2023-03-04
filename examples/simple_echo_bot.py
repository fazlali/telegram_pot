import io

import requests

from src.telegram_pot.apis import SendMessage, SendPhoto
from src.telegram_pot.bot import TelegramBot, Process
from src.telegram_pot.models import Message, InputFile

bot = TelegramBot('BOT_API_KEY')


@bot.on_command('ping')
def pong(message: Message):
    bot.execute(SendMessage(
        text='PONG',
        chat_id=message.chat.id,
        reply_to_message_id=message.message_id
    ))


@bot.on_command('photo')
def photo(message: Message):
    image_response = requests.get('https://loremflickr.com/640/480')
    bot.execute(SendPhoto(
        caption='sample qrcode',
        chat_id=message.chat.id,
        reply_to_message_id=message.message_id,
        photo=InputFile(
            upload_file_name='sample_qrcode',
            upload_file_content_type='image/png',
            upload_file_object=io.BytesIO(image_response.content)
        )
    ))
    bot.execute(SendPhoto(
        caption='sample qrcode',
        chat_id=message.chat.id,
        reply_to_message_id=message.message_id,
        photo=InputFile(
            file_url='https://loremflickr.com/640/480'
        )
    ))


@bot.on_message()
def echo(message: Message):
    bot.execute(SendMessage(
        text=message.text,
        chat_id=message.chat.id,
        reply_to_message_id=message.message_id
    ))
    return True


@bot.on_command('start')
def start(message: Message):
    process = bot.create_process(message.chat.id, 'profile')
    process.stage = 'first_name'
    bot.execute(SendMessage(text='First name ?', chat_id=message.chat.id))
    return True


@bot.on_process('profile')
def start(message: Message, process: Process):
    if process.stage == 'first_name':
        process.data['first_name'] = message.text
        process.stage = 'last_name'
        bot.execute(SendMessage(text='Last name ?', chat_id=message.chat.id))
    elif process.stage == 'last_name':
        process.data['last_name'] = message.text
        process.stage = 'gender'
        bot.execute(SendMessage(text='Gender ?', chat_id=message.chat.id))
    elif process.stage == 'gender':
        process.data['gender'] = message.text
        process.stage = 'age'
        bot.execute(SendMessage(text='Age ?', chat_id=message.chat.id))
    elif process.stage == 'age':
        process.data['age'] = message.text
        bot.close_current_process(message.chat.id)
        bot.execute(SendMessage(
            text=f'First name: {process.data["first_name"]}\n'
                 f'Last name: {process.data["last_name"]}\n'
                 f'Gender: {process.data["gender"]}\n'
                 f'Age : {process.data["age"]}\n',
            chat_id=message.chat.id))

    return True


bot.start()

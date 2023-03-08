from __future__ import annotations

import io

from .model import Model


class User(Model):
    id: int
    is_bot: bool
    first_name: str
    last_name: str
    username: str
    language_code: str
    is_premium: bool
    added_to_attachment_menu: bool
    can_join_groups: bool
    can_read_all_group_messages: bool
    supports_inline_queries: bool


class Chat(Model):
    id: int
    type: str
    title: str
    username: str
    first_name: str
    last_name: str
    is_forum: bool = True
    photo: ChatPhoto
    active_usernames: list[str]
    emoji_status_custom_emoji_id: str
    bio: str
    has_private_forwards: bool = True
    has_restricted_voice_and_video_messages: bool = True
    join_to_send_messages: bool = True
    join_by_request: bool = True
    description: str
    invite_link: str
    pinned_message: Message
    permissions: ChatPermissions
    slow_mode_delay: int
    message_auto_delete_time: int
    has_aggressive_anti_spam_enabled: bool = True
    has_hidden_members: bool = True
    has_protected_content: bool = True
    sticker_set_name: str
    can_set_sticker_set: bool = True
    linked_chat_id: int
    location: ChatLocation


class Message(Model):
    message_id: int
    message_thread_id: int
    from_: User
    sender_chat: Chat
    date: int
    chat: Chat
    forward_from: User
    forward_from_chat: Chat
    forward_from_message_id: int
    forward_signature: str
    forward_sender_name: str
    forward_date: int
    is_topic_message: bool = True
    is_automatic_forward: bool = True
    reply_to_message: Message
    via_bot: User
    edit_date: int
    has_protected_content: bool = True
    media_group_id: str
    author_signature: str
    text: str
    entities: list[MessageEntity]
    animation: Animation
    audio: Audio
    document: Document
    photo: list[PhotoSize]
    sticker: Sticker
    video: Video
    video_note: VideoNote
    voice: Voice
    caption: str
    caption_entities: list[MessageEntity]
    has_media_spoiler: bool = True
    contact: Contact
    dice: Dice
    game: Game
    poll: Poll
    venue: Venue
    location: Location
    new_chat_members: list[User]
    left_chat_member: User
    new_chat_title: str
    new_chat_photo: list[PhotoSize]
    delete_chat_photo: bool = True
    group_chat_created: bool = True
    supergroup_chat_created: bool = True
    channel_chat_created: bool = True
    message_auto_delete_timer_changed: MessageAutoDeleteTimerChanged
    migrate_to_chat_id: int
    migrate_from_chat_id: int
    pinned_message: Message
    invoice: Invoice
    successful_payment: SuccessfulPayment
    connected_website: str
    write_access_allowed: WriteAccessAllowed
    passport_data: PassportData
    proximity_alert_triggered: ProximityAlertTriggered
    forum_topic_created: ForumTopicCreated
    forum_topic_edited: ForumTopicEdited
    forum_topic_closed: ForumTopicClosed
    forum_topic_reopened: ForumTopicReopened
    general_forum_topic_hidden: GeneralForumTopicHidden
    general_forum_topic_unhidden: GeneralForumTopicUnhidden
    video_chat_scheduled: VideoChatScheduled
    video_chat_started: VideoChatStarted
    video_chat_ended: VideoChatEnded
    video_chat_participants_invited: VideoChatParticipantsInvited
    web_app_data: WebAppData
    reply_markup: InlineKeyboardMarkup


class MessageId(Model):
    message_id: int


class MessageEntity(Model):
    type: str
    offset: int
    length: int
    url: str
    user: User
    language: str
    custom_emoji_id: str


class PhotoSize(Model):
    file_id: str
    file_unique_id: str
    width: int
    height: int
    file_size: int


class Animation(Model):
    file_id: str
    file_unique_id: str
    width: int
    height: int
    duration: int
    thumb: PhotoSize
    file_name: str
    mime_type: str
    file_size: int


class Audio(Model):
    file_id: str
    file_unique_id: str
    duration: int
    performer: str
    title: str
    file_name: str
    mime_type: str
    file_size: int
    thumb: PhotoSize


class Document(Model):
    file_id: str
    file_unique_id: str
    thumb: PhotoSize
    file_name: str
    mime_type: str
    file_size: int


class Video(Model):
    file_id: str
    file_unique_id: str
    width: int
    height: int
    duration: int
    thumb: PhotoSize
    file_name: str
    mime_type: str
    file_size: int


class VideoNote(Model):
    file_id: str
    file_unique_id: str
    length: int
    duration: int
    thumb: PhotoSize
    file_size: int


class Voice(Model):
    file_id: str
    file_unique_id: str
    duration: int
    mime_type: str
    file_size: int


class Contact(Model):
    phone_number: str
    first_name: str
    last_name: str
    user_id: int
    vcard: str


class Dice(Model):
    emoji: str
    value: int


class PollOption(Model):
    text: str
    voter_count: int


class PollAnswer(Model):
    poll_id: str
    user: User
    option_ids: list[int]


class Poll(Model):
    id: str
    question: str
    options: list[PollOption]
    total_voter_count: int
    is_closed: bool
    is_anonymous: bool
    type: str
    allows_multiple_answers: bool
    correct_option_id: int
    explanation: str
    explanation_entities: list[MessageEntity]
    open_period: int
    close_date: int


class Location(Model):
    longitude: float
    latitude: float
    horizontal_accuracy: float
    live_period: int
    heading: int
    proximity_alert_radius: int


class Venue(Model):
    location: Location
    title: str
    address: str
    foursquare_id: str
    foursquare_type: str
    google_place_id: str
    google_place_type: str


class WebAppData(Model):
    data: str
    button_text: str


class ProximityAlertTriggered(Model):
    traveler: User
    watcher: User
    distance: int


class MessageAutoDeleteTimerChanged(Model):
    message_auto_delete_time: int


class ForumTopicCreated(Model):
    name: str
    icon_color: int
    icon_custom_emoji_id: str


class ForumTopicClosed(Model):
    pass


class ForumTopicEdited(Model):
    name: str
    icon_custom_emoji_id: str


class ForumTopicReopened(Model):
    pass


class GeneralForumTopicHidden(Model):
    pass


class GeneralForumTopicUnhidden(Model):
    pass


class WriteAccessAllowed(Model):
    pass


class VideoChatScheduled(Model):
    start_date: int


class VideoChatStarted(Model):
    pass


class VideoChatEnded(Model):
    duration: int


class VideoChatParticipantsInvited(Model):
    users: list[User]


class UserProfilePhotos(Model):
    total_count: int
    photos: list[list[PhotoSize]]


class File(Model):
    file_id: str
    file_unique_id: str
    file_size: int
    file_path: str


class WebAppInfo(Model):
    url: str


class ReplyKeyboardMarkup(Model):
    keyboard: list[list[KeyboardButton]]
    is_persistent: bool
    resize_keyboard: bool
    one_time_keyboard: bool
    input_field_placeholder: str
    selective: bool


class KeyboardButton(Model):
    text: str
    request_contact: bool
    request_location: bool
    request_poll: KeyboardButtonPollType
    web_app: WebAppInfo


class KeyboardButtonPollType(Model):
    type: str


class ReplyKeyboardRemove(Model):
    remove_keyboard: bool = True
    selective: bool


class InlineKeyboardMarkup(Model):
    inline_keyboard: list[list[InlineKeyboardButton]]


class InlineKeyboardButton(Model):
    text: str
    url: str
    callback_data: str
    web_app: WebAppInfo
    login_url: LoginUrl
    switch_inline_query: str
    switch_inline_query_current_chat: str
    callback_game: CallbackGame
    pay: bool


class LoginUrl(Model):
    url: str
    forward_text: str
    bot_username: str
    request_write_access: bool


class CallbackQuery(Model):
    id: str
    from_: User
    message: Message
    inline_message_id: str
    chat_instance: str
    data: str
    game_short_name: str


class ForceReply(Model):
    force_reply: bool = True
    input_field_placeholder: str
    selective: bool


class ChatPhoto(Model):
    small_file_id: str
    small_file_unique_id: str
    big_file_id: str
    big_file_unique_id: str


class ChatInviteLink(Model):
    invite_link: str
    creator: User
    creates_join_request: bool
    is_primary: bool
    is_revoked: bool
    name: str
    expire_date: int
    member_limit: int
    pending_join_request_count: int


class ChatAdministratorRights(Model):
    is_anonymous: bool
    can_manage_chat: bool
    can_delete_messages: bool
    can_manage_video_chats: bool
    can_restrict_members: bool
    can_promote_members: bool
    can_change_info: bool
    can_invite_users: bool
    can_post_messages: bool
    can_edit_messages: bool
    can_pin_messages: bool
    can_manage_topics: bool


class ChatMember(Model):
    user: User
    status: str


class ChatMemberOwner(ChatMember):
    status: str = 'owner'
    is_anonymous: bool
    custom_title: str


class ChatMemberAdministrator(ChatMember):
    status: str = 'administrator'
    can_be_edited: bool
    is_anonymous: bool
    can_manage_chat: bool
    can_delete_messages: bool
    can_manage_video_chats: bool
    can_restrict_members: bool
    can_promote_members: bool
    can_change_info: bool
    can_invite_users: bool
    can_post_messages: bool
    can_edit_messages: bool
    can_pin_messages: bool
    can_manage_topics: bool
    custom_title: str


class ChatMemberMember(ChatMember):
    pass
    status: str = 'member'


class ChatMemberRestricted(ChatMember):
    status: str = 'restricted'
    is_member: bool
    can_change_info: bool
    can_invite_users: bool
    can_pin_messages: bool
    can_manage_topics: bool
    can_send_messages: bool
    can_send_media_messages: bool
    can_send_polls: bool
    can_send_other_messages: bool
    can_add_web_page_previews: bool
    until_date: int


class ChatMemberLeft(ChatMember):
    pass
    status: str = 'left'


class ChatMemberBanned(ChatMember):
    status: str = 'banned'
    until_date: int


class ChatMemberUpdated(ChatMember):
    status: str = 'updated'
    chat: Chat
    from_: User
    date: int
    old_chat_member: ChatMember
    new_chat_member: ChatMember
    invite_link: ChatInviteLink


class ChatJoinRequest(Model):
    chat: Chat
    from_: User
    date: int
    bio: str
    invite_link: ChatInviteLink


class ChatPermissions(Model):
    can_send_messages: bool
    can_send_media_messages: bool
    can_send_polls: bool
    can_send_other_messages: bool
    can_add_web_page_previews: bool
    can_change_info: bool
    can_invite_users: bool
    can_pin_messages: bool
    can_manage_topics: bool


class ChatLocation(Model):
    location: Location
    address: str


class ForumTopic(Model):
    message_thread_id: int
    name: str
    icon_color: int
    icon_custom_emoji_id: str


class BotCommand(Model):
    command: str
    description: str


class BotCommandScope(Model):
    type: str


class BotCommandScopeDefault(BotCommand):
    type: str = 'default'


class BotCommandScopeAllPrivateChats(BotCommand):
    type: str = 'all_private_chats'


class BotCommandScopeAllGroupChats(BotCommand):
    type: str = 'all_group_chats'


class BotCommandScopeAllChatAdministrators(BotCommand):
    type: str = 'all_chat_administrators'


class BotCommandScopeChat(BotCommand):
    type: str = 'chat'
    chat_id: int or str


class BotCommandScopeChatAdministrators(BotCommand):
    type: str = 'chat_administrators'
    chat_id: int or str


class BotCommandScopeChatMember(BotCommand):
    type: str = 'chat_member'
    chat_id: int or str
    user_id: int


class MenuButton(Model):
    type: str


class MenuButtonCommands(Model):
    type: str = 'commands'


class MenuButtonWebApp(Model):
    type: str = 'web_app'
    text: str
    web_app: WebAppInfo


class MenuButtonDefault(Model):
    type: str = 'default'


class ResponseParameters(Model):
    migrate_to_chat_id: int
    retry_after: int


class InputMedia(Model):
    type: str


class InputMediaPhoto(InputMedia):
    type: str = 'photo'
    media: str
    caption: str
    parse_mode: str
    caption_entities: list[MessageEntity]
    has_spoiler: bool


class InputMediaVideo(InputMedia):
    type: str = 'video'
    media: str
    thumb: InputFile or str
    caption: str
    parse_mode: str
    caption_entities: list[MessageEntity]
    width: int
    height: int
    duration: int
    supports_streaming: bool
    has_spoiler: bool


class InputMediaAnimation(InputMedia):
    type: str = 'animation'
    media: str
    thumb: InputFile or str
    caption: str
    parse_mode: str
    caption_entities: list[MessageEntity]
    width: int
    height: int
    duration: int
    has_spoiler: bool


class InputMediaAudio(InputMedia):
    type: str = 'audio'
    media: str
    thumb: InputFile or str
    caption: str
    parse_mode: str
    caption_entities: list[MessageEntity]
    duration: int
    performer: str
    title: str


class InputMediaDocument(InputMedia):
    type: str = 'document'
    media: str
    thumb: InputFile or str
    caption: str
    parse_mode: str
    caption_entities: list[MessageEntity]
    disable_content_type_detection: bool


class InputFile(Model):
    file_url: str
    file_id: str

    upload_file_name: str
    upload_file_object: io.BytesIO
    upload_file_content_type: str

    def to_tuple(self) -> tuple[str, io.BytesIO, str]:
        return self.upload_file_name, self.upload_file_object, self.upload_file_content_type

    def to_dict(self):
        if self.upload_file_name or self.upload_file_content_type or self.upload_file_object:
            return self
        else:
            return self.file_id or self.file_url or None


class Sticker(Model):
    file_id: str
    file_unique_id: str
    type: str
    width: int
    height: int
    is_animated: bool
    is_video: bool
    thumb: PhotoSize
    emoji: str
    set_name: str
    premium_animation: File
    mask_position: MaskPosition
    custom_emoji_id: str
    file_size: int


class StickerSet(Model):
    name: str
    title: str
    sticker_type: str
    is_animated: bool
    is_video: bool
    stickers: list[Sticker]
    thumb: PhotoSize


class MaskPosition(Model):
    point: str
    x_shift: float
    y_shift: float
    scale: float


class InlineQuery(Model):
    id: str
    from_: User
    query: str
    offset: str
    chat_type: str
    location: Location


class InlineQueryResult(Model):
    type: str
    id: str


class InlineQueryResultArticle(InlineQueryResult):
    type: str = 'article'
    id: str
    title: str
    input_message_content: InputMessageContent
    reply_markup: InlineKeyboardMarkup
    url: str
    hide_url: bool
    description: str
    thumb_url: str
    thumb_width: int
    thumb_height: int


class InlineQueryResultPhoto(InlineQueryResult):
    type: str = 'photo'
    id: str
    photo_url: str
    thumb_url: str
    photo_width: int
    photo_height: int
    title: str
    description: str
    caption: str
    parse_mode: str
    caption_entities: list[MessageEntity]
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent


class InlineQueryResultGif(InlineQueryResult):
    type: str = 'gif'
    id: str
    gif_url: str
    gif_width: int
    gif_height: int
    gif_duration: int
    thumb_url: str
    thumb_mime_type: str
    title: str
    caption: str
    parse_mode: str
    caption_entities: list[MessageEntity]
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent


class InlineQueryResultMpeg4Gif(InlineQueryResult):
    type: str = 'mpeg4_gif'
    id: str
    mpeg4_url: str
    mpeg4_width: int
    mpeg4_height: int
    mpeg4_duration: int
    thumb_url: str
    thumb_mime_type: str
    title: str
    caption: str
    parse_mode: str
    caption_entities: list[MessageEntity]
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent


class InlineQueryResultVideo(InlineQueryResult):
    type: str = 'video'
    id: str
    video_url: str
    mime_type: str
    thumb_url: str
    title: str
    caption: str
    parse_mode: str
    caption_entities: list[MessageEntity]
    video_width: int
    video_height: int
    video_duration: int
    description: str
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent


class InlineQueryResultAudio(InlineQueryResult):
    type: str = 'audio'
    id: str
    audio_url: str
    title: str
    caption: str
    parse_mode: str
    caption_entities: list[MessageEntity]
    performer: str
    audio_duration: int
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent


class InlineQueryResultVoice(InlineQueryResult):
    type: str = 'voice'
    id: str
    voice_url: str
    title: str
    caption: str
    parse_mode: str
    caption_entities: list[MessageEntity]
    voice_duration: int
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent


class InlineQueryResultDocument(InlineQueryResult):
    type: str = 'document'
    id: str
    title: str
    caption: str
    parse_mode: str
    caption_entities: list[MessageEntity]
    document_url: str
    mime_type: str
    description: str
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent
    thumb_url: str
    thumb_width: int
    thumb_height: int


class InlineQueryResultLocation(InlineQueryResult):
    type: str = 'location'
    id: str
    latitude: float
    longitude: float
    title: str
    horizontal_accuracy: float
    live_period: int
    heading: int
    proximity_alert_radius: int
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent
    thumb_url: str
    thumb_width: int
    thumb_height: int


class InlineQueryResultVenue(InlineQueryResult):
    type: str = 'venue'
    id: str
    latitude: float
    longitude: float
    title: str
    address: str
    foursquare_id: str
    foursquare_type: str
    google_place_id: str
    google_place_type: str
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent
    thumb_url: str
    thumb_width: int
    thumb_height: int


class InlineQueryResultContact(InlineQueryResult):
    type: str = 'contact'
    id: str
    phone_number: str
    first_name: str
    last_name: str
    vcard: str
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent
    thumb_url: str
    thumb_width: int
    thumb_height: int


class InlineQueryResultGame(InlineQueryResult):
    type: str = 'game'
    id: str
    game_short_name: str
    reply_markup: InlineKeyboardMarkup


class InlineQueryResultCachedPhoto(InlineQueryResult):
    type: str = 'photo'
    id: str
    photo_file_id: str
    title: str
    description: str
    caption: str
    parse_mode: str
    caption_entities: list[MessageEntity]
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent


class InlineQueryResultCachedGif(InlineQueryResult):
    type: str = 'gif'
    id: str
    gif_file_id: str
    title: str
    caption: str
    parse_mode: str
    caption_entities: list[MessageEntity]
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent


class InlineQueryResultCachedMpeg4Gif(InlineQueryResult):
    type: str = 'mpeg4_gif'
    id: str
    mpeg4_file_id: str
    title: str
    caption: str
    parse_mode: str
    caption_entities: list[MessageEntity]
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent


class InlineQueryResultCachedSticker(InlineQueryResult):
    type: str = 'sticker'
    id: str
    sticker_file_id: str
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent


class InlineQueryResultCachedDocument(InlineQueryResult):
    type: str = 'document'
    id: str
    title: str
    document_file_id: str
    description: str
    caption: str
    parse_mode: str
    caption_entities: list[MessageEntity]
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent


class InlineQueryResultCachedVideo(InlineQueryResult):
    type: str = 'video'
    id: str
    video_file_id: str
    title: str
    description: str
    caption: str
    parse_mode: str
    caption_entities: list[MessageEntity]
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent


class InlineQueryResultCachedVoice(InlineQueryResult):
    type: str = 'voice'
    id: str
    voice_file_id: str
    title: str
    caption: str
    parse_mode: str
    caption_entities: list[MessageEntity]
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent


class InlineQueryResultCachedAudio(InlineQueryResult):
    type: str = 'audio'
    id: str
    audio_file_id: str
    caption: str
    parse_mode: str
    caption_entities: list[MessageEntity]
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent


class InputMessageContent(Model):
    pass


class InputTextMessageContent(InputMessageContent):
    message_text: str
    parse_mode: str
    entities: list[MessageEntity]
    disable_web_page_preview: bool


class InputLocationMessageContent(InputMessageContent):
    latitude: float
    longitude: float
    horizontal_accuracy: float
    live_period: int
    heading: int
    proximity_alert_radius: int


class InputVenueMessageContent(InputMessageContent):
    latitude: float
    longitude: float
    title: str
    address: str
    foursquare_id: str
    foursquare_type: str
    google_place_id: str
    google_place_type: str


class InputContactMessageContent(InputMessageContent):
    phone_number: str
    first_name: str
    last_name: str
    vcard: str


class InputInvoiceMessageContent(InputMessageContent):
    title: str
    description: str
    payload: str
    provider_token: str
    currency: str
    prices: list[LabeledPrice]
    max_tip_amount: int
    suggested_tip_amounts: list[int]
    provider_data: str
    photo_url: str
    photo_size: int
    photo_width: int
    photo_height: int
    need_name: bool
    need_phone_number: bool
    need_email: bool
    need_shipping_address: bool
    send_phone_number_to_provider: bool
    send_email_to_provider: bool
    is_flexible: bool


class SentWebAppMessage(Model):
    inline_message_id: str


class ChosenInlineResult(Model):
    result_id: str
    from_: User
    location: Location
    inline_message_id: str
    query: str


class LabeledPrice(Model):
    label: str
    amount: int


class Invoice(Model):
    title: str
    description: str
    start_parameter: str
    currency: str
    total_amount: int


class ShippingAddress(Model):
    country_code: str
    state: str
    city: str
    street_line1: str
    street_line2: str
    post_code: str


class OrderInfo(Model):
    name: str
    phone_number: str
    email: str
    shipping_address: ShippingAddress


class ShippingOption(Model):
    id: str
    title: str
    prices: list[LabeledPrice]


class SuccessfulPayment(Model):
    currency: str
    total_amount: int
    invoice_payload: str
    shipping_option_id: str
    order_info: OrderInfo
    telegram_payment_charge_id: str
    provider_payment_charge_id: str


class ShippingQuery(Model):
    id: str
    from_: User
    invoice_payload: str
    shipping_address: ShippingAddress


class PreCheckoutQuery(Model):
    id: str
    from_: User
    currency: str
    total_amount: int
    invoice_payload: str
    shipping_option_id: str
    order_info: OrderInfo


class PassportData(Model):
    data: list[EncryptedPassportElement]
    credentials: EncryptedCredentials


class PassportFile(Model):
    file_id: str
    file_unique_id: str
    file_size: int
    file_date: int


class EncryptedPassportElement(Model):
    type: str
    data: str
    phone_number: str
    email: str
    files: list[PassportFile]
    front_side: PassportFile
    reverse_side: PassportFile
    selfie: PassportFile
    translation: list[PassportFile]
    hash: str


class EncryptedCredentials(Model):
    data: str
    hash: str
    secret: str


class PassportElementError(Model):
    source: str
    type: str
    message: str


class PassportElementErrorDataField(PassportElementError):
    source: str
    type: str
    field_name: str
    data_hash: str
    message: str


class PassportElementErrorFrontSide(PassportElementError):
    source: str
    type: str
    file_hash: str
    message: str


class PassportElementErrorReverseSide(PassportElementError):
    source: str
    type: str
    file_hash: str
    message: str


class PassportElementErrorSelfie(PassportElementError):
    source: str
    type: str
    file_hash: str
    message: str


class PassportElementErrorFile(PassportElementError):
    source: str
    type: str
    file_hash: str
    message: str


class PassportElementErrorFiles(PassportElementError):
    source: str
    type: str
    file_hashes: list[str]
    message: str


class PassportElementErrorTranslationFile(PassportElementError):
    source: str
    type: str
    file_hash: str
    message: str


class PassportElementErrorTranslationFiles(PassportElementError):
    source: str
    type: str
    file_hashes: list[str]
    message: str


class PassportElementErrorUnspecified(PassportElementError):
    source: str
    type: str
    element_hash: str
    message: str


class Game(Model):
    title: str
    description: str
    photo: list[PhotoSize]
    text: str
    text_entities: list[MessageEntity]
    animation: Animation


class CallbackGame:
    pass


class GameHighScore(Model):
    position: int
    user: User
    score: int


class Update(Model):
    update_id: int
    message: Message
    edited_message: Message
    channel_post: Message
    edited_channel_post: Message
    inline_query: InlineQuery
    chosen_inline_result: ChosenInlineResult
    callback_query: CallbackQuery
    shipping_query: ShippingQuery
    pre_checkout_query: PreCheckoutQuery
    poll: Poll
    poll_answer: PollAnswer
    my_chat_member: ChatMemberUpdated
    chat_member: ChatMemberUpdated
    chat_join_request: ChatJoinRequest

    @property
    def type(self):
        for key, value in self.__dict__.items():
            if value and isinstance(value, Model):
                return key
        return None


class WebhookInfo(Model):
    url: str
    has_custom_certificate: bool
    pending_update_count: list[int]
    ip_address: str
    last_error_date: list[int]
    last_error_message: str
    last_synchronization_error_date: list[int]
    max_connections: list[int]
    allowed_updates: list[str]

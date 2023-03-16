
from .model import API
from .models import MessageEntity, InputFile, InlineKeyboardMarkup, InputMedia, InputMediaAudio, InputMediaVideo, \
    InputMediaDocument, InputMediaPhoto, ChatPermissions, BotCommand, BotCommandScope, MenuButton, \
    ChatAdministratorRights, PhotoSize, File, MaskPosition, InlineQueryResult, LabeledPrice, ShippingOption, \
    PassportElementError, Update, WebhookInfo, User, Message, MessageId, UserProfilePhotos, ChatInviteLink, Chat, \
    ChatMember, Sticker, ForumTopic, Poll, StickerSet, SentWebAppMessage, GameHighScore, ReplyKeyboardMarkup, \
    ReplyKeyboardRemove, ForceReply


class GetUpdates(API):
    _result: list[Update]

    offset: int
    limit: int
    timeout: int
    allowed_updates: list[str]


class SetWebhook(API):
    _result: bool

    url: str
    certificate: InputFile
    ip_address: str
    max_connections: int
    allowed_updates: list[str]
    drop_pending_updates: bool
    secret_token: str


class DeleteWebhook(API):
    _result: dict

    drop_pending_updates: bool


class GetWebhookInfo(API):
    _result: WebhookInfo


class GetMe(API):
    _result: User


class LogOut(API):
    _result: bool


class Close(API):
    _result: bool


class SendMessage(API):
    _result: Message

    chat_id: int | str
    message_thread_id: int
    text: str
    parse_mode: str = ''
    entities: list[MessageEntity]
    disable_web_page_preview: bool
    disable_notification: bool
    protect_content: bool
    reply_to_message_id: int
    allow_sending_without_reply: bool
    reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply


class ForwardMessage(API):
    _result: Message

    chat_id: int | str
    message_thread_id: int
    from_chat_id: int | str
    disable_notification: bool
    protect_content: bool
    message_id: int


class CopyMessage(API):
    _result: MessageId

    chat_id: int | str
    message_thread_id: int
    from_chat_id: int | str
    message_id: int
    caption: str
    parse_mode: str
    caption_entities: list[MessageEntity]
    disable_notification: bool
    protect_content: bool
    reply_to_message_id: int
    allow_sending_without_reply: bool
    reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply


class SendPhoto(API):
    _result: Message

    chat_id: int | str
    message_thread_id: int
    photo: InputFile | str
    caption: str
    parse_mode: str
    caption_entities: list[MessageEntity]
    has_spoiler: bool
    disable_notification: bool
    protect_content: bool
    reply_to_message_id: int
    allow_sending_without_reply: bool
    reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply


class SendAudio(API):
    _result: Message

    chat_id: int | str
    message_thread_id: int
    audio: InputFile | str
    caption: str
    parse_mode: str
    caption_entities: list[MessageEntity]
    duration: int
    performer: str
    title: str
    thumb: InputFile | str
    disable_notification: bool
    protect_content: bool
    reply_to_message_id: int
    allow_sending_without_reply: bool
    reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply


class SendDocument(API):
    _result: Message

    chat_id: int | str
    message_thread_id: int
    document: InputFile | str
    thumb: InputFile | str
    caption: str
    parse_mode: str
    caption_entities: list[MessageEntity]
    disable_content_type_detection: bool
    disable_notification: bool
    protect_content: bool
    reply_to_message_id: int
    allow_sending_without_reply: bool
    reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply


class SendVideo(API):
    _result: Message

    chat_id: int | str
    message_thread_id: int
    video: InputFile | str
    duration: int
    width: int
    height: int
    thumb: InputFile | str
    caption: str
    parse_mode: str
    caption_entities: list[MessageEntity]
    has_spoiler: bool
    supports_streaming: bool
    disable_notification: bool
    protect_content: bool
    reply_to_message_id: int
    allow_sending_without_reply: bool
    reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply


class SendAnimation(API):
    _result: Message

    chat_id: int | str
    message_thread_id: int
    animation: InputFile | str
    duration: int
    width: int
    height: int
    thumb: InputFile | str
    caption: str
    parse_mode: str
    caption_entities: list[MessageEntity]
    has_spoiler: bool
    disable_notification: bool
    protect_content: bool
    reply_to_message_id: int
    allow_sending_without_reply: bool
    reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply


class SendVoice(API):
    _result: Message

    chat_id: int | str
    message_thread_id: int
    voice: InputFile | str
    caption: str
    parse_mode: str
    caption_entities: list[MessageEntity]
    duration: int
    disable_notification: bool
    protect_content: bool
    reply_to_message_id: int
    allow_sending_without_reply: bool
    reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply


class SendVideoNote(API):
    _result: Message

    chat_id: int | str
    message_thread_id: int
    video_note: InputFile | str
    duration: int
    length: int
    thumb: InputFile | str
    disable_notification: bool
    protect_content: bool
    reply_to_message_id: int
    allow_sending_without_reply: bool
    reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply


class SendMediaGroup(API):
    _result: Message

    chat_id: int | str
    message_thread_id: int
    media: list[InputMediaAudio | InputMediaVideo | InputMediaDocument | InputMediaPhoto]
    disable_notification: bool
    protect_content: bool
    reply_to_message_id: int
    allow_sending_without_reply: bool


class SendLocation(API):
    _result: Message

    chat_id: int | str
    message_thread_id: int
    latitude: float
    longitude: float
    horizontal_accuracy: float
    live_period: int
    heading: int
    proximity_alert_radius: int
    disable_notification: bool
    protect_content: bool
    reply_to_message_id: int
    allow_sending_without_reply: bool
    reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply


class EditMessageLiveLocation(API):
    _result: Message

    chat_id: int | str
    message_id: int
    inline_message_id: str
    latitude: float
    longitude: float
    horizontal_accuracy: float
    heading: int
    proximity_alert_radius: int
    reply_markup: InlineKeyboardMarkup


class StopMessageLiveLocation(API):
    _result: Message

    chat_id: int | str
    message_id: int
    inline_message_id: str
    reply_markup: InlineKeyboardMarkup


class SendVenue(API):
    _result: Message

    chat_id: int | str
    message_thread_id: int
    latitude: float
    longitude: float
    title: str
    address: str
    foursquare_id: str
    foursquare_type: str
    google_place_id: str
    google_place_type: str
    disable_notification: bool
    protect_content: bool
    reply_to_message_id: int
    allow_sending_without_reply: bool
    reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply


class SendContact(API):
    _result: Message

    chat_id: int | str
    message_thread_id: int
    phone_number: str
    first_name: str
    last_name: str
    vcard: str
    disable_notification: bool
    protect_content: bool
    reply_to_message_id: int
    allow_sending_without_reply: bool
    reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply


class SendPoll(API):
    _result: Message

    chat_id: int | str
    message_thread_id: int
    question: str
    options: list[str]
    is_anonymous: bool
    type: str
    allows_multiple_answers: bool
    correct_option_id: int
    explanation: str
    explanation_parse_mode: str
    explanation_entities: list[MessageEntity]
    open_period: int
    close_date: int
    is_closed: bool
    disable_notification: bool
    protect_content: bool
    reply_to_message_id: int
    allow_sending_without_reply: bool
    reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply


class SendDice(API):
    _result: Message

    chat_id: int | str
    message_thread_id: int
    emoji: str
    disable_notification: bool
    protect_content: bool
    reply_to_message_id: int
    allow_sending_without_reply: bool
    reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply


class SendChatAction(API):
    _result: bool

    chat_id: int | str
    message_thread_id: int
    action: str


class GetUserProfilePhotos(API):
    _result: UserProfilePhotos

    user_id: int
    offset: int
    limit: int


class BanChatMember(API):
    _result: bool

    chat_id: int | str
    user_id: int
    until_date: int
    revoke_messages: bool


class UnbanChatMember(API):
    _result: bool

    chat_id: int | str
    user_id: int
    only_if_banned: bool


class RestrictChatMember(API):
    _result: bool

    chat_id: int | str
    user_id: int
    permissions: ChatPermissions
    until_date: int


class PromoteChatMember(API):
    _result: bool

    chat_id: int | str
    user_id: int
    is_anonymous: bool
    can_manage_chat: bool
    can_post_messages: bool
    can_edit_messages: bool
    can_delete_messages: bool
    can_manage_video_chats: bool
    can_restrict_members: bool
    can_promote_members: bool
    can_change_info: bool
    can_invite_users: bool
    can_pin_messages: bool
    can_manage_topics: bool


class SetChatAdministratorCustomTitle(API):
    _result: bool

    chat_id: int | str
    user_id: int
    custom_title: str


class BanChatSenderChat(API):
    _result: bool

    chat_id: int | str
    sender_chat_id: int


class UnbanChatSenderChat(API):
    _result: bool

    chat_id: int | str
    sender_chat_id: int


class SetChatPermissions(API):
    _result: bool

    chat_id: int | str
    permissions: ChatPermissions


class ExportChatInviteLink(API):
    _result: bool

    chat_id: int | str


class CreateChatInviteLink(API):
    _result: ChatInviteLink

    chat_id: int | str
    name: str
    expire_date: int
    member_limit: int
    creates_join_request: bool


class EditChatInviteLink(API):
    _result: ChatInviteLink

    chat_id: int | str
    invite_link: str
    name: str
    expire_date: int
    member_limit: int
    creates_join_request: bool


class RevokeChatInviteLink(API):
    _result: ChatInviteLink

    chat_id: int | str
    invite_link: str


class ApproveChatJoinRequest(API):
    _result: bool

    chat_id: int | str
    user_id: int


class DeclineChatJoinRequest(API):
    _result: bool

    chat_id: int | str
    user_id: int


class SetChatPhoto(API):
    _result: bool

    chat_id: int | str
    photo: InputFile


class DeleteChatPhoto(API):
    _result: bool

    chat_id: int | str


class SetChatTitle(API):
    _result: bool

    chat_id: int | str
    title: str


class SetChatDescription(API):
    _result: bool

    chat_id: int | str
    description: str


class PinChatMessage(API):
    _result: bool

    chat_id: int | str
    message_id: int
    disable_notification: bool


class UnpinChatMessage(API):
    _result: bool

    chat_id: int | str
    message_id: int


class UnpinAllChatMessages(API):
    _result: bool

    chat_id: int | str


class LeaveChat(API):
    _result: bool

    chat_id: int | str


class GetChat(API):
    _result: Chat

    chat_id: int | str


class GetChatAdministrators(API):
    _result: list[ChatMember]

    chat_id: int | str


class GetChatMemberCount(API):
    _result: int

    chat_id: int | str


class GetChatMember(API):
    _result: ChatMember

    chat_id: int | str
    user_id: int


class SetChatStickerSet(API):
    _result: bool

    chat_id: int | str
    sticker_set_name: str


class DeleteChatStickerSet(API):
    _result: bool

    chat_id: int | str


class GetForumTopicIconStickers(API):
    _result: list[Sticker]


class CreateForumTopic(API):
    _result: ForumTopic

    chat_id: int | str
    name: str
    icon_color: int
    icon_custom_emoji_id: str


class EditForumTopic(API):
    _result: ForumTopic

    chat_id: int | str
    message_thread_id: int
    name: str
    icon_custom_emoji_id: str


class CloseForumTopic(API):
    _result: bool

    chat_id: int | str
    message_thread_id: int


class ReopenForumTopic(API):
    _result: bool

    chat_id: int | str
    message_thread_id: int


class DeleteForumTopic(API):
    _result: bool

    chat_id: int | str
    message_thread_id: int


class UnpinAllForumTopicMessages(API):
    _result: bool

    chat_id: int | str
    message_thread_id: int


class EditGeneralForumTopic(API):
    _result: bool

    chat_id: int | str
    name: str


class CloseGeneralForumTopic(API):
    _result: bool

    chat_id: int | str


class ReopenGeneralForumTopic(API):
    _result: bool

    chat_id: int | str


class HideGeneralForumTopic(API):
    _result: bool

    chat_id: int | str


class UnhideGeneralForumTopic(API):
    _result: bool

    chat_id: int | str


class AnswerCallbackQuery(API):
    _result: bool

    callback_query_id: str
    text: str
    show_alert: bool
    url: str
    cache_time: int


class SetMyCommands(API):
    _result: bool

    commands: list[BotCommand]
    scope: BotCommandScope
    language_code: str


class DeleteMyCommands(API):
    _result: bool

    scope: BotCommandScope
    language_code: str


class GetMyCommands(API):
    _result: list[BotCommand]

    scope: BotCommandScope
    language_code: str


class SetChatMenuButton(API):
    _result: bool

    chat_id: int
    menu_button: MenuButton


class GetChatMenuButton(API):
    _result: MenuButton

    chat_id: int


class SetMyDefaultAdministratorRights(API):
    _result: bool

    rights: ChatAdministratorRights
    for_channels: bool


class GetMyDefaultAdministratorRights(API):
    _result: ChatAdministratorRights

    for_channels: bool


class EditMessageText(API):
    _result: Message

    chat_id: int | str
    message_id: int
    inline_message_id: str
    text: str
    parse_mode: str
    entities: list[MessageEntity]
    disable_web_page_preview: bool
    reply_markup: InlineKeyboardMarkup


class EditMessageCaption(API):
    _result: Message

    chat_id: int | str
    message_id: int
    inline_message_id: str
    caption: str
    parse_mode: str
    caption_entities: list[MessageEntity]
    reply_markup: InlineKeyboardMarkup


class EditMessageMedia(API):
    _result: Message

    chat_id: int | str
    message_id: int
    inline_message_id: str
    media: InputMedia
    reply_markup: InlineKeyboardMarkup


class EditMessageReplyMarkup(API):
    _result: Message

    chat_id: int | str
    message_id: int
    inline_message_id: str
    reply_markup: InlineKeyboardMarkup


class StopPoll(API):
    _result: Poll

    chat_id: int | str
    message_id: int
    reply_markup: InlineKeyboardMarkup


class DeleteMessage(API):
    _result: bool

    chat_id: int | str
    message_id: int
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


class SendSticker(API):
    _result: Message

    chat_id: int | str
    message_thread_id: int
    sticker: InputFile | str
    disable_notification: bool
    protect_content: bool
    reply_to_message_id: int
    allow_sending_without_reply: bool
    reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply


class GetStickerSet(API):
    _result: StickerSet

    name: str


class GetCustomEmojiStickers(API):
    _result: list[Sticker]

    custom_emoji_ids: list[str]


class UploadStickerFile(API):
    _result: File

    user_id: int
    png_sticker: InputFile | str


class CreateNewStickerSet(API):
    _result: bool

    user_id: int
    name: str
    title: str
    png_sticker: InputFile | str
    tgs_sticker: InputFile | str
    webm_sticker: InputFile | str
    sticker_type: str
    emojis: str
    mask_position: MaskPosition


class AddStickerToSet(API):
    _result: bool

    user_id: int
    name: str
    png_sticker: InputFile | str
    tgs_sticker: InputFile | str
    webm_sticker: InputFile | str
    emojis: str
    mask_position: MaskPosition


class SetStickerPositionInSet(API):
    _result: bool

    sticker: str
    position: int


class DeleteStickerFromSet(API):
    _result: bool

    sticker: str


class SetStickerSetThumb(API):
    _result: bool

    name: str
    user_id: int
    thumb: InputFile | str


class AnswerInlineQuery(API):
    _result: bool

    inline_query_id: str
    results: list[InlineQueryResult]
    cache_time: int
    is_personal: bool
    next_offset: str
    switch_pm_text: str
    switch_pm_parameter: str


class AnswerWebAppQuery(API):
    _result: SentWebAppMessage

    web_app_query_id: str
    result: InlineQueryResult


class SendInvoice(API):
    _result: Message

    chat_id: int | str
    message_thread_id: int
    title: str
    description: str
    payload: str
    provider_token: str
    currency: str
    prices: list[LabeledPrice]
    max_tip_amount: int
    suggested_tip_amounts: list[int]
    start_parameter: str
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
    disable_notification: bool
    protect_content: bool
    reply_to_message_id: int
    allow_sending_without_reply: bool
    reply_markup: InlineKeyboardMarkup


class CreateInvoiceLink(API):
    _result: bool

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


class AnswerShippingQuery(API):
    _result: bool

    shipping_query_id: str
    ok: bool
    shipping_options: list[ShippingOption]
    error_message: str


class AnswerPreCheckoutQuery(API):
    _result: bool

    pre_checkout_query_id: str
    ok: bool
    error_message: str


class SetPassportDataErrors(API):
    _result: bool

    user_id: int
    errors: list[PassportElementError]


class SendGame(API):
    _result: Message

    chat_id: int | str
    message_thread_id: int
    game_short_name: str
    disable_notification: bool
    protect_content: bool
    reply_to_message_id: int
    allow_sending_without_reply: bool
    reply_markup: InlineKeyboardMarkup


class SetGameScore(API):
    _result: Message

    user_id: int
    score: int
    force: bool
    disable_edit_message: bool
    chat_id: int | str
    message_id: int
    inline_message_id: str


class GetGameHighScores(API):
    _result: list[GameHighScore]

    user_id: int
    chat_id: int | str
    message_id: int
    inline_message_id: str

import logging
# from telegram import Updater, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filter, CallbackContext

# Source group
source_group_id = -1001951006269
# Target group
target_group_id = -1001661936464
# Bot token
bot_token = '5964334978:AAFCFR2Ea2yTNc4bVGcWi2ouihJY4d_X9ss'

# logining settings
logging.basicConfig(format='%(asctime)s-%(name)s-%(levelname)s-%(message)s', level=logging.INFO)
loger = logging.getLogger(__name__)

                               # parameter: parameter_type
def hendle_message(update: Update, context: CallbackContext):
    message = update.message
    text = message.text
    photos = message.photo
    videos = message.video

    context.bot.send_message(chat_id=target_group_id, text=text)
    for photo in photos:
        context.bot.send_photo(chat_id=target_group_id, photo=photo)
    for video in videos:
        context.bot.send_video(chat_id=target_group_id, video=video)

updater = Updater(token=bot_token, use_context=True)

dispatcher = updater.dispatcher

message_hendler = MessageHandler(Filter.chat(source_group_id) & Filter.text, hendle_message)
dispatcher.add_handler(message_hendler)

updater.start_polling()
import logging
from telegram import Update
from telegram.ext import Updater, MessageHandler, CallbackContext, Filters

# Source group
source_group_id =
# Target group
target_group_id =
# Bot token
bot_token = ''

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

message_hendler = MessageHandler(Filters.chat(source_group_id), hendle_message)
dispatcher.add_handler(message_hendler)

updater.start_polling()
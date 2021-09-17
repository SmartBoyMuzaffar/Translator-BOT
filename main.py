from googletrans import Translator
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


m = Translator()


def start(update, context):
        """Send a message when the command /start is issued."""
        user = update.message.from_user
        update.message.reply_text('Salom {} \n Hush kelibsiz!!!'.format(user['username'])



def translate(update, context):
        """Echo the user message."""
        update.message.reply_html("""<code>
Tarjimasi: \n </code>
""" + m.translate(f"<code> {update.message.text} </code>", dest='uz').text)





def main():
    """Start the bot."""
    updater = Updater("1951916813:AAGBgKKsJZfdbXfCBQazEBcuF2xaNZmWnmY")
    M = updater.dispatcher
    M.add_handler(CommandHandler("start", start))
    M.add_handler(MessageHandler(Filters.text & ~Filters.command, translate))
    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()

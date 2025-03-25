from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Вставь сюда свой токен
TOKEN = '7394391595:AAFdJ2IvHWMhdBNP6Qy1lob1-s1Ef0zVLrQ'

# Замените на ваш ID, который вы получили
MY_USER_ID = 1647743009  # Пример ID

async def start(update: Update, context) -> None:
    await update.message.reply_text(' ✧･ﾟ: *✧･ﾟ:* ✧ \n Привет! Я бот канала You&Me. Моя владелица сейчас занята, но постарается ответить вам, как только увидит сообщение. Не расстраивайтесь, если она не ответит сразу — даже мне она отвечает не всегда.')

async def handle_message(update: Update, context) -> None:
    user_message = update.message.text  # Получаем текст сообщения от пользователя
    chat_id = update.message.chat_id  # ID чата пользователя

    # Отправляем заявку вам в личку
    await context.bot.send_message(chat_id=MY_USER_ID, text=f"Новое сообщение :\n\n{user_message}")
    
    # Сообщение для пользователя
    await update.message.reply_text("✧✧✧✧✧✧✧ \n Любое, даже самое маленькое взаимодействие с ботом очень радует нашу владелицу! Мы с удовольствием примем вашу заявку и будем ждать новых сообщений. ")

def main() -> None:
    # Создаем объект Application для работы с ботом
    application = Application.builder().token(TOKEN).build()

    # Добавляем команду /start
    application.add_handler(CommandHandler("start", start))

    # Добавляем обработчик для текстовых сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()

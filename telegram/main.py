import telebot
import threading
import time
import random  # Не забывайте импортировать random

# Создаем экземпляр бота
bot = telebot.TeleBot('7612971147:AAH36SwnOjJxGdC0P92Qxz4Axa9pjiRCZ9U')

# Множество для хранения chat_id пользователей, которым нужно отправлять сообщения
active_users = {1228215570}

# Список мотивационных сообщений
motivational_messages = [
    "Ты способен на большее, чем ты думаешь!",
    "Продолжай двигаться вперед! Маленькие шаги приводят к большим победам 🚀",
    "Каждый день — это новая возможность стать лучше!",
    "Ты делаешь отличный прогресс, не сдавайся 💪",
    "Улыбнись, и весь мир улыбнется тебе! 😊"
]

# Функция для отправки мотивационных сообщений
def send_motivational_messages():
    while True:
        try:
            for chat_id in active_users:  # Для множества просто итерация без .keys()
                message = random.choice(motivational_messages)  # Выбираем случайное сообщение
                bot.send_message(chat_id, message)
            time.sleep(120)  # Отправка каждые 2 минуты
        except Exception as e:
            print(f"Ошибка при отправке сообщения: {e}")
            time.sleep(5)  # Если ошибка, повтор через 5 секунд

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id, 
        f"Привет, {message.from_user.first_name}! Я буду отправлять тебе мотивационные сообщения. Напиши /subscribe, чтобы подписаться!"
    )

# Обработчик команды /subscribe
@bot.message_handler(commands=['subscribe'])
def subscribe(message):
    chat_id = message.chat.id
    if chat_id not in active_users:
        active_users.add(chat_id)  # Используем .add() для множества
        bot.send_message(chat_id, "Вы подписаны на мотивационные сообщения! Я буду отправлять их каждые 2 минуты 😊")
    else:
        bot.send_message(chat_id, "Вы уже подписаны на мотивационные сообщения.")

# Обработчик команды /unsubscribe
@bot.message_handler(commands=['unsubscribe'])
def unsubscribe(message):
    chat_id = message.chat.id
    if chat_id in active_users:
        active_users.remove(chat_id)  # Используем .remove() для множества
        bot.send_message(chat_id, "Вы отписались от мотивационных сообщений. Если передумаете, напишите /subscribe.")
    else:
        bot.send_message(chat_id, "Вы не были подписаны на мотивационные сообщения.")

# Обработчик команды /id
@bot.message_handler(commands=['id'])
def send_chat_id(message):
    bot.send_message(message.chat.id, f"Ваш chat_id: {message.chat.id}")

# Запускаем поток для отправки мотивационных сообщений
motivational_thread = threading.Thread(target=send_motivational_messages)
motivational_thread.daemon = True
motivational_thread.start()

bot.polling(none_stop=True)
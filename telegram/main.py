import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.enums import ParseMode, ChatAction
from aiogram.utils.markdown import hbold
from g4f.client import Client
from typing import List, Dict, Set
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# Enable logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class GPTService:
    def __init__(self):
        self.client = Client()
        self.conversations: Dict[int, List[Dict]] = {}
        self.max_history = 10
        
        self.system_prompt = """Вы являетесь ИИ-ассистентом образовательной платформы Expera. Ваша основная роль - помогать студентам в их образовательном пути, предоставлять информацию о курсах и поддерживать их мотивацию и информированность. Следуйте этим ключевым принципам в общении:

ЛИЧНОСТЬ И СТИЛЬ ОБЩЕНИЯ:
- Будьте дружелюбным, поддерживающим и ободряющим
- Используйте позитивный язык и сохраняйте профессиональный, но доступный тон
- Проявляйте энтузиазм к обучению и успехам студентов
- Пишите простым и понятным языком, подходящим для учащихся
- Используйте уместные эмодзи для вовлечения в разговор 📚✨

ОСНОВНЫЕ ОБЯЗАННОСТИ:

1. МОТИВАЦИОННАЯ ПОДДЕРЖКА:
- Предоставляйте персонализированные мотивационные сообщения
- Фокусируйтесь на развитии мышления и прогрессе в обучении
- Делитесь релевантными историями успеха и советами по обучению
- Используйте ободряющие фразы и отмечайте маленькие победы
- Запоминайте прогресс студентов и упоминайте его в разговорах

2. РЕКОМЕНДАЦИИ ПО КУРСАМ:
- Задавайте уточняющие вопросы о:
  * Текущем уровне знаний
  * Целях обучения
  * Доступном времени
  * Предпочтительном стиле обучения
  * Бюджетных ограничениях

3. ПОДДЕРЖКА В ОБУЧЕНИИ:
- Отвечайте на вопросы о содержании курсов и материалах
- Объясняйте сложные темы простыми словами
- Разбивайте сложные концепции на управляемые части
- Приводите релевантные примеры и аналогии
- Направляйте студентов к дополнительным ресурсам

4. КРУГЛОСУТОЧНАЯ ПОДДЕРЖКА:
- Предоставляйте помощь 24/7 по вопросам:
  * Технических проблем
  * Доступа к курсам
  * Разъяснения заданий
  * Общих вопросов
- Ведите подробную историю разговоров
- Знайте, когда передать вопрос человеку-специалисту
- Предоставляйте контакты для экстренной связи

5. УПРАВЛЕНИЕ РАСПИСАНИЕМ:
- Отслеживайте и информируйте о:
  * Предстоящих занятиях
  * Дедлайнах заданий
  * Датах начала курсов
  * Расписании экзаменов
- Отправляйте своевременные напоминания
- Помогайте с конфликтами в расписании
- Предлагайте альтернативные варианты

СТРУКТУРА ОТВЕТОВ:
1. Подтвердите получение запроса
2. Предоставьте четкую, релевантную информацию
3. Добавьте мотивационный элемент, где уместно
4. Укажите следующие шаги или действия
5. Предложите дополнительную помощь

БАЗА ЗНАНИЙ:
- Каталог курсов
- Расписание и доступность занятий
- Цены и варианты оплаты
- Предварительные требования
- Образовательные траектории и сертификации
- Технические требования
- Ресурсы поддержки

ОСОБЫЕ ИНСТРУКЦИИ:
1. При предоставлении информации о расписании всегда указывайте дату, время и часовой пояс
2. Для рекомендаций курсов всегда объясняйте предварительные требования и ожидаемые результаты
3. При решении технических проблем предоставляйте пошаговые инструкции
4. Включайте ссылки на учебные материалы или ресурсы, когда это применимо
5. Поддерживайте контекст разговора и ссылайтесь на предыдущие взаимодействия
6. Всегда подтверждайте понимание перед предоставлением решений

КРИТИЧЕСКИ ВАЖНЫЕ ОТВЕТЫ:

Для запросов о курсах:
"[Название курса] требует [предварительные требования]. Учитывая ваш опыт в [упомянутый опыт], я рекомендую начать с [конкретный уровень/курс]. Курс включает [ключевые компоненты] и поможет вам достичь [конкретные цели]."

Для вопросов о расписании:
"Следующее занятие по [предмет] уровня [уровень] состоится [дата/время]. Хотите, чтобы я напомнил вам об этом за час до начала?"

Для мотивации:
"🌟 [Имя студента], вы отлично продвигаетесь в изучении [предмет]! Уже пройдено [X] уроков, и я вижу значительный прогресс в [конкретный навык]. Продолжайте в том же духе!"

Для технической поддержки:
"Давайте решим эту проблему пошагово. Сначала проверьте [первый шаг]. Если это не помогает, попробуйте [следующий шаг]. Я здесь, чтобы помочь вам на каждом этапе."

ОБРАБОТКА ОШИБОК:
- Если информация недоступна, объясните причину и предложите альтернативы
- Если потребности студента превышают возможности бота, знайте, как связать его с человеком-специалистом
- Всегда сохраняйте ориентацию на решение

Помните:
- Держите ответы краткими, но информативными
- Используйте позитивное подкрепление
- Оставайтесь в образовательном контексте
- Приоритизируйте успех и удовлетворенность студента
- Поддерживайте постоянный энтузиазм и поддержку"""

    def add_message_to_history(self, chat_id: int, role: str, content: str) -> None:
        if chat_id not in self.conversations:
            self.conversations[chat_id] = []

        self.conversations[chat_id].append({
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat()
        })

        if len(self.conversations[chat_id]) > self.max_history:
            self.conversations[chat_id] = self.conversations[chat_id][-self.max_history:]

    def format_messages_for_g4f(self, chat_id: int) -> List[Dict[str, str]]:
        messages = [
            {"role": "system", "content": self.system_prompt}
        ]
        
        for msg in self.conversations.get(chat_id, []):
            messages.append({
                "role": msg["role"],
                "content": msg["content"]
            })
            
        return messages

    async def get_gpt_response(self, chat_id: int, user_message: str) -> str:
        try:
            self.add_message_to_history(chat_id, "user", user_message)
            messages = self.format_messages_for_g4f(chat_id)
            
            response = await asyncio.to_thread(
                self.client.chat.completions.create,
                model="gpt-4",
                messages=messages,
                temperature=0.7,
                max_tokens=2000
            )
            
            response_text = response.choices[0].message.content.strip()
            self.add_message_to_history(chat_id, "assistant", response_text)
            
            return response_text

        except Exception as e:
            logger.error(f"Error getting GPT response: {str(e)}")
            raise

    def clear_history(self, chat_id: int) -> None:
        self.conversations[chat_id] = []

# Initialize bot and dispatcher
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()
gpt_service = GPTService()

# Set of active users for motivational messages
active_users: Set[int] = set()

# Motivational messages task
async def send_motivational_messages():
    while True:
        try:
            for chat_id in active_users:
                try:
                    motivation_request = "Generate a short, personalized motivational message for a student learning new skills. Make it inspiring and concise."
                    response = await gpt_service.get_gpt_response(chat_id, motivation_request)
                    await bot.send_message(chat_id, response)
                except Exception as e:
                    logger.error(f"Error sending motivation to {chat_id}: {e}")
            
            await asyncio.sleep(120)  # 2 minutes
        except Exception as e:
            logger.error(f"Motivation task error: {e}")
            await asyncio.sleep(5)

@dp.message(Command("start"))
async def cmd_start(message: Message):
    kb = [
        [
            types.KeyboardButton(text="/subscribe"),
            types.KeyboardButton(text="/unsubscribe")
        ],
        [
            types.KeyboardButton(text="/clear"),
            types.KeyboardButton(text="/help")
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Задайте ваш вопрос..."
    )
    
    welcome_text = (
        f"👋 Привет, {hbold(message.from_user.first_name)}!\n\n"
        "Я ваш образовательный ассистент. Помогу вам с:\n"
        "• Подбором курсов\n"
        "• Ответами на вопросы\n"
        "• Расписанием занятий\n"
        "• Поддержкой 24/7\n\n"
        "Доступные команды:\n"
        "/subscribe - получать мотивационные сообщения\n"
        "/unsubscribe - отключить мотивационные сообщения\n"
        "/clear - очистить историю диалога\n"
        "/help - показать все возможности"
    )
    
    await message.answer(
        welcome_text,
        parse_mode=ParseMode.HTML,
        reply_markup=keyboard
    )

@dp.message(Command("subscribe"))
async def cmd_subscribe(message: Message):
    chat_id = message.chat.id
    if chat_id not in active_users:
        active_users.add(chat_id)
        await message.answer("✨ Вы подписались на мотивационные сообщения! Я буду поддерживать ваш настрой каждые 2 минуты.")
    else:
        await message.answer("Вы уже подписаны на мотивационные сообщения.")

@dp.message(Command("unsubscribe"))
async def cmd_unsubscribe(message: Message):
    chat_id = message.chat.id
    if chat_id in active_users:
        active_users.remove(chat_id)
        await message.answer("Вы отписались от мотивационных сообщений. Надеюсь, они были полезны!")
    else:
        await message.answer("Вы не были подписаны на мотивационные сообщения.")

@dp.message(Command("clear"))
async def cmd_clear(message: Message):
    try:
        gpt_service.clear_history(message.chat.id)
        await message.answer("✨ История диалога очищена!")
    except Exception as e:
        logger.error(f"Error clearing history: {e}")
        await message.answer("❌ Произошла ошибка при очистке истории.")

@dp.message(Command("help"))
async def cmd_help(message: Message):
    help_text = """
🎓 Вот что я умею:

1️⃣ Подбор курсов
- Задам вопросы о ваших целях
- Предложу подходящие курсы
- Расскажу о требованиях

2️⃣ Ответы на вопросы
- О программах обучения
- О расписании
- О технических требованиях

3️⃣ Мотивация
- Регулярные мотивационные сообщения
- Поддержка в обучении
- Советы по эффективному обучению

4️⃣ Расписание
- Информация о занятиях
- Напоминания
- Уведомления об изменениях

Просто спросите меня о чем угодно, связанном с обучением! 📚
"""
    await message.answer(help_text)

@dp.message()
async def process_message(message: Message):
    try:
        chat_id = message.chat.id
        user_message = message.text

        await bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)
        
        response = await gpt_service.get_gpt_response(chat_id, user_message)
        await message.answer(response)
        
    except Exception as e:
        logger.error(f"Error processing message: {e}")
        error_message = (
            "😔 Извините, произошла ошибка при обработке вашего сообщения.\n"
            "Пожалуйста, попробуйте позже или начните новый диалог командой /clear"
        )
        await message.answer(error_message)

async def main():
    try:
        logger.info("Starting bot...")
        asyncio.create_task(send_motivational_messages())
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Critical error: {e}")
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(main())
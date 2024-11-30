import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.enums import ParseMode, ChatAction
from aiogram.utils.markdown import hbold
from config import TELEGRAM_TOKEN
from gpt_service import GPTService

# Enable logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize bot, dispatcher and GPT service
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()
gpt_service = GPTService()

@dp.message(Command("start"))
async def cmd_start(message: Message):
    """Handle /start command"""
    kb = [
        [
            types.KeyboardButton(text="/clear"),
            types.KeyboardButton(text="/history")
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Задайте ваш вопрос..."
    )
    
    welcome_text = (
        f"👋 Привет, {hbold(message.from_user.first_name)}!\n\n"
        "Я бот с GPT. Задайте мне любой вопрос, и я постараюсь помочь.\n\n"
        "Доступные команды:\n"
        "/clear - очистить историю диалога\n"
        "/history - показать историю диалога"
    )
    
    await message.answer(
        welcome_text,
        parse_mode=ParseMode.HTML,
        reply_markup=keyboard
    )

@dp.message(Command("clear"))
async def cmd_clear(message: Message):
    """Handle /clear command"""
    try:
        gpt_service.clear_history(message.chat.id)
        await message.answer("✨ История диалога очищена!")
    except Exception as e:
        logger.error(f"Error clearing history: {e}")
        await message.answer("❌ Произошла ошибка при очистке истории.")

@dp.message(Command("history"))
async def cmd_history(message: Message):
    """Handle /history command"""
    try:
        history = gpt_service.get_formatted_history(message.chat.id)
        await message.answer(history)
    except Exception as e:
        logger.error(f"Error getting history: {e}")
        await message.answer("❌ Произошла ошибка при получении истории.")

@dp.message()
async def process_message(message: Message):
    """Handle all other messages"""
    try:
        chat_id = message.chat.id
        user_message = message.text

        await bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)
        
        response = await gpt_service.get_gpt_response(chat_id, user_message)
        
        if response:
            await message.answer(response)
        else:
            await message.answer("😔 Извините, не удалось получить ответ. Попробуйте еще раз.")
        
    except Exception as e:
        logger.error(f"Error processing message: {e}")
        error_message = (
            "😔 Извините, произошла ошибка при обработке вашего сообщения.\n"
            "Пожалуйста, попробуйте позже или начните новый диалог командой /clear"
        )
        await message.answer(error_message)

async def main():
    """Main function to start the bot"""
    try:
        logger.info("Starting bot...")
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Critical error: {e}")
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(main())
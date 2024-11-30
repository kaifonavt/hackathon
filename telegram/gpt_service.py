from g4f.client import Client
from typing import List, Dict, Optional
import logging
from datetime import datetime
import asyncio

class GPTService:
    def __init__(self):
        """Initialize the GPT service using g4f client"""
        self.client = Client()
        self.conversations: Dict[int, List[Dict]] = {}
        self.max_history = 10
        self.setup_logging()

    def setup_logging(self):
        """Set up logging configuration"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            filename='gpt_service.log'
        )
        self.logger = logging.getLogger(__name__)

    def add_message_to_history(self, chat_id: int, role: str, content: str) -> None:
        """Add a message to the conversation history"""
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
        """Format conversation history for g4f"""
        messages = [
            {"role": "system", "content": "You are a helpful assistant."}
        ]
        
        for msg in self.conversations.get(chat_id, []):
            messages.append({
                "role": msg["role"],
                "content": msg["content"]
            })
            
        return messages

    async def get_gpt_response(self, chat_id: int, user_message: str) -> str:
        """Get response from GPT model using g4f client"""
        try:
            self.add_message_to_history(chat_id, "user", user_message)
            messages = self.format_messages_for_g4f(chat_id)
            
            self.logger.info("Sending request to GPT")
            response = await asyncio.to_thread(
                self.client.chat.completions.create,
                model="gpt-4",  # You can change this to other models like "gpt-3.5-turbo"
                messages=messages
            )
            
            response_text = response.choices[0].message.content.strip()
            self.add_message_to_history(chat_id, "assistant", response_text)
            
            return response_text

        except Exception as e:
            error_msg = f"Error getting GPT response: {str(e)}"
            self.logger.error(error_msg)
            raise Exception(error_msg)

    def get_formatted_history(self, chat_id: int) -> str:
        """Get formatted conversation history"""
        history = self.conversations.get(chat_id, [])
        if not history:
            return "История диалога пуста!"

        formatted_history = "История диалога:\n\n"
        for msg in history:
            timestamp = datetime.fromisoformat(msg['timestamp']).strftime('%H:%M:%S')
            role = "Пользователь" if msg['role'] == "user" else "Ассистент"
            formatted_history += f"[{timestamp}] {role}:\n{msg['content']}\n\n"

        return formatted_history

    def clear_history(self, chat_id: int) -> None:
        """Clear conversation history for a chat"""
        self.conversations[chat_id] = []
from telegram import Bot

def send_test_link_to_telegram(test_link, chat_id, bot_token):
    bot = Bot(token=bot_token)
    message = f"Пройдите тест: {test_link}"
    
    try:
        bot.send_message(chat_id, text=message)
        return True
    except Exception as e:
        print(f"Ошибка отправки сообщения в Telegram: {e}")
        return False

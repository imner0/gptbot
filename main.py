import openai
import telebot

# Set up OpenAI API key
openai.api_key = 'your_api_key_here'

# Create Telebot instance
bot = telebot.TeleBot('your_bot_token_here')

# Define message handler function
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    prompt = f"User: {message.text}\nAI:"
    response = openai.Completion.create(
        engine="davinci", prompt=prompt, max_tokens=1024
    )
    bot.reply_to(message, response.choices[0].text)

# Start bot polling
if __name__ == '__main__':
    bot.polling()

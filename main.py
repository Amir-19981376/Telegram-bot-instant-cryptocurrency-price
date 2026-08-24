import telebot
import requests

TOKEN= "8649692518:AAHgHFXmWhPq--oqeqEFhfHrBmVcc9BaAjA"
bot = telebot.TeleBot(TOKEN)
URL ="https://api.binance.com/api/v3/ticker/price?symbol=BTCUSD"

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Hi im amir what can i do for you?")

@bot.message_handler(func=lambda m: True)
def show_price(message):
	symbol = message.text.upper()
	response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}")
	print(response)
	if response.status_code == 200:
		data =response.json()
		bot.reply_to(message, f"{data['symbol']} price is{data['price']}")
	else:
		bot.reply_to(message, "Something went wrong")

bot.infinity_polling()
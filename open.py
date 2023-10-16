from aiogram import Bot, Dispatcher, types, executor
import subprocess
import requests

def send_to_telegram(message):

    apiToken = '6628897049:AAGzSfvTc8xSMpX9wMFiU7OF-PLBx0VMPDU'
    chatID = '673968568'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(
            apiURL, json={'chat_id': chatID, 'text': message})
        # print(response.text)
    except Exception as e:
        print(e)


bot = Bot(token="6628897049:AAGzSfvTc8xSMpX9wMFiU7OF-PLBx0VMPDU")
dp = Dispatcher(bot)

@dp.message_handler(commands = ['start', 'help'])
async def welcome(message: types.Message):
  await message.reply('Hello! Im GPT chat bot. Ask me something')

@dp.message_handler(commands = ['command1'])
async def welcome(message: types.Message):
    subprocess.call([r'open_service.bat'])
    await message.reply('Service Started!!')

@dp.message_handler(commands = ['command2'])
async def welcome(message: types.Message):
    subprocess.call([r'close_service.bat'])
    await message.reply('Service Stoped!!')
  


@dp.message_handler()
async def a(message: types.Message):
    if message.text=="Hello":
       await message.reply(text="Welcome")
    else:
      await message.reply(text=message.text)


async def main() -> None:
    """"Entry Point"""
    await dp.start_polling(bot)

if __name__ == "__main__":
  send_to_telegram("Service is Running!!")
  executor.start_polling(dp)





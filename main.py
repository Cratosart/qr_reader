import qrcode
import secrets
import string
from aiogram import types, executor, Dispatcher, Bot
from aiogram.types import InputFile

TOKEN = '2136993706:AAFy2qLZkZPZLcDWGgltR0BGCtT0cIHt73M'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(20))
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(password)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode2.jpg", "JPEG")
# photo = InputFile('/home/artem/pipenv_demo/qr_create/qrcode2.jpg')


@dp.message_handler(commands='start')
async def begin(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, types.image(img))


executor.start_polling(dp)

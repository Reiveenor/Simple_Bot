from aiogram import Dispatcher, Bot, types
from aiogram.utils import executor
from requests import get

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands="albums")
async def bot_albums(message: types.Message):
    albums = []
    r = get("https://music.yandex.by/handlers/artist.jsx?artist=5286660")
    for i in range(len(r.json()["albums"])):
        albums.append(r.json()["albums"][i]["title"])
    await message.answer("\n".join(albums))


@dp.message_handler(commands="artist")
async def bot_artist(message: types.Message):
    r = get("https://music.yandex.by/handlers/artist.jsx?artist=5286660")
    artist = r.json()["artist"]["name"]
    genre = r.json()["artist"]["genres"][0]
    await message.answer(f"Artist: {artist}\nGenre: {genre}")


@dp.message_handler(commands="start")
async def bot_start(message: types.Message):
    await message.answer("Commands list:\n /artist\n /albums")

# @dp.message_handler()
# async def echo(message: types.Message):
#     await bot.send_message(message.from_user.id, message.text)


if __name__ == '__main__':
    executor.start_polling(dp)

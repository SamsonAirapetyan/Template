from aiogram import types, Dispatcher


async def catch_document(message: types.Message):
    await message.document.download()
    await message.reply("документ скачан\n"
                        f"<pre>FILE ID = {message.document.file_id}</pre>")


async def catch_audio(message: types.Message):
    await message.audio.download()
    await message.reply("Аудиозапись скачана\n",
                        f"<pre>FILE ID = {message.audio.file_id}</pre>")


def register_all_catch(dp: Dispatcher):
    dp.register_message_handler(catch_document, content_types=types.ContentType.DOCUMENT)
    dp.register_message_handler(catch_audio, content_types=types.ContentType.AUDIO)

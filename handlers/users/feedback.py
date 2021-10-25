from aiogram import types
from loader import dp

@dp.message_handler(commands = ['feedback'], state = "1")
async def feedback(message: types.Message) -> None:
	text = [
		f"Dzień dobry {message.chat.first_name}!",
		"Mogę robić coś takiego zamisat",
		"końcówek? :D",
	]
	await message.answer("\n".join(text))
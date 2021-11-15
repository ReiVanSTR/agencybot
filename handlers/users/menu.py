from aiogram import types
from aiogram.dispatcher.filters import Command
from loader import dp

@dp.message_handler(Command("menu"))
async def show_menu(message: types.Message):
	pass

async def load_vacancies(message: [types.Message, types.CallbackQuery])

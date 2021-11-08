from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states.createvacancy import Vacancy
from data.messages.createvacancy import messages

@dp.message_handler(Command("createvacancy"), state = None)
async def _start(message: types.Message) -> None:
	await message.answer(messages['title'])

	await Vacancy.title()

@dp.message_handler(state = Vacancy.title)
async def _set_title(message: types.Message, state: FSMContext) -> None:
	await message.answer('1')
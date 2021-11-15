from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states.createvacancy import Vacancy
from data.messages.createvacancy import messages
from utils.vacancyconstructor import Constructor

c = Constructor()

@dp.message_handler(Command("createvacancy"), state = None)
async def _start(message: types.Message) -> None:
	await message.answer(messages['title']['default'])

	await Vacancy.title.set()

@dp.message_handler(state = Vacancy.title)
async def _set_title(message: types.Message, state: FSMContext) -> None:
	try:
		title = message.text.strip()
		if 4 < len(title) < 25:
			await state.update_data({'title':title})
			await message.reply(title)
			await Vacancy.responsibilities.set()
		else:
			await message.answer(messages['title']['exception'])
	except:
		pass

@dp.message_handler(state=Vacancy.responsibilities)
async def _set_responsibilities(message: types.Message, state: FSMContext) -> None:
	await message.answer(messages['responsibilities']['default'])


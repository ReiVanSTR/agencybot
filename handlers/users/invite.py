from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states.invite import Invite

@dp.message_handler(Command("sighin"), state = None)
async def _start_invite(message: types.Message) -> None:
	await message.answer(f"{message.from_user.first_name} введите код приглашения: \n")

	await Invite.invite_code.set()


@dp.message_handler(state = Invite.invite_code)
async def _get_invite_key(message: types.Message, state: FSMContext) -> None:
	await message.answer("True")
	await state.update_data({'key':message.text})
	await Invite.next()

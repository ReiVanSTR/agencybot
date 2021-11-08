from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, AdminFilter

from loader import dp
from states.invite import Invite

@dp.message_handler(Command("sighin"),is_chat_admin = True ,state = None)
async def _start_invite(message: types.Message) -> None:
	await message.answer(f"{message.from_user.first_name} введите код приглашения: \n")

	await Invite.invite_code.set()


@dp.message_handler(state = Invite.invite_code)
async def _get_invite_key(message: types.Message, state: FSMContext) -> None:
	await message.answer("True, write name")
	await state.update_data({'key':message.text})
	await Invite.next()
	data = await state.get_data()
	print(data)

@dp.message_handler(state = Invite.admin_nickname)
async def _tt(message: types.Message, state: FSMContext) -> None:
	await message.answer("True 2")
	await state.update_data({'name':message.text})
	data = await state.get_data()
	print(data)
	await state.finish()
	await message.answer(f"Code: {data['key']} Name: {data['name']}")

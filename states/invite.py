"""Приглашения администатора используя код"""
from aiogram.dispatcher.filters.state import StatesGroup, State
from typing import Dict

class Invite(StatesGroup):
	invite_code = State()
	admin_nickname = State()
	admin_status = State()

	

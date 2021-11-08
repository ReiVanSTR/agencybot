"""ФМС для конструктора вакансий"""
from aiogram.dispatcher.filters.state import StatesGroup, State

class Vacancy(StatesGroup):
	title = State()
	responsibilities = State()
	requirements = State()
	rate = State()
	timetable = State()
	add_info = State() #additional information
	housing = State()
	city = State()

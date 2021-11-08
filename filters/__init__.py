from aiogram import Dispatcher

from loader import dp
# from .is_admin import AdminFilter
from .title import TitileLen


if __name__ == "filters":
    # dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(TitileLen)

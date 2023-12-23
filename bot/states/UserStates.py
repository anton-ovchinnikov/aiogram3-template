from aiogram.fsm.state import StatesGroup, State


class OrderStates(StatesGroup):
    set_firstname = State()
    set_lastname = State()
    set_age = State()

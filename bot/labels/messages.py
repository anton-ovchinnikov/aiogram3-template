from emoji import emojize

# USER
START_MSG = emojize(':wave: <b>Привет, {firstname}!</b>', language='alias')
USER_MSG = '<i>Сработала юзер кнопка!</i>'

# ADMIN
ADMIN_MSG = emojize(':gear: <b>Админ-панель</b>', language='alias')

# ALERTS
ADMIN_ALERT = emojize(':check_mark: Вы админ!', language='alias')

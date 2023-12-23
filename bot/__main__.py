import asyncio
import logging

from aiogram import Dispatcher, Bot
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncConnection

from bot.database.Database import Database
from bot.database.base import Base
from bot.handlers import menuHandlers, adminHandlers
from bot.middlewares.DatabaseMiddleware import DatabaseMiddleware
from configreader import config


async def main() -> None:
    logging.basicConfig(format='[%(asctime)s - %(name)s] %(levelname)s: %(message)s', level=logging.INFO)

    dp = Dispatcher()
    bot = Bot(token=config.BOT_TOKEN, parse_mode='html', protect_content=True)

    engine = create_async_engine(f"sqlite+aiosqlite:///database.sqlite", future=True, echo=True)

    conn: AsyncConnection
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    session = async_sessionmaker(engine, expire_on_commit=True).begin().async_session
    database = Database(session=session)

    dp.include_router(router=menuHandlers.router)
    dp.include_router(router=adminHandlers.router)

    dp.message.middleware(DatabaseMiddleware(database=database))
    dp.callback_query.middleware(DatabaseMiddleware(database=database))

    await bot.delete_webhook(drop_pending_updates=True)

    try:
        await dp.start_polling(bot)
    except KeyboardInterrupt:
        await session.close()
        await engine.dispose()
        await bot.close()


asyncio.run(main())

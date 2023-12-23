from datetime import datetime

from sqlalchemy import select
from sqlalchemy.dialects.sqlite import insert
from sqlalchemy.ext.asyncio import AsyncSession

from bot.database.models import User


# noinspection PyTypeChecker
class Database:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_user(self, chat_id: int, username: str) -> None:
        values = {'chat_id': chat_id, 'username': username, 'registered_at': datetime.now()}

        stmt = insert(User).values(**values).on_conflict_do_nothing()
        await self.session.execute(stmt)
        await self.session.commit()

    async def read_user(self, chat_id: int) -> User | None:
        stmt = select(User).where(User.chat_id == chat_id)
        user = await self.session.execute(stmt)
        return user.scalar_one_or_none()

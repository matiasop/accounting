from datetime import datetime

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from accounting.db.dependencies import get_db_session
from accounting.db.models.entries import Entry


class EntryDAO:
    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    async def create(
        self,
        description: str,
        type: str,
        datetime: datetime,
        category: str,
        subcategory: str,
        debit: int,
        credit: int,
        debit_account_id: int,
        credit_account_id: int,
    ) -> Entry:
        entry = Entry(
            description=description,
            datetime=datetime,
            category=category,
            subcategory=subcategory,
            type=type,
            debit=debit,
            credit=credit,
            debit_account_id=debit_account_id,
            credit_account_id=credit_account_id,
        )
        self.session.add(entry)
        await self.session.commit()
        await self.session.refresh(entry)
        return entry

    async def get_all(self) -> list[Entry]:
        raw_entries = await self.session.execute(select(Entry))
        return list(raw_entries.scalars().fetchall())

    async def get_by_id(self, entry_id: int) -> Entry | None:
        result = await self.session.execute(
            select(Entry).filter_by(id=entry_id),
        )
        return result.fetchone()

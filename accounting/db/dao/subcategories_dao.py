from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from accounting.db.dependencies import get_db_session
from accounting.db.models.subcategories import Subcategory


class SubcategoryDAO:
    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    async def create(self, category_id: int, name: str) -> Subcategory:
        subcategory = Subcategory(category_id=category_id, name=name)
        self.session.add(subcategory)
        await self.session.commit()
        await self.session.refresh(subcategory)
        return subcategory

    async def get_all(self) -> list[Subcategory]:
        raw_subcategories = await self.session.execute(select(Subcategory))
        return list(raw_subcategories.scalars().fetchall())

    async def get_by_id(self, subcategory_id: int) -> Subcategory | None:
        result = await self.session.execute(
            select(Subcategory).filter_by(id=subcategory_id),
        )
        return result.fetchone()

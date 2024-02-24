from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from accounting.db.dependencies import get_db_session
from accounting.db.models.categories import Category
from accounting.db.models.subcategories import Subcategory


class CategoryDAO:
    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    async def create(self, name: str) -> Category:
        category = Category(name=name)
        self.session.add(category)
        await self.session.commit()
        await self.session.refresh(category)
        return category

    async def get_all(self) -> list[Category]:
        raw_categories = await self.session.execute(select(Category))
        return list(raw_categories.scalars().fetchall())

    async def get_by_id(self, category_id: int) -> Category | None:
        result = await self.session.execute(select(Category).filter_by(id=category_id))
        return result.fetchone()

    async def get_subcategories_by_category_id(
        self,
        category_id: int,
    ) -> list[Subcategory]:
        raw_subcategories = await self.session.execute(
            select(Subcategory).filter_by(category_id=category_id),
        )
        return list(raw_subcategories.scalars().fetchall())

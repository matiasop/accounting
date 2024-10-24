from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from accounting.db.dependencies import get_db_session
from accounting.db.models.accounts import Account


class AccountDAO:
    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    async def create(self, name: str, type: str, initial_amount: int) -> None:
        """Creates an account"""
        self.session.add(
            Account(name=name, type=type, initial_amount=initial_amount, total=0),
        )

    async def get_all(self) -> list[Account]:
        """Gets all accounts

        Returns:
            list[Account]: list of all accounts
        """
        raw_accounts = await self.session.execute(select(Account))
        return list(raw_accounts.scalars().fetchall())

    async def filter(self, name: str) -> list[Account]:
        """Get specific account based on its name

        Args:
            name (str): name of the account

        Returns:
            list[Account]: _description_
        """
        query = select(Account).where(Account.name == name)
        rows = await self.session.execute(query)
        return list(rows.scalars().fetchall())

    async def get_by_id(self, account_id: int) -> Account | None:
        result = await self.session.execute(select(Account).filter_by(id=account_id))
        return result.fetchone()

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql.sqltypes import DateTime, Integer, String

from accounting.db.base import Base


class Entry(Base):
    __tablename__ = "entry"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    description: Mapped[str] = mapped_column(String(length=200))
    datetime: Mapped[datetime] = mapped_column(DateTime)
    category: Mapped[str] = mapped_column(String(length=120))
    subcategory: Mapped[str] = mapped_column(String(length=200))
    type: Mapped[str] = mapped_column(String(length=120))
    amount: Mapped[int] = mapped_column(Integer)
    debit_account_id: Mapped[int] = mapped_column(ForeignKey("account.id"))
    debit_account: Mapped["Account"] = relationship(
        "Account",
        foreign_keys=[debit_account_id],
    )
    credit_account_id: Mapped[int] = mapped_column(ForeignKey("account.id"))
    credit_account: Mapped["Account"] = relationship(
        "Account",
        foreign_keys=[credit_account_id],
    )

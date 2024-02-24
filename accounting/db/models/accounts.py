from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import Integer, String

from accounting.db.base import Base


class Account(Base):
    __tablename__ = "account"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(length=200), unique=True)
    type: Mapped[str] = mapped_column(String(length=10))  # ASSET, LIABILITY, EQUITY
    initial_amount: Mapped[int] = mapped_column(Integer)
    total: Mapped[int] = mapped_column(Integer())

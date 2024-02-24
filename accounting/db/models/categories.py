from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql.sqltypes import String

from accounting.db.base import Base


class Category(Base):
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(length=200), unique=True)

    subcategories: Mapped[list["Category"]] = relationship(
        "Subcategory",
        back_populates="category",
    )

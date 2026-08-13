from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from ..database import Base

class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, unique=True, index=True)
    slug: Mapped[str | None] = mapped_column(String, unique=True, index=True)

    products = relationship("Product", back_populates="category")

    def __repr__(self):
        return f"<Category(id={self.id}, name='{self.name}')>"
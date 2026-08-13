from sqlalchemy import Integer, String, Text, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
from ..database import Base

class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, index=True)
    description: Mapped[str | None] = mapped_column(Text)
    price: Mapped[float] = mapped_column(Float)
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("categories.id"))
    image_url: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    category = relationship("Category", back_populates="products")

    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', price={self.price})>"
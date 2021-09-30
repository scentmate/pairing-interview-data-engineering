from sqlalchemy import Boolean, Column, Integer, String

from cms.src.infrastructure.orm.sqlalchemy import Base


class Fragrance(Base):
    __tablename__ = "fragrances"

    fragrance_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    cost = Column(Integer)
    forbidden = Column(Boolean, default=False)


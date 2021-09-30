from typing import Any, Dict

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base

Base: DeclarativeMeta = declarative_base()
metadata = Base.metadata


class Fragrance(Base):
    __tablename__ = "fragrances"

    extend_existing = True

    fragrance_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    description = Column(String)
    cost = Column(Integer)
    forbidden = Column(Boolean, default=False)

    def __jsonify__(self) -> Dict[str, Any]:
        return {
            "fragrance_id": self.fragrance_id,
            "name": self.name,
            "description": self.description,
            "cost": int(self.cost),
            "forbidden": self.forbidden
        }
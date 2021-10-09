from sqlalchemy import Column, Integer, String

from db.base import Base


class Story(Base):
    __tablename__ = "stories"

    id = Column(Integer, primary_key=True)

    next = Column(Integer, nullable=True)
    prev = Column(Integer, nullable=True)

    # next = relationship("Story", remote_side=["id"], backref="next_story")
    # prev = relationship("Story", remote_side=["id"], backref="prev_story")

    description = Column(String)

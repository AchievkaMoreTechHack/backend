from sqlalchemy import Column, Integer, String

from db.base import Base


class Story(Base):
    __tablename__ = "stories"

    id = Column(Integer, primary_key=True)
    next = Column(String, nullable=True)  # url
    prev = Column(String, nullable=True)  # url
    story = Column(String)  # list
    description = Column(String, nullable=True)
    description_preview = Column(String, nullable=True)
    action_type = Column(String, nullable=True)  # button/edittext/gender
    action_data = Column(String, nullable=True)  # list
    background = Column(String)  # url
    character = Column(String, nullable=True)  # url
    position = Column(String, nullable=True)  # center/side

import os
import sys
from datetime import datetime
sys.path.append('..')
from server.database import Base
from server.database import engine
from sqlalchemy import Column, String, DateTime, Text, Integer
from sqlalchemy.sql.functions import current_timestamp

SQLITE3_NAME = './db.sqlite3'

class Todo(Base):
    __tablename__ = 'todos'

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    text = Column(String(256))
    created_at = Column(
        DateTime,
        default=datetime.now(),
        nullable=False,
        server_default=current_timestamp()
    )
    updated_at = Column(
        DateTime,
        default=datetime.now(),
        nullable=True,
        onupdate=datetime.now()
    )

Base.metadata.create_all(engine)


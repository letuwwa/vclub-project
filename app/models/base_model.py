from datetime import datetime
import uuid as uuid_pkg
from sqlalchemy import Column, DateTime
from sqlmodel import SQLModel, Field


class Base(SQLModel):
    id: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True),
                         default=datetime.utcnow)
    )
    updated_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True),
                         onupdate=datetime.utcnow,
                         default=datetime.utcnow)
    )

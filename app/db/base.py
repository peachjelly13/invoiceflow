from datetime import datetime, timezone
from sqlalchemy import Column, DateTime, event
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
import uuid
from sqlalchemy.dialects.postgresql import UUID


class Base(DeclarativeBase):
    pass


class TimestampMixin:
    """Adds created_at and updated_at to any model automatically."""

    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )
    created_at._creation_order = 9998

    updated_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )
    updated_at._creation_order = 9999

    @staticmethod
    def _updated_at(mapper, connection, target):
        """Called automatically before every update."""
        target.updated_at = datetime.now(timezone.utc)

    @classmethod
    def __declare_last__(cls):
        """Registers the before_update event for this model."""
        event.listen(cls, "before_update", cls._updated_at)


class PrimaryKeyMixin:
    """Adds an auto-incrementing primary key to any model."""

    id:Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )
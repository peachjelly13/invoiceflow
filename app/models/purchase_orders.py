import uuid
import enum
from datetime import date

from sqlalchemy import String, Text, Integer, Numeric, Date, ForeignKey, Enum as SAEnum
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base, TimestampMixin, PrimaryKeyMixin


class POStatus(enum.Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    FULFILLED = "fulfilled"


class PurchaseOrder(Base, TimestampMixin, PrimaryKeyMixin):
    __tablename__ = "purchase_orders"
    po_number: Mapped[str] = mapped_column(
        String(1000),
        nullable=False,
        unique=True,
        index=True
    )
    description: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )
    quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )
    unit_price: Mapped[float] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )
    total_amount: Mapped[float] = mapped_column(
        Numeric(10, 3),
        nullable=False
    )
    purchase_date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )
    status: Mapped[POStatus] = mapped_column(
        SAEnum(POStatus),
        nullable=False,
        default=POStatus.PENDING
    )
    vendor_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("vendors.id"),
        nullable=False,
        index=True
    )
    


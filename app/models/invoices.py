import uuid
import enum
from datetime import datetime

from sqlalchemy import String, Text, Numeric, DateTime, ForeignKey, Enum as SAEnum, JSON
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base, TimestampMixin, PrimaryKeyMixin


class InvoiceStatus(enum.Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    APPROVED = "approved"
    REJECTED = "rejected"
    PAID = "paid"


class Invoice(Base, TimestampMixin, PrimaryKeyMixin):
    __tablename__ = "invoices"
    invoice_number: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True,
        index=True
    )
    amount: Mapped[float] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )
    invoice_date: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False
    )
    status: Mapped[InvoiceStatus] = mapped_column(
        SAEnum(InvoiceStatus),
        nullable=False,
        default=InvoiceStatus.PENDING
    )
    file_path: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )
    extracted_data: Mapped[dict] = mapped_column(
        JSON,
        nullable=True
    )
    rejection_reason: Mapped[str] = mapped_column(
        Text,
        nullable=True
    )
    vendor_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("vendors.id"),
        nullable=False,
        index=True
    )
    po_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("purchase_orders.id"),
        nullable=True,
        index=True
    )
    reviewed_by: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=True
    )
    reviewed_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=True
    )

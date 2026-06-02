import uuid
import enum

from sqlalchemy import String, Text, ForeignKey, Enum as SAEnum, JSON
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base, TimestampMixin, PrimaryKeyMixin


class AuditAction(enum.Enum):
    # Invoice actions
    INVOICE_CREATED = "invoice_created"
    INVOICE_APPROVED = "invoice_approved"
    INVOICE_REJECTED = "invoice_rejected"
    INVOICE_PAID = "invoice_paid"
    # PO actions
    PO_CREATED = "po_created"
    PO_APPROVED = "po_approved"
    PO_FULFILLED = "po_fulfilled"
    # Vendor actions
    VENDOR_CREATED = "vendor_created"
    VENDOR_DEACTIVATED = "vendor_deactivated"
    # User actions
    USER_LOGIN = "user_login"
    USER_CREATED = "user_created"


class AuditLog(Base, TimestampMixin, PrimaryKeyMixin):
    __tablename__ = "audit_logs"

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False,
        index=True
    )
    action: Mapped[AuditAction] = mapped_column(
        SAEnum(AuditAction),
        nullable=False,
        index=True
    )
    entity_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True
    )
    entity_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        nullable=False,
        index=True
    )
    old_data: Mapped[dict] = mapped_column(
        JSON,
        nullable=True
    )
    new_data: Mapped[dict] = mapped_column(
        JSON,
        nullable=True
    )
    ip_address: Mapped[str] = mapped_column(
        String(45),
        nullable=True
    )

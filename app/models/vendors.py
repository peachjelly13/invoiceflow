from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base,TimestampMixin,PrimaryKeyMixin
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import String, Boolean, Date, ForeignKey, Text, UniqueConstraint
from datetime import datetime,date


class Vendor(Base,TimestampMixin,PrimaryKeyMixin):
    __tablename__ = "vendors"
    name:Mapped[str] = mapped_column(
        String(255),
        nullable=False,  
    )
    email:Mapped[str] =mapped_column(
        String(255),
        nullable=False
    )
    phone:Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )
    address:Mapped[str]= mapped_column(
        Text,
        nullable=False
    )
    partnership_date:Mapped[date] = mapped_column(
        Date,
        nullable=False
    )
    is_active:Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )



class VendorUserMapping(Base, PrimaryKeyMixin, TimestampMixin):
    __tablename__ = "vendor_user_mapping"
    __table_args__ = (
        UniqueConstraint("vendor_id", "user_id"),
    )

    vendor_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("vendors.id"),
        nullable=False,
        index=True
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False,
        index=True
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )


import uuid
from datetime import date
from app.models.vendors import Vendor, VendorUserMapping


def test_vendor_creation():
    vendor = Vendor(
        name="Test Vendor",
        email="test@vendor.com",
        phone="7718829766",
        address="123 Test Street, Test City, Test Country",
        partnership_date=date(2024, 1, 1),
        is_active=True
    )
    assert vendor.name == "Test Vendor"
    assert vendor.email == "test@vendor.com"
    assert vendor.phone == "7718829766"
    assert vendor.address == "123 Test Street, Test City, Test Country"
    assert vendor.partnership_date == date(2024, 1, 1)
    assert vendor.is_active == True


def test_vendor_user_mapping_creation():
    mapping = VendorUserMapping(
        vendor_id=uuid.uuid4(),
        user_id=uuid.uuid4(),
        is_active=True
    )
    assert mapping.vendor_id is not None
    assert mapping.user_id is not None
    assert mapping.is_active == True
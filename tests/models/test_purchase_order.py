import uuid
from app.models.purchase_orders import PurchaseOrder, POStatus
from datetime import date

def test_purchase_order_creation():
    po = PurchaseOrder(
        po_number = "PO123456",
        description = "Test Purchase Order",
        quantity = 10,
        unit_price = 99.99,
        total_amount = 999.90,
        purchase_date=date(2024, 1, 1),
        status = POStatus.PENDING,
        vendor_id = uuid.uuid4(),
        authorized_by = uuid.uuid4(),
    )
    assert po.po_number == "PO123456"
    assert po.description == "Test Purchase Order"
    assert po.quantity == 10
    assert po.unit_price == 99.99
    assert po.total_amount == 999.90
    assert po.purchase_date == date(2024, 1, 1)
    assert po.status == POStatus.PENDING
    assert po.vendor_id == po.vendor_id
    assert po.authorized_by == po.authorized_by

if __name__ == "__main__":
    test_purchase_order_creation()


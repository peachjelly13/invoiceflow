
from  app.models.invoices import Invoice,InvoiceStatus
import uuid
from datetime import datetime,date


def test_invoice():
    invoice = Invoice(
    invoice_number = "INV-001",
    amount = 1500.00,
    invoice_date = datetime(2024 , 1 ,1),
    status = "pending",
    file_path = "/path/to/invoice/INV-001.pdf",
    extracted_data = {"key": "value"},
    rejection_reason = None,
    vendor_id = uuid.uuid4(),
    po_id = uuid.uuid4(),
    reviewed_by = uuid.uuid4(),
    reviewed_at = datetime(2024,1,2)

    )
    assert invoice.invoice_number == "INV-001"
    assert invoice.amount == 1500.00
    assert invoice.invoice_date == datetime(2024 , 1 ,1)
    assert invoice.status == "pending"
    assert invoice.file_path == "/path/to/invoice/INV-001.pdf"
    assert invoice.extracted_data == {"key": "value"}
    assert invoice.rejection_reason == None
    assert invoice.vendor_id == invoice.vendor_id
    assert invoice.po_id == invoice.po_id
    assert invoice.reviewed_by == invoice.reviewed_by
    assert invoice.reviewed_at == datetime(2024, 1 , 2)

if __name__ == "__main__":
    test_invoice()




import uuid
from app.models.audit_logs import AuditLog, AuditAction


def test_audit_log_creation():
    log = AuditLog(
        user_id=uuid.uuid4(),
        action=AuditAction.INVOICE_APPROVED,
        entity_type="invoice",
        entity_id=uuid.uuid4(),
        old_data={"status": "pending"},
        new_data={"status": "approved"},
        ip_address="192.168.1.1"
    )
    assert log.action == AuditAction.INVOICE_APPROVED
    assert log.entity_type == "invoice"
    assert log.old_data == {"status": "pending"}
    assert log.new_data == {"status": "approved"}
    assert log.ip_address == "192.168.1.1"


def test_audit_actions():
    assert AuditAction.INVOICE_APPROVED.value == "invoice_approved"
    assert AuditAction.PO_CREATED.value == "po_created"
    assert AuditAction.USER_LOGIN.value == "user_login"


if __name__ == "__main__":
    test_audit_log_creation()
    test_audit_actions()


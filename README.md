# invoiceflow
A backend system that automates the entire accounts payable workflow for small-to-mid sized businesses using AI.

## Running Tests

Run specific test file:

Run all tests:
```bash
uv run pytest -v
```

```bash
uv run pytest tests/models/test_user.py -v
uv run pytest tests/models/test_vendor.py -v
uv run pytest tests/models/test_purchase_order.py -v
```




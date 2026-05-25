import uuid
from app.models.users import User,UserRole


#We created a user here this is a dummy user
def test_user_creation():
    user = User(
        email="test@gmail.com",
        hashed_password="hashedpassword",
        full_name="Test User",
        role=UserRole.ADMIN
    )
    assert user.email == "test@gmail.com"
    assert user.hashed_password == "hashedpassword"
    assert user.full_name == "Test User"
    assert user.role == UserRole.ADMIN
    print("Test User Created Successfully")

def test_user_roles():
    assert UserRole.ADMIN.value == "admin"
    assert UserRole.FINANCE_MANAGER.value == "finance_manager"
    assert UserRole.VENDOR.value == "vendor"
    print("Test User Roles Created Successfully")


if __name__ == "__main__":
    test_user_creation()
    test_user_roles()

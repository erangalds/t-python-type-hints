from typing import Optional

def get_user_email(user_id: int) -> Optional[str]:
    """
    Returns user email if found, otherwise None.
    """
    if user_id == 1:
        return "alice@example.com"
    return None

user_email = get_user_email(1)
if user_email: # Recommended way to check for None
    print(f"User email: {user_email.upper()}")
else:
    print("User not found.")

user_email_2 = get_user_email(2)
# mypy will warn if you try to call .upper() on user_email_2 directly
# without a None check, because it knows Optional[str] might be None.
#
# Run mypy again after uncommenting below
print(user_email_2.upper()) # Mypy error!


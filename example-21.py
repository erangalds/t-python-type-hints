from typing import NewType

UserId = NewType('UserId', int)
ProductId = NewType('ProductId', int)

def get_user_data(user_id: UserId) -> str:
    return f"Fetching data for user ID: {user_id}"

def get_product_info(product_id: ProductId) -> str:
    return f"Fetching info for product ID: {product_id}"

user_id_val = UserId(123)
product_id_val = ProductId(456)

print(get_user_data(user_id_val))
print(get_product_info(product_id_val))

# mypy will flag this, even though both are ints at runtime
# print(get_user_data(product_id_val)) # Mypy error!

# At runtime, NewType instances are just their underlying type:
print(type(user_id_val)) # Output: <class 'int'>


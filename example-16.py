from typing import Final

MAX_CONNECTIONS: Final[int] = 100
# Run this code twice with mypy by uncommenting the below line
#  
MAX_CONNECTIONS = 200 # Mypy error: Cannot assign to final name "MAX_CONNECTIONS"

class Config:
    DEBUG_MODE: Final[bool] = True

    def set_debug(self, value: bool) -> None:
        # self.DEBUG_MODE = value # Mypy error: Cannot assign to final attribute
        pass


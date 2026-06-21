from pydantic import BaseModel
from typing import List, Dict, Any
from backend.models.object.user import User

class SignUpDataResponse(BaseModel):
    success: bool
    message: str
    total_users: int
    users_data: List[User]
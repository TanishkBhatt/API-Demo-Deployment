from pydantic import BaseModel
from typing import List, Dict, Any

class HomeResponse(BaseModel):
    success: bool
    message: str
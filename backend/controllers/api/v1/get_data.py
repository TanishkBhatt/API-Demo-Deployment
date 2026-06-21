from fastapi import HTTPException, status
from typing import List, Dict, Any
from random import sample
from backend.utils.json_parser import json_parser, JSON_FILEPATH

def get_sign_up_data(limit: int) -> Dict[str, Any]:
    # Fetching JSON Data
    data: Dict[str, Any] = json_parser(JSON_FILEPATH)

    # Validating Is JSON Data Exists
    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cannot fetch users from the database"
        )
    
    # Extracting User SignUp Data
    users_data: List[Dict[str, Any]] = sample(data["data"], min(limit, len(data["data"])))

    # Return Object
    return {
        "success": True,
        "message": "Data Successfully Retreived",
        "total_users": len(users_data),
        "users_data": users_data
    }
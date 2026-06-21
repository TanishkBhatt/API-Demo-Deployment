from fastapi import APIRouter, status
from backend.models.home import HomeResponse

router = APIRouter()

@router.get(
    "/",
    response_model=HomeResponse,
    status_code=status.HTTP_200_OK
)

def main() -> dict:
    return {
        "success": True,
        "message": "Connection Succesful"
    }
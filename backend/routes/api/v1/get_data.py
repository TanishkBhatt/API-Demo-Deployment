from fastapi import APIRouter, status, Query
from backend.models.api.v1.get_data import SignUpDataResponse
from backend.controllers.api.v1.get_data import get_sign_up_data

router = APIRouter()

@router.get(
    "/sign-up-data",
    response_model=SignUpDataResponse,
    status_code=status.HTTP_200_OK
)

def main(limit: int = Query(10, ge=1)) -> dict:
    return get_sign_up_data(limit)
from fastapi import FastAPI
from backend.routes import home
from backend.routes.api.v1 import get_data

# Init App
app = FastAPI(
    title="API Demo Deployment",
    description="Demo SignUp Data Services for API Testing Purposes.",
    version="1.0"
)

# Including Routes
app.include_router(home.router)
app.include_router(get_data.router)
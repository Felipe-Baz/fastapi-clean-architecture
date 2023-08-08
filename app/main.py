from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.configs.Environment import get_environment_variables
from app.routers import user

# Application Environment Configuration
env = get_environment_variables()

# Core Application Instance
app = FastAPI(title=env.APP_NAME, version=env.API_VERSION)

origins = [
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add Routers
app.include_router(user.router, prefix="/v1", tags=["users"])


# Health
@app.get("/v1/health")
async def root():
    return {"version": env.API_VERSION}

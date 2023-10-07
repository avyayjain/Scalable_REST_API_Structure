# main.py
import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from API.resources.sign_up import add_user_router
from API.resources.web.v1.test_1 import test_v1_router
from API.resources.token import token_router
from web.v2.test_file_2 import test_v2_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(add_user_router, prefix="/api/user/sign-up")
app.include_router(token_router, prefix="/api/token")
app.include_router(test_v1_router, prefix="/api/v1/hello")
app.include_router(test_v2_router, prefix="/api/v2/hello")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

# include v1 router
# include v2 router

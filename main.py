from typing import Awaitable, Callable
import uuid
# from secure import SecureHeaders

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import Response

import config
# from logging import logger
from routers import Debug




app = FastAPI(
    title=config.PROJECT_TITLE,
    version=config.VERSION,
    root_path=config.ROOT_PATH,
    description=config.DESCRIPTION,
    docs_url='/docs',
    redoc_url='/redoc',
)

# app.include_router(default.router, tags=["Default Endpoints"]) 
app.include_router(Debug.router, tags=["Debugging Endpoints"])
# _secure_headers = SecureHeaders()

# assign request ids, standard logging / error handling
# @app.middleware("http")
# async def _request_middleware(request: Request, call_next: Callable[[Request], Awaitable[Response]]) -> Response:
#     request_id = str(uuid.uuid4())
#     with logger.contextualize(request_id=request_id):
#         logger.info("Request received")

#         try:
#             response = await call_next(request)
#             # add security headers
#             _secure_headers.starlette(response)

#         except Exception as ex:
#             logger.error(f"Request failed: {ex}")
#             print(f"Request failed: {ex}")
#             response = JSONResponse(content={"success": False}, status_code=500)

#         finally:
#             response.headers["X-Request-ID"] = request_id
#             logger.info("Request ended")
#             return response   
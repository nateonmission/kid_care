from loguru import logger

from fastapi import APIRouter, Depends, Path, Query, status
from fastapi.params import Body
from fastapi.responses import JSONResponse


from services.Debug import Debug


# Router
router = APIRouter()

@router.get("/debug")
def is_server_up(this_text: str = Query(default=None)) -> dict:    
    logger.info(f"this_text = {this_text}")
    logger.info("ROUTER: /debug, is_server_up")
    debug = Debug()
    return_item = debug.is_server_up(this_text)
    logger.info("ROUTER: returning")
    return return_item
    
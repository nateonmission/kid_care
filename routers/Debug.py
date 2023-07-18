from datetime import datetime

from fastapi import APIRouter, Depends, Path, Query, status
from fastapi.params import Body
from fastapi.responses import JSONResponse



# Router
router = APIRouter()


@router.get("/debug")
def is_server_up(this_text: str = Query(default=None)):
    now = datetime.now()
    if this_text:
        return {"Success": True, "DateTime": now, "Output Text": this_text}
    else:
        return {"Success": True, "DateTime": now, "Output Text": "NONE given"}

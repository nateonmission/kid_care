from datetime import datetime
from loguru import logger

class Debug:

    def is_server_up(self, this_text: str = None) -> dict:
        logger.info("SERVICE: is_server_up")
        now = datetime.now()
    
        if this_text:
            logger.info(f"SERVICE: Returning with text: '{this_text}'")
            return {"Success": True, "DateTime": now, "Output Text": this_text}
        else:
            logger.info(f"SERVICE: Returning without text")
            return {"Success": True, "DateTime": now, "Output Text": "NONE given"}
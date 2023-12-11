from fastapi import Depends, HTTPException, Header
from loguru import logger
from app.utils.config import settings


def get_session_code_header(x_session_code: str = Header(...)): 
    return x_session_code


async def get_session_code(session_code: str = Depends(get_session_code_header)):
    if verify_session_code(session_code):
        return session_code
    else:
        raise HTTPException(status_code=401, detail="Invalid session code")
    

def verify_session_code(session_code):
    codes=settings.SECURITY_CODE
    valid_session_codes = codes.split(",")
    logger.info(valid_session_codes)
    if session_code in valid_session_codes:
        return True
    else:
        return False



from fastapi import Header, HTTPException

from config import UTP_API_KEY



async def verify_api_key(
    x_api_key: str = Header(...)
):

    if x_api_key != UTP_API_KEY:

        raise HTTPException(
            status_code=401,
            detail="API Key non valida"
        )


    return True
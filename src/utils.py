from pexels_apis import PexelsAPI

from fastapi.security import APIKeyHeader
from fastapi import Depends,  HTTPException, status

header_scheme = APIKeyHeader(name="Authorization")

async def authenticate_user(apikey: str = Depends(header_scheme)):
    if not apikey:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    pexels = PexelsAPI(apikey=apikey)
    return {"pexels": pexels}

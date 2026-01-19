from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.core.security import verify_access_token

bearer_scheme = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Security(bearer_scheme)):
    token = credentials.credentials
    user_id = verify_access_token(token)  # Must be string, matches owner_id
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return user_id

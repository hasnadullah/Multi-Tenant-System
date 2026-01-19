from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.core.security import verify_access_token

bearer_scheme = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Security(bearer_scheme)):
    payload = verify_access_token(credentials.credentials)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")

    return {
        "user_id": payload["user_id"],
        "tenant_id": payload["tenant_id"],
        "role": payload["role"]
    }

from fastapi import HTTPException

def require_roles(allowed: list, role: str):
    if role not in allowed:
        raise HTTPException(status_code=403, detail="Permission denied")

from fastapi import APIRouter
from pydantic import BaseModel
router = APIRouter(prefix="/auth", tags=["Authentication"])
class UserRequest(BaseModel):
    username: str
    password: str
@router.post("/register")
def register(request: UserRequest):
    return {
        "success": True,
        "message": f"User {request.username} registered successfully."
    }
@router.post("/login")
def login(request: UserRequest):
    return {
        "success": True,
        "message": f"User {request.username} logged in successfully."
    }
@router.post("/logout")
def logout():
    return {"success": True, "message": "User logged out successfully."}
@router.get("/session-info")
def session_info():
    return {"logged_in": False, "message": "No active session."}

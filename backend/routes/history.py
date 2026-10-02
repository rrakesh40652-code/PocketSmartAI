from fastapi import APIRouter
router = APIRouter(prefix="/history", tags=["History"])
@router.get("")
def get_history():
    return {
        "success": True,
        "history": []
    }

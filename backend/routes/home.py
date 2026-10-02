from fastapi import APIRouter, Form
from services.gemini_utils import generate_text
router = APIRouter(prefix="/generate-home", tags=["Home Planner"])
@router.post("")
def generate_home(
    budget: float = Form(...),
    room_type: str = Form(...),
    quantity: int = Form(...)
):
    prompt = f"""You are a home interior recommendation assistant.
Budget: ?{budget}
Room type: {room_type}
Quantity: {quantity}
Suggest suitable home interior products within the budget.
Give product category, approximate price and suitable platform
such as IKEA or Amazon."""
    result = generate_text(prompt)
    return {
        "success": True,
        "recommendations": result
    }

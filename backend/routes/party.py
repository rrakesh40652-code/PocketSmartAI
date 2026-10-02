from fastapi import APIRouter, Form
from services.gemini_utils import generate_text
router = APIRouter(prefix="/generate-party", tags=["Party Planner"])
@router.post("")
def generate_party(
    budget: float = Form(...),
    guests: int = Form(...),
    event_type: str = Form(...),
    venue: str = Form("")
):
    prompt = f"""
You are a party planning recommendation assistant.
Budget: Rs.{budget}
Number of guests: {guests}
Event type: {event_type}
Venue: {venue or "Not specified"}
Give a SHORT recommendation.
List 4 suitable party items or services with approximate prices.
Keep the total within the given budget.
Do not give long explanations.
"""
    result = generate_text(prompt)
    return {
        "success": True,
        "recommendations": result
    }

from fastapi import APIRouter, Form
from services.gemini_utils import generate_text
router = APIRouter(prefix="/generate-jewelry", tags=["Jewelry Planner"])
@router.post("")
def generate_jewelry(
    budget: float = Form(...),
    occasion: str = Form(...),
    style: str = Form(...)
):
    prompt = f"""You are a jewelry recommendation assistant.
Budget: ?{budget}
Occasion: {occasion}
Style: {style}
Suggest suitable jewelry options within the budget.
Mention approximate price and suitable shopping platforms
such as Amazon or Flipkart."""
    result = generate_text(prompt)
    return {
        "success": True,
        "recommendations": result
    }

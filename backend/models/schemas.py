from pydantic import BaseModel
from typing import Optional
class HomeRequest(BaseModel):
    budget: float
    room_type: str
    quantity: int = 1
class PartyRequest(BaseModel):
    budget: float
    guests: int
    event_type: str
    venue: Optional[str] = None
class JewelryRequest(BaseModel):
    budget: float
    occasion: str
    style: str

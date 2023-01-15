from typing import Optional
from pydantic import BaseModel, Field

class Item(BaseModel):
    name: str = Field(None, title='Item ...', min_length=3, max_length=11)
    price: float = Field(None, title='Price 300')
    is_offer: Optional[bool] = Field(False, title='Is Offer')
from datetime import time, date

from pydantic import BaseModel

class BookBase(BaseModel):
    product_id: int
    date: date
    time: time

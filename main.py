from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
    title: str
    author: str
    price: float
    bsr: int
    est_sales: int
    est_revenue: float
    reviews: int
    rating: float
    pub_date: str
    category: str
    subcategory: str

books_db: List[Book] = [
    Book(
        title="The Dopamine Detox Plan",
        author="John Smith",
        price=9.99,
        bsr=4200,
        est_sales=1000,
        est_revenue=6993.0,
        reviews=87,
        rating=4.6,
        pub_date="2023-06-12",
        category="Health & Fitness",
        subcategory="Mental Health"
    )
]

@app.get("/books", response_model=List[Book])
def get_books():
    return books_db

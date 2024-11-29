__all__ = (
    "User",
    "Author",
    "Product",
    "ProductDate",
    "ProductTime",
    "Book",
)

from core.config import settings

from .users.models import User
from .authors.models import Author
from .products.products import Product
from .products.product_dates import ProductDate
from .products.product_times import ProductTime
from .books.models.books import Book
from .authors.author_table import AuthorTable
from .authors.author_table_date import AuthorTableDate

from .users.views import router as users_router
from .authors.views import router as authors_router
from .products.views import router as products_router
from .books.views import router as books_router

from fastapi import APIRouter

router = APIRouter(
    prefix=settings.api.prefix
)

router.include_router(users_router)
router.include_router(authors_router)
router.include_router(products_router)
router.include_router(books_router)

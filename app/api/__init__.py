__all__ = (
    "User",
    "Author",
    "Product"
)

from core.config import settings

from .users.models import User
from .authors.models import Author
from .products.models import Product

from .users.views import router as users_router
from .authors.views import router as authors_router
from .products.views import router as products_router

from fastapi import APIRouter

router = APIRouter(
    prefix=settings.api.prefix
)

router.include_router(users_router)
router.include_router(authors_router)
router.include_router(products_router)

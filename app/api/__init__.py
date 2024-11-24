__all__ = (
    "User",
    "Author",
    "Product"
)

from .users.models import User
from .authors.models import Author
from .products.models import Product


from core.config import settings

from .users.views import router as users_router
from .authors.views import router as authors_router

from fastapi import APIRouter

router = APIRouter(
    prefix=settings.api.prefix
)

router.include_router(users_router)
router.include_router(authors_router)
from rest_framework.routers import DefaultRouter
from app.views import GrammerViews

router = DefaultRouter()
router.register(r"Grammer", GrammerViews, basename="Grammer")

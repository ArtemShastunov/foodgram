from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import (
    avatar,
    IngredientViewSet,
    RecipeViewSet,
    SubscriptionViewSet,
    TagViewSet
)

router = DefaultRouter()
router.register('tags', TagViewSet)
router.register('ingredients', IngredientViewSet)
router.register('recipes', RecipeViewSet)
router.register(
    'users/subscriptions',
    SubscriptionViewSet,
    basename='subscriptions'
)

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('users/me/avatar/', avatar),
]

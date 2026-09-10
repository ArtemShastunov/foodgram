from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import (
    avatar,
    IngredientViewSet,
    RecipeViewSet,
    SubscriptionViewSet,
    TagViewSet,
    UserViewSet
)

router = DefaultRouter()
router.register('tags', TagViewSet)
router.register('ingredients', IngredientViewSet)
router.register('recipes', RecipeViewSet)
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path(
        'users/subscriptions/',
        SubscriptionViewSet.as_view({'get': 'list'}),
        name='subscriptions'
    ),
    path(
        'users/<int:pk>/subscribe/',
        SubscriptionViewSet.as_view({'post': 'subscribe', 'delete': 'subscribe'}),
        name='subscribe'
    ),
    path('users/me/avatar/', avatar),
    path('', include(router.urls)),
    path('', include('djoser.urls')),
]

from rest_framework.routers import DefaultRouter
from api.views import UsersApiViewSet
from django.urls import path, include

user_list = UsersApiViewSet.as_view({'get': 'list'})
user_detail = UsersApiViewSet.as_view({'get': 'retrieve'})
router = DefaultRouter()
router.register(r'persona', UsersApiViewSet, basename='persona')
urlpatterns = [
    path('', include(router.urls)),
]

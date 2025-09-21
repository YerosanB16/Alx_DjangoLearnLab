from django.urls import path, include
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)  # this is your Task 2 ViewSet

urlpatterns = [
    path('booklist/', BookList.as_view(), name='book-list'),  # Task 1 endpoint
    path('', include(router.urls)),  # Task 2 endpoints
]


from rest_framework.authtoken.views import obtain_auth_token

urlpatterns += [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Task 3
]

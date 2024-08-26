from django.urls import path, include
from .views import home
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, CategoryViewSet, BookViewSet, MemberViewSet, LoanViewSet

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'books', BookViewSet)
router.register(r'members', MemberViewSet)
router.register(r'loans', LoanViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('', include(router.urls)),
]

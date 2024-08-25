from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Author, Category, Book, Member, Loan
from .serializers import AuthorSerializer, CategorySerializer, BookSerializer, MemberSerializer, LoanSerializer

def home(request):
    return HttpResponse("Welcome to the Library Management System!")

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

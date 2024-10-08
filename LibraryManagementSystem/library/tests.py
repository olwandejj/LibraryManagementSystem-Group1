from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Author, Category, Book, Member, Loan
from django.contrib.auth.models import User
from datetime import date

class AuthorAPITests(APITestCase):

    def setUp(self):
        self.author = Author.objects.create(name="J.K. Rowling", biography="Author of the Harry Potter series.")
        self.url = reverse('author-list')

    def test_get_all_authors(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_author(self):
        data = {"name": "George Orwell", "biography": "Author of 1984."}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_author(self):
        url = reverse('author-detail', args=[self.author.id])
        data = {"name": "J.K. Rowling", "biography": "British author, best known for the Harry Potter series."}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_author(self):
        url = reverse('author-detail', args=[self.author.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CategoryAPITests(APITestCase):

    def setUp(self):
        self.category = Category.objects.create(name="Fantasy")
        self.url = reverse('category-list')

    def test_get_all_categories(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_category(self):
        data = {"name": "Science Fiction"}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_category(self):
        url = reverse('category-detail', args=[self.category.id])
        data = {"name": "Sci-Fi"}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_category(self):
        url = reverse('category-detail', args=[self.category.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class BookAPITests(APITestCase):

    def setUp(self):
        self.author = Author.objects.create(name="J.K. Rowling", biography="Author of the Harry Potter series.")
        self.category = Category.objects.create(name="Fantasy")
        self.book = Book.objects.create(title="Harry Potter", description="A young boy discovers he is a wizard.", author=self.author, category=self.category, isbn="1234567890", copies_available=5)
        self.url = reverse('book-list')

    def test_get_all_books(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book(self):
        data = {
            "title": "1984",
            "description": "A dystopian novel.",
            "author": self.author.id,
            "category": self.category.id,
            "isbn": "1234567890123",
            "copies_available": 5
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_update_book(self):
        url = reverse('book-detail', args=[self.book.id])
        data = {
            "title": "Harry Potter",
            "description": "A young boy discovers he is a wizard. Revised edition.",
            "author": self.author.id,
            "category": self.category.id,
            "isbn": "1234567890123",
            "copies_available": 10
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_delete_book(self):
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class MemberAPITests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.member = Member.objects.create(user=self.user, address="123 Library Lane")
        self.url = reverse('member-list')

    def test_get_all_members(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_member(self):
        new_user = User.objects.create_user(username='newuser', password='12345')
        data = {"user": new_user.id, "address": "456 Book Blvd"}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)    
        self.assertEqual(Member.objects.count(), 2)
        self.assertEqual(Member.objects.get(user=new_user).address, "456 Book Blvd")

    def test_update_member(self):
        url = reverse('member-detail', args=[self.member.id])
        data = {"user": self.user.id, "address": "789 Fiction Road"}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.member.refresh_from_db()
        self.assertEqual(self.member.address, "789 Fiction Road")

    def test_delete_member(self):
        url = reverse('member-detail', args=[self.member.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Member.objects.count(), 0)


class LoanAPITests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.member = Member.objects.create(user=self.user, address="123 Library Lane")
        self.author = Author.objects.create(name="J.K. Rowling", biography="Author of the Harry Potter series.")
        self.category = Category.objects.create(name="Fantasy")
        self.book = Book.objects.create(title="Harry Potter", description="A young boy discovers he is a wizard.", author=self.author, category=self.category, isbn="1234567890123", copies_available=5)
        self.loan = Loan.objects.create(member=self.member, book=self.book)
        self.url = reverse('loan-list')

    def test_get_all_loans(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_loan(self):
        data = {
            "book": self.book.id,
            "member": self.member.id,
            "return_date": "2024-09-26"
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Loan.objects.get(id=response.data['id']).return_date, date(2024, 9, 26))

    def test_update_loan(self):
        url = reverse('loan-detail', args=[self.loan.id])
        data = {
            "book": self.loan.book.id,
            "member": self.loan.member.id,
            "return_date": "2024-09-01"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.loan.refresh_from_db()
        self.assertEqual(self.loan.return_date, date(2024, 9, 1))

    def test_delete_loan(self):
        url = reverse('loan-detail', args=[self.loan.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Loan.objects.count(), 0)

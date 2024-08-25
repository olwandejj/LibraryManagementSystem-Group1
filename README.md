# Library Management System

## Group Members
- 150768
- 152955
- 151353
- 149008
- 124020
- 081000

## Project Overview
This project is a Library Management System built using Django and Django REST Framework (DRF). The system allows users to manage authors, categories, books, members, and loans. It provides a RESTful API that supports full CRUD (Create, Read, Update, Delete) operations.

## Models and Their Relationships

### 1. Author
- **Fields:** `name`, `biography`
- **Relationships:**
  - One-to-Many: An author can write many books, but each book has only one author.

### 2. Category
- **Fields:** `name`
- **Relationships:**
  - One-to-Many: A category can include many books, but each book belongs to only one category.

### 3. Book
- **Fields:** `title`, `description`, `isbn`, `copies_available`
- **Relationships:**
  - ForeignKey to Author: Indicates the author of the book.
  - ForeignKey to Category: Indicates the category of the book.

### 4. Member
- **Fields:** `user`, `address`
- **Relationships:**
  - One-to-Many: A member can have many loans, but each loan is associated with one member.

### 5. Loan
- **Fields:** `loan_date`, `return_date`
- **Relationships:**
  - ForeignKey to Member: Indicates the member who borrowed the book.
  - ForeignKey to Book: Indicates the book that was borrowed.

**Model Relationships Summary:**
- Author has a one-to-many relationship with Book.
- Category has a one-to-many relationship with Book.
- Member has a one-to-many relationship with Loan.
- Book has a one-to-many relationship with Loan.

## Views/ViewSets and Their Roles

### 1. AuthorViewSet
- Handles all CRUD operations for the Author model.
- Supports listing all authors, retrieving a single author, creating a new author, updating an existing author, and deleting an author.

### 2. CategoryViewSet
- Manages CRUD operations for the Category model.
- Provides endpoints for listing categories, creating, updating, retrieving, and deleting a category.

### 3. BookViewSet
- Manages CRUD operations for the Book model.
- Provides endpoints for managing the library's book inventory, including adding, updating, and deleting books.

### 4. MemberViewSet
- Handles CRUD operations for the Member model.
- Allows for the creation, retrieval, updating, and deletion of library members.

### 5. LoanViewSet
- Manages loan transactions between members and books.
- Supports creating a loan, retrieving loans, updating loan details (e.g., return date), and deleting a loan.

**General Role of ViewSets:**
Each ViewSet encapsulates all the logic for managing a particular model. They leverage Django REST Framework's `ModelViewSet`, which provides default implementations for CRUD operations.

## Serializers and Validation Rules

### 1. AuthorSerializer
- Serializes the Author model to JSON and handles deserialization.
- **Validation:** Ensures that the name field is not empty.

### 2. CategorySerializer
- Serializes the Category model.
- **Validation:** Ensures that the name field is unique.

### 3. BookSerializer
- Serializes the Book model, including nested representations for Author and Category.
- **Validation:** Ensures that the isbn field is unique and that copies_available is a positive integer.

### 4. MemberSerializer
- Serializes the Member model, including the User model.
- **Validation:** Ensures that the address field is not empty.

### 5. LoanSerializer
- Serializes the Loan model, including nested Member and Book representations.
- **Validation:** Validates that the loan_date is before the return_date if a return date is provided.

**Overview of Validation:**
Validation is implemented within the serializers to ensure that the data meets the expected criteria before it's processed by the views or saved to the database.

## URL Patterns and Their Purpose

### Project-level `urls.py`
- The main entry point for the application's URLs.
- Routes `/admin/` to the Django admin interface.
- Includes all API routes from the library app under the `/api/` path.

### App-level `urls.py`
- Defines the routing for the library app.
- Uses Django REST Framework's `DefaultRouter` to automatically generate routes for the ViewSets.

**Purpose of URL Patterns:**
- **Admin:** Manages the application through Django's built-in admin interface.
- **API:** Provides RESTful access to the models, allowing CRUD operations via HTTP methods.

## Test Case Summary for Library API
This document outlines the test cases implemented for the Library API. These tests utilize the Django REST framework's testing utilities (`rest_framework.test`).

### Models Covered
- Author
- Category
- Book
- Member
- Loan

### Test Cases

#### AuthorAPITests
- **test_get_all_authors:** Retrieves all authors successfully (expected status code: 200 OK)
- **test_create_author:** Creates a new author successfully (expected status code: 201 CREATED)
- **test_update_author:** Updates an existing author successfully (expected status code: 200 OK)
- **test_delete_author:** Deletes an author successfully (expected status code: 204 NO CONTENT)

#### CategoryAPITests
- **test_get_all_categories:** Retrieves all categories successfully (expected status code: 200 OK)
- **test_create_category:** Creates a new category successfully (expected status code: 201 CREATED)
- **test_update_category:** Updates an existing category successfully (expected status code: 200 OK)
- **test_delete_category:** Deletes a category successfully (expected status code: 204 NO CONTENT)

#### BookAPITests
- **test_get_all_books:** Retrieves all books successfully (expected status code: 200 OK)
- **test_create_book:** Creates a new book successfully (expected status code: 201 CREATED)
- **test_update_book:** Updates an existing book successfully (expected status code: 200 OK)
- **test_delete_book:** Deletes a book successfully (expected status code: 204 NO CONTENT)

#### MemberAPITests
- **test_get_all_members:** Retrieves all members successfully (expected status code: 200 OK)
- **test_create_member:** Creates a new member successfully (expected status code: 201 CREATED)
- **test_update_member:** Updates an existing member successfully (expected status code: 200 OK)
- **test_delete_member:** Deletes a member successfully (expected status code: 204 NO CONTENT)

#### LoanAPITests
- **test_get_all_loans:** Retrieves all loans successfully (expected status code: 200 OK)
- **test_create_loan:** Creates a new loan successfully (expected status code: 201 CREATED)
- **test_update_loan:** Updates an existing loan successfully (expected status code: 200 OK)
- **test_delete_loan:** Deletes a loan successfully (expected status code: 204 NO CONTENT)

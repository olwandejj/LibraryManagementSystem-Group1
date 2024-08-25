from rest_framework import serializers
from .models import Author, Category, Book, Member, Loan

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_isbn(self, value):
        if len(value) != 13:
            raise serializers.ValidationError("ISBN must be 13 characters long.")
        return value

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'

    def validate(self, data):
        loan_date = data.get('loan_date', None)
        if loan_date is None:
            loan_date = self.instance.loan_date if self.instance else None

        return_date = data.get('return_date', None)
        if return_date and loan_date and return_date < loan_date:
            raise serializers.ValidationError("Return date cannot be before the loan date.")
        return data

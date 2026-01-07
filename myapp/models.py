from django.db import models
from django.core.validators import MinLengthValidator,RegexValidator
class User(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100)
    email=models.EmailField(blank=False,unique=True)
    phone_number = models.CharField(
    max_length=10,
    validators=[
        MinLengthValidator(10, message="Phone number must be 10 digits"),
        RegexValidator(r'^\d{10}$', message="Phone number must contain only digits")
    ]
)
    password=models.CharField(max_length=100,blank=False)
    def __str__(self):
        return self.username
class Blog(models.Model):
    title=models.TextField(max_length=200)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField(max_length=500)
    created_at=models.DateTimeField(auto_now_add=True)
    edited_at=models.DateTimeField(auto_now=True)
    location=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.title
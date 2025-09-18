from django.db import models
from django.core.validators import MinLengthValidator

class Tag(models.Model):
    caption=models.CharField(max_length=20)

    def __str__(self):
        return self.caption

class Author(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email_address=models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name()
# Create your models here.
class posts(models.Model):
    title=models.CharField(max_length=50)
    image=models.ImageField(upload_to="posts",null=True)
    excerpt=models.CharField(max_length=250)
    date=models.DateField(auto_now=True)
    slug=models.SlugField(unique=True,db_index=True)
    content=models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)
    tags=models.ManyToManyField(Tag)
     

    def __str__(self):
         return self.title
class Comment(models.Model):
    user_name=models.CharField(max_length=120)
    user_email=models.EmailField()
    text=models.TextField(max_length=400)
    post=models.ForeignKey(posts,on_delete=models.CASCADE,related_name="comments")

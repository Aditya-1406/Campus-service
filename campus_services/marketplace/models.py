from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.


class Skill(models.Model):
    name = models.CharField(max_length=100,unique=True,case_sensitive=False)
    
    def __str__(self):
        return self.name
    
class User(AbstractUser):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    username = models.CharField(max_length=150,unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10,blank=True,null=True)
    college = models.CharField(max_length=100,blank=True,null=True)
    bio = models.TextField(blank=True,null=True)
    profile_picture = models.ImageField(upload_to='profiles/',blank=True,null=True)
    skills = models.ManyToManyField(Skill,blank=True)
    rating_avg = models.FloatField(default=0)
    total_reviews = models.IntegerField(default=0)
    tasks_completed = models.IntegerField(default=0)
    tasks_posted = models.IntegerField(default=0)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.username
    

class Task(models.Model):
    STATUS_CHOICES = [
        ('OPEN','Open'),
        ('IN_PROGRESS','In Progress'),
        ('COMPLETED','Completed'),
        ('CANCELLED','Cancelled'),
    ]
    
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    services = models.ForeignKey(Skill,on_delete=models.CASCADE,related_name='tasks')
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='tasks_created')
    budget_min = models.DecimalField(max_digits=10,decimal_places=2)
    budget_max = models.DecimalField(max_digits=10,decimal_places=2)
    location = models.CharField(max_length=255)
    deadline = models.DateTimeField()
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='OPEN')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    

class Bid(models.Model):
    STATUS_CHOICES = [
        ('PENDING','Pending'),
        ('ACCEPTED','Accepted'),
        ('REJECTED','Rejected'),
    ]
    
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    task =models.ForeignKey(Task,on_delete=models.CASCADE,related_name='bids')
    bidder = models.ForeignKey(User,on_delete=models.CASCADE,related_name='bids_made')
    price = models.DecimalField(max_digits=10,decimal_places=2)
    estimated_time = models.CharField(max_length=100)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('task','bidder')
    
    def __str__(self):
        return f"{self.bidder.username} - {self.task.title}"
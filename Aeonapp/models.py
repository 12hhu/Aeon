from django.db import models
class WorkshopDetail(models.Model):
    id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=20)
    description=models.CharField(max_length=800)
    is_active=models.BooleanField(default=True)

class WorkshopFormDetails(models.Model):
    username=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    profession=models.CharField(max_length=25)
    institute=models.CharField(max_length=60)
    state=models.CharField(max_length=25)
    queries=models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
class PublicationPaper(models.Model):
    year = models.IntegerField()
    title = models.CharField(max_length=255)
    authors = models.CharField(max_length=255)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.year} - {self.title}"
# Create your models here.
class PublicationFormDetail(models.Model):
    username=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    profession=models.CharField(max_length=25)
    institute=models.CharField(max_length=60)
    state=models.CharField(max_length=25)
    queries=models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
class ManuscriptFormDetail(models.Model):
    username=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    profession=models.CharField(max_length=25)
    institute=models.CharField(max_length=60)
    state=models.CharField(max_length=25)
    queries=models.CharField(max_length=100)

    def __str__(self):
        return self.username
    


class ContactusFormDetails(models.Model):
    username=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    profession=models.CharField(max_length=25)
    institute=models.CharField(max_length=60)
    state=models.CharField(max_length=25)
    queries=models.CharField(max_length=100)

    def __str__(self):
        return self.username
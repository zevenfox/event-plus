from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Venue(models.Model):
    name = models.CharField("Venue Name",max_length=100)
    address = models.CharField(max_length=100)
    zip_code = models.CharField('Zip code',max_length=100)
    phone = models.CharField('Contract',max_length=100)
    website = models.URLField('Web address',max_length=100)
    email_address = models.EmailField('Email',max_length=100)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField('Event Name',max_length=100)
    event_date = models.DateTimeField('Event date')
    vanues = models.ForeignKey(Venue, max_length=100, blank=True,on_delete=models.CASCADE)
    manager = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=100, null=True, blank=True)
    attendees = models.ManyToManyField(User, blank=True)

def __str__(self):
    return self.name
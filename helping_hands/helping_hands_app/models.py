from __future__ import unicode_literals
import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, UserManager, BaseUserManager

class Event(models.Model):
    event_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.event_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    event = models.ForeignKey(Event)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __unicode__(self):
	return self.choice_text



class ITUUserManager(BaseUserManager):
    def create_user(self,
                        email,
                        username,
                        first_name,
                        last_name,
                        security_question,
                        security_answer,
                        gender,
                        phone_number,
                        password=None):

        user = self.model(  email=email,
                            username=username,
                            first_name=first_name,
                            last_name=last_name,
                            security_question=security_question,
                            security_answer=security_answer,
                            gender=gender,
                            phone_number=phone_number,
                            password=password)
        return user

    def create_superuser(self, email, first_name,
                         password):
        user = self.create_user(email, first_name, 
                                password=password)        
        user.save()
        return user

class NGOUserManager(BaseUserManager):
    def create_user(self, email, ngo_website, 
                    password=None):
        user = self.model(email=email, 
                          ngo_website=ngo_website)        
        return user

    def create_superuser(self, email, ngo_website,
                         password):
        user = self.create_user(email,
                                 ngo_website, 
                                password=password)        
        user.save()
        return user


class ITUUser(AbstractBaseUser):    
    username = models.CharField(max_length=254, unique=True, primary_key=True, default='')    
    email = models.EmailField(blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)    
    security_question =  models.CharField(max_length=30, blank=True)
    security_answer = models.CharField(max_length=30, blank=True)
    gender = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.IntegerField()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = ITUUserManager()


class NGOUser(AbstractBaseUser):
    # user = models.OneToOneField(User)    
    ngo_website = models.CharField(max_length=100)
    security_answer = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    objects =  UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'ngo_website']
    objects = NGOUserManager()



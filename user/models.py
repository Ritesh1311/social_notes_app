from django.db import models

# Create your models here.

class userReg(models.Model):
    name=models.CharField(max_length=100)
    contact_number=models.IntegerField()
    password=models.CharField(max_length=255)
    status=models.BooleanField(default=True)

class notesCreation(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=255)
    created_by=models.ForeignKey(userReg,on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

class sharedWith(models.Model):
    notes_id=models.ForeignKey(notesCreation,on_delete=models.CASCADE)
    shared_with=models.ForeignKey(userReg,on_delete=models.CASCADE)
    view_access=models.BooleanField(default=True)
    edit_access=models.BooleanField(default=True)


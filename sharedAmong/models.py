from django.db import models

# Create your models here.
class sharedWith(models.Model):
    notes_id=models.ForeignKey(notesCreation,on_delete=models.CASCADE)
    shared_with=models.ForeignKey(userReg,on_delete=models.CASCADE)
    view_access=models.BooleanField(default=True)
    edit_access=models.BooleanField(default=True)
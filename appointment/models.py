from django.db import models
from django.contrib.auth.models import User

class Appointment(models.Model):
    
    time = models.TimeField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_confirmed = models.BooleanField(default=False)
    petOwner = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )
    
    def __str__(self):
        strDate = str(self.date)
        strTime = str(self.time)
        nameItself = strDate + ' | ' + strTime+'h'
        return nameItself
    

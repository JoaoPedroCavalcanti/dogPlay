from django.db import models

class Appointment(models.Model):
    
    def __str__(self):
        strDate = str(self.date)
        strTime = str(self.time)
        nameItself = strDate + ' | ' + strTime+'h'
        return nameItself
    
    time = models.TimeField()
    date = models.DateField()

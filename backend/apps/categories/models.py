from django.db import models

# Create your models here.
class Categories(models.Model):
    class Meta(object):
        db_table='categories'
    name = models.CharField(
        "Name", blank = False, null = False, max_length = 50
    )
    created_at = models.DateTimeField(
        "Created Date", blank= True, auto_now_add = True
    )
    updated_at = models.DateTimeField(
        "Update DateTime", blank = True, auto_now= True
    )
    
    def __str__(self):
        return self.name
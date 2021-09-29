from django.db import models
import uuid

class feedback(models.Model):
    Name        = models.CharField(max_length = 30)
    Email       = models.CharField(max_length= 50)
    Feedback    = models.TextField(null = False, blank = False)
    Created     = models.DateTimeField(auto_now_add = True)
    UUID        = models.UUIDField(default = uuid.uuid4,
                               unique = True,
                               primary_key = True,
                               editable = False
                               )

    def __str__(self):
        return str(self.Name)

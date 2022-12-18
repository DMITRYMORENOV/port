from django.db import models

class CheckBox(models.Model):
    name = models.CharField(max_length=150)
    is_checked = models.BooleanField(default=False)

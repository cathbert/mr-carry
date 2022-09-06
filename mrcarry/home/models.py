from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import random
import string
letter = random.choice([i for i in string.ascii_uppercase])
def create_new_ref_letter():
      return str(random.choice([i for i in string.ascii_uppercase]))
def create_new_ref_number():
      return str(random.randint(0000000000, 9999999999))
# Create your models here.
class Load(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    pick_up_location = models.CharField(max_length=255)
    drop_off_location = models.CharField(max_length=255)
    pick_up_date = models.DateField(editable=True, default=timezone.now, null=True)
    drop_off_date = models.DateField(editable=True, default=timezone.now, null=True)
    pick_up_time = models.TimeField()
    load_number = models.CharField(max_length=100, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.load_number:
            self.load_number = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
        super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f"{self.customer} - {self.load_number}" 
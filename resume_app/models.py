from django.db import models
from django.conf import settings

class Resume_home_data(models.Model):
    thumbnail=models.ImageField(upload_to="thumbnail/")
    serial_no=models.IntegerField()

    def __str__(self):
        return str(self.serial_no)

class Resume_template_data(models.Model):
    attach_pin=models.ForeignKey(Resume_home_data,on_delete=models.CASCADE,related_name="resume_pin")
    title=models.CharField(max_length=35)
    info=models.TextField(max_length=255)
    large_image=models.ImageField(upload_to='large_image/')



from django.db import models
import uuid
import os

def unique_file_path(instance, filename):
    ext = filename.split('.')[-1]
    unique_name = f"{uuid.uuid4()}.{ext}"
    return os.path.join('media', unique_name)

class Teacher(models.Model):
    CATEGORY_CHOICES = (
        ('Oliy', 'Oliy'),
        ('Birinchi', 'Birinchi'),
        ('Ikkinchi', 'Ikkinchi'),
    )

    SUBJECT_CHOICES = (
        ('math', 'Matematika'),
        ('physics', 'Fizika'),
        ('chemistry', 'Himiya'),
        ('biology','Biologiya'),
        ('history', 'Tarix'),
    )

    name = models.CharField(max_length=255, verbose_name="Ism Familiyasi")
    birth_year = models.IntegerField(verbose_name="Tug'ilgan yili")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Oliy', verbose_name="Toifasi")
    category_certificate = models.FileField(upload_to=unique_file_path, null=True, blank=True, verbose_name="Toifa sertifikati")
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES, verbose_name="Dars beradigan fani", default='Matematika')
    image = models.ImageField(upload_to=unique_file_path, null=True, blank=True, verbose_name="Rasm")
    additional_info = models.TextField(blank=True, verbose_name="Qo'shimcha ma'lumotlar")

    def __str__(self):
        return self.name
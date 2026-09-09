from django.db import models

# Create your models here.
class Patient(models.Model):
    GENDER_CHOICE = [
        ('L','Laki-laki'),
        ('P','Perempuan'),
    ]
    STATUS_CHOICE = [
        ('active','Active'),
        ('sakit','Sakit'),
        ('dikembalikan','Dikembalikan'),
        ('hilang','Hilang'),
        ('meninggal','Meninggal')
    ]

    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1,
                              choices=GENDER_CHOICE,
                              default='L',)
    birth_date = models.DateField()
    admission_date = models.DateField()
    status = models.CharField(max_length=20,
                              choices=STATUS_CHOICE,
                              default='active',
                             )
    address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.full_name} ({self.get_status_display()})"
from django.db import models


# Create your models here.
class FakultetData(models.Model):
    fakultet = models.CharField(max_length=100)
    students = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Number of students Data'

    def __str__(self):
        return f'{self.fakultet}-{self.students}'

from django.db import models


# Create your models here.
class Register(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='نام')
    last_name = models.CharField(max_length=50, verbose_name='نام خانوادگی')
    avg = models.IntegerField(verbose_name='معدل')
    grade = models.CharField(max_length=50, verbose_name='مقطع تحصیلی')
    field_study = models.CharField(max_length=50, verbose_name='رشته تحصیلی')
    university = models.CharField(max_length=50, verbose_name='دانشگاه')
    education_place = models.CharField(max_length=50, verbose_name='محل تحصیل')
    degree_education = models.ImageField(upload_to='about/', null=True, blank=True, verbose_name='مدرک تحصیلی')

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    @property
    def full_name(self):
        return self.get_full_name()

    def __str__(self):
        return self.get_full_name()

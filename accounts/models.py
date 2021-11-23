from django.db import models


# Create your models here.
class PersonalInformation(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='نام')
    last_name = models.CharField(max_length=50, verbose_name='نام خانوادگی')
    father_name = models.CharField(max_length=50, verbose_name='نام پدر')
    phone_number = models.CharField(max_length=11, verbose_name='شماره تماس')
    national_code = models.CharField(max_length=10, verbose_name='کد کلی')
    email = models.EmailField(verbose_name='ایمیل')

    def __str__(self):
        return self.email


class EducationalInformation(models.Model):
    GRADE = [('bachelors', 'کارشناس'), ('masters', 'کارشناسی ارشد'), ('Doctorate', 'دکترا')]
    ORIENTATION = [('مهندسی', 'مهندسی'), ('پزشکی', 'پزشکی'), ('علوم انسانی', 'علوم انسانی'),
                   ('علوم حوزوی', 'عوم حوزوی')]
    orientation = models.CharField(choices=ORIENTATION, max_length=20, verbose_name='گرایش ')
    grade = models.CharField(choices=GRADE, max_length=50, verbose_name='مقطع تحصیلی')
    field_study = models.CharField(max_length=50, verbose_name='رشته تحصیلی')
    avg = models.IntegerField(verbose_name='معدل')
    university = models.CharField(max_length=50, verbose_name='دانشگاه')
    education_place = models.CharField(max_length=50, verbose_name='محل تحصیل')
    degree_education = models.ImageField(upload_to='about/', null=True, blank=True, verbose_name='مدرک تحصیلی')

from django import forms


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=50, verbose_name='نام')
    last_name = forms.CharField(max_length=50, verbose_name='نام خانوادگی')
    avg = forms.IntegerField(verbose_name='معدل')
    grade = forms.CharField(max_length=50, verbose_name='مقطع تحصیلی')
    field_study = forms.CharField(max_length=50, verbose_name='رشته تحصیلی')
    university = forms.CharField(max_length=50, verbose_name='دانشگاه')
    education_place = forms.CharField(max_length=50, verbose_name='محل تحصیل')
    degree_education = forms.ImageField(upload_to='about/', verbose_name='مدرک تحصیلی')

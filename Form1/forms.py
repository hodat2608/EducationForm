from django import forms

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Nhan_vien, Thong_tin_nhan_vien


class Add_nhanvien_Form(forms.ModelForm):
    class Meta:
        model = Nhan_vien
        fields = ['Hoten', 'Msnv','Phongban']

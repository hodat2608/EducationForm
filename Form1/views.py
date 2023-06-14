from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import  HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.shortcuts import render, redirect
from .models import Nhan_vien, Thong_tin_nhan_vien
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.shortcuts import render
from .forms import Add_nhanvien_Form 

class List_nhan_vien(generic.ListView):
    template_name = 'DisplayWeb/Danh_sach_nhan_vien.html'
    context_object_name = 'Nhanviens'
    def get_queryset(self):
        return Nhan_vien.objects.all() 

class list_thongtinnhanvien(generic.DetailView):
    model = Nhan_vien
    template_name = 'DisplayWeb/Thong_tin_nhan_vien.html'    

def add_nhan_vien(request):
    if request.method == "POST": 
        form = Add_nhanvien_Form(request.POST)
        if form.is_valid():
            ho_ten = form.cleaned_data['Hoten']
            msnv = form.cleaned_data['Msnv']
            phong_ban = form.cleaned_data['Phongban']
            if Nhan_vien.objects.filter(Hoten=ho_ten).exists():
                return render(request, 'DisplayWeb/Danh_sach_nhan_vien.html',{ 'error1': "nhan vien nay da ton tai!",})
            add_nv = Nhan_vien.objects.create(Hoten=ho_ten,Msnv=msnv,Phongban=phong_ban)
            add_nv.save()
            return redirect('Form1:List_nhan_vien')
    else:
        form = Add_nhanvien_Form()
    return redirect('Form1:List_nhan_vien')
                    
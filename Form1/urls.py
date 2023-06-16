from django.urls import re_path, include,path
 
from . import views 
 
app_name = 'Form1'
urlpatterns = [
    re_path(r'^List_nhan_vien', views.List_nhan_vien.as_view(), name='List_nhan_vien'),
    re_path(r'^(?P<pk>[0-9]+)/List_thong_tin/$', views.list_thongtinnhanvien.as_view(), name='List_thong_tin'),
    re_path(r'^add_nhanvien/$', views.add_nhan_vien, name='add_nv'),
    re_path(r'^(?P<id_nhanvien>[0-9]+)/Form_danh_gia/$', views.Evaluation, name='evaluate'),
    re_path(r'^(?P<id_nhanvien>[0-9]+)/Infor_evaluated_form/$', views.Evaluated_form, name='evaluate_form'),
    re_path(r'^(?P<id_nhanvien>[0-9]+)/del_staff/$', views.Delete_staff, name='del_staff'),
    re_path(r'^(?P<id_nhanvien>[0-9]+)/del_infor/$', views.Delete_infor, name='del_infor'),
]
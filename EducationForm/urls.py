
from django.contrib import admin
from django.urls import re_path, path
from django.conf.urls import include

urlpatterns = [
    re_path('Form1/', include('Form1.urls')),
    re_path('admin/', admin.site.urls),
]
# Generated by Django 4.2.1 on 2023-06-13 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nhan_vien',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hoten', models.CharField(default='', max_length=20)),
                ('Msnv', models.IntegerField(default='', max_length=5)),
                ('Phongban', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Thong_tin_nhan_vien',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ngay_kiem_tra', models.DateField(default='', max_length=20)),
                ('Doi_tuong_danh_gia', models.CharField(default='', max_length=20)),
                ('Lan_danh_gia', models.CharField(default='', max_length=20)),
                ('Thoi_gian_TC', models.IntegerField(default='', max_length=100)),
                ('Ma_hoc_trinh', models.TextField(default='', max_length=10)),
                ('Diem', models.IntegerField(default='', max_length=100)),
                ('Phan_dinh', models.CharField(default='', max_length=20)),
                ('key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Form1.nhan_vien')),
            ],
        ),
    ]
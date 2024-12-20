# Generated by Django 5.0.4 on 2024-11-26 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ADMINsignin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminid_model', models.CharField(default='1BY23XX000', max_length=10)),
                ('name_model', models.CharField(default='xyz', max_length=60)),
                ('phoneno_model', models.CharField(default='+910000000000', max_length=13)),
                ('email_model', models.EmailField(max_length=50, unique=True)),
                ('password_model', models.CharField(max_length=50)),
                ('image_model', models.ImageField(default='NULL', upload_to='')),
            ],
        ),
    ]

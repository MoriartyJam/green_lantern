# Generated by Django 3.0.6 on 2020-06-15 13:56

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('CityID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('CountryID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=64)),
                ('Code', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to=settings.AUTH_USER_MODEL)),
                ('DealerID', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=64)),
                ('Email', models.EmailField(blank=True, max_length=70)),
                ('FirstName', models.CharField(max_length=64)),
                ('LastName', models.CharField(max_length=64)),
                ('CityID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealers.City')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='CountryID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealers.Country'),
        ),
    ]

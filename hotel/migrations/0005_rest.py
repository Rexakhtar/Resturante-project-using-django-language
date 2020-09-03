# Generated by Django 2.1.5 on 2019-07-25 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_remove_hotel_is_mvp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hotel.Hotel')),
            ],
        ),
    ]

# Generated by Django 4.2.3 on 2023-08-02 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('educacion', models.CharField(max_length=100)),
                ('experiencia_laboral', models.TextField()),
                ('habilidades', models.CharField(max_length=200)),
            ],
        ),
    ]

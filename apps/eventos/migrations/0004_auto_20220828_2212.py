# Generated by Django 3.2 on 2022-08-29 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0003_auto_20220828_2137'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modalidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='evento',
            name='modalidad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eventos.modalidad'),
        ),
    ]
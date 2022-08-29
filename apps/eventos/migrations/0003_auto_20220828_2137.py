# Generated by Django 3.2 on 2022-08-29 00:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0002_evento_lugar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('decripcion', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='evento',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eventos.categoria'),
        ),
    ]

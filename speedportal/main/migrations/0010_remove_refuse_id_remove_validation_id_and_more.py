# Generated by Django 4.2.6 on 2023-11-14 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_refuse_run_alter_validation_run'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='refuse',
            name='id',
        ),
        migrations.RemoveField(
            model_name='validation',
            name='id',
        ),
        migrations.AlterField(
            model_name='refuse',
            name='run',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.run'),
        ),
        migrations.AlterField(
            model_name='validation',
            name='run',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.run'),
        ),
    ]

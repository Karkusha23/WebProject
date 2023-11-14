# Generated by Django 4.2.6 on 2023-11-14 08:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_refuse_run_is_validated'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moderator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('can_make_moderators', models.BooleanField(default=False)),
                ('can_add_categories', models.BooleanField(default=False)),
                ('can_approve_runs', models.BooleanField(default=False)),
                ('can_ban', models.BooleanField(default=False)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.game')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'moderator',
                'verbose_name_plural': 'moderators',
                'unique_together': {('user', 'game')},
            },
        ),
    ]

# Generated by Django 5.0.1 on 2024-02-01 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_remove_game_move_is_first_game_first_move'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='first_move',
        ),
        migrations.AlterField(
            model_name='game',
            name='field_with_mines',
            field=models.JSONField(blank=True, default=None, null=True),
        ),
    ]
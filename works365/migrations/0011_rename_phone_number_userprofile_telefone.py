# Generated by Django 5.0.6 on 2024-06-25 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works365', '0010_userprofile_delete_profissional_delete_usuario_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='phone_number',
            new_name='telefone',
        ),
    ]

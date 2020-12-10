# Generated by Django 2.2.14 on 2020-07-26 14:10

import django.core.validators
from django.db import migrations, models
import django.utils.timezone
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ("gpauth", "0003_auto_20200712_1421"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="gpgroup",
            options={"verbose_name": "Group", "verbose_name_plural": "Groups"},
        ),
        migrations.AlterModelOptions(
            name="gppermission",
            options={"verbose_name": "Permission", "verbose_name_plural": "Permissões"},
        ),
        migrations.AlterModelOptions(
            name="user",
            options={"verbose_name": "Usuário", "verbose_name_plural": "Users"},
        ),
        migrations.AlterField(
            model_name="user",
            name="date_joined",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="Registration date"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                error_messages={"unique": "This email already exists."},
                help_text="The email will be used to access the system and send information",
                max_length=254,
                unique=True,
                validators=[django.core.validators.EmailValidator()],
                verbose_name="Email",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="email_confirmation",
            field=models.CharField(
                max_length=250, null=True, verbose_name="E-mail Confirmation"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="groups",
            field=models.ManyToManyField(
                blank=True,
                help_text="Os grupos que este usuário pertence. Um usuário terá todas as permissões concedidas a cada um dos seus grupos.",
                related_name="user_set",
                related_query_name="user",
                to="auth.Group",
                verbose_name="grupos",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(
                default=True,
                help_text="Only active users can access the system.",
                verbose_name="Active?",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_staff",
            field=models.BooleanField(
                default=False,
                help_text="Determines whether the user has access to the system panel.",
                verbose_name="Is part of the team?",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="name",
            field=models.CharField(
                help_text="Enter the user's full name.",
                max_length=200,
                verbose_name="Nome",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="photo",
            field=sorl.thumbnail.fields.ImageField(
                blank=True, null=True, upload_to="user/photos", verbose_name="Photo"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                help_text="Permissões específicas para este usuário.",
                related_name="user_set",
                related_query_name="user",
                to="auth.Permission",
                verbose_name="permissões do usuário",
            ),
        ),
    ]

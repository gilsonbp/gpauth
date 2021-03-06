# Generated by Django 2.2.4 on 2019-08-18 21:58

import django.core.validators
from django.db import migrations, models
import django.utils.timezone
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ("gpauth", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="gpgroup",
            options={"verbose_name": "Grupo", "verbose_name_plural": "Grupos"},
        ),
        migrations.AlterModelOptions(
            name="gppermission",
            options={"verbose_name": "Permissão", "verbose_name_plural": "Permissões"},
        ),
        migrations.AlterModelOptions(
            name="user",
            options={"verbose_name": "Usuário", "verbose_name_plural": "Usuários"},
        ),
        migrations.AlterField(
            model_name="user",
            name="date_joined",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="Data de cadastro"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                error_messages={"unique": "Esse email já existe."},
                help_text="O email será usado para acessar o sistema e enviar informações",
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
                max_length=250, null=True, verbose_name="Confirmação de email"
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
                help_text="Somente usuários ativos podem acessar o sistema.",
                verbose_name="Ativo?",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_staff",
            field=models.BooleanField(
                default=False,
                help_text="Determina se o usuário tem acesso ao painel administrador do sistema.",
                verbose_name="Faz parte da equipe?",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="name",
            field=models.CharField(
                help_text="Digite o nome completo do usuário.",
                max_length=200,
                verbose_name="Nome",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="photo",
            field=sorl.thumbnail.fields.ImageField(
                blank=True, null=True, upload_to="user/photos", verbose_name="Foto"
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

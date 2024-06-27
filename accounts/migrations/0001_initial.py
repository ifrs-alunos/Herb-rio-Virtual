# Generated by Django 3.2.7 on 2024-06-12 22:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='Mensagem')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Data de envio')),
                ('status', models.CharField(choices=[('sent', 'Em análise'), ('accepted', 'Aceita'), ('denied', 'Negada')], default='sent', max_length=8)),
                ('term', models.BooleanField(default=False, verbose_name='Termo de cessão de uso de materiais audiovisuais')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitations', to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Solicitação',
                'verbose_name_plural': 'Solicitações',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Não utilize abreviações nos sobrenomes.', max_length=200, verbose_name='Nome completo')),
                ('institution', models.CharField(help_text='Caso possuia mais de uma, escreva a que atua principalmente.', max_length=150, verbose_name='Instituição de trabalho e/ou estudo')),
                ('role', models.CharField(help_text='Utilize como base seu cargo na instituição citada.', max_length=100, verbose_name='Cargo de ofício')),
                ('phone', models.CharField(help_text='Informe o DDD e, em seguida, seu número.', max_length=11, unique=True, verbose_name='Telefone fixo ou celular')),
                ('cpf', models.CharField(help_text='Informe o CPF somente com números.', max_length=11, verbose_name='CPF')),
                ('rg', models.CharField(max_length=10, verbose_name='RG')),
                ('get_messages', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contribuition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contribuitions', to='accounts.profile', verbose_name='Perfil')),
            ],
        ),
    ]
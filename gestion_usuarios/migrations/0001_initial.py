# Generated by Django 2.0.4 on 2018-06-07 05:40

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
            name='Asignatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento_Provincial_Educacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Encargado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asignatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_usuarios.Asignatura')),
            ],
        ),
        migrations.CreateModel(
            name='Establecimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=100)),
                ('departamento_Provincial_Educacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_usuarios.Departamento_Provincial_Educacion')),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('autor_rut', models.CharField(max_length=15)),
                ('establecimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_usuarios.Establecimiento')),
            ],
            options={
                'verbose_name': 'grupo',
                'verbose_name_plural': 'grupos',
            },
        ),
        migrations.CreateModel(
            name='Servicio_Local_Educacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asignatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_usuarios.Asignatura')),
                ('departamento_Provincial_Educacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_usuarios.Departamento_Provincial_Educacion')),
                ('servicio_Local_Educacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_usuarios.Servicio_Local_Educacion')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='establecimiento',
            name='servicio_Local_Educacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_usuarios.Servicio_Local_Educacion'),
        ),
        migrations.AddField(
            model_name='encargado',
            name='establecimiento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_usuarios.Establecimiento'),
        ),
        migrations.AddField(
            model_name='encargado',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

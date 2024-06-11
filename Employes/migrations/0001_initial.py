# Generated by Django 5.0.6 on 2024-06-11 15:19

import django.core.validators
import django.db.models.deletion
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estados',
            fields=[
                ('codEstado', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('estado', models.CharField(max_length=30, verbose_name='Estado')),
                ('capital', models.CharField(max_length=30, verbose_name='Capital')),
                ('sigla', models.CharField(blank=True, max_length=2, null=True, verbose_name='Sigla')),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estados',
                'db_table': 'estados',
                'ordering': ['estado'],
            },
        ),
        migrations.CreateModel(
            name='Employes',
            fields=[
                ('status', models.CharField(blank=True, choices=[('AC', 'ACTIVO'), ('HP', 'HONORARIOS PROFESIONALES'), ('JUB', 'JUBILADO')], max_length=3, null=True, verbose_name='Status')),
                ('cedper', models.CharField(max_length=9, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(6)], verbose_name='cedula')),
                ('nomper', models.CharField(max_length=40, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='Nombre')),
                ('apeper', models.CharField(max_length=40, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='Apellido')),
                ('telmovper', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=13, null=True, region=None, verbose_name='Telf. Movil')),
                ('dependencia', models.CharField(choices=[('AUD', 'AUDITORIA INTERNA'), ('CON', 'CONSULTORIA JURIDICA'), ('LIC', 'LICITACIÓN Y CONTRATACIÓN'), ('PRE', 'PRESIDENCIA'), ('VPGC', 'VICEPRESIDENCIA DE GESTION COMERCIAL'), ('VPGC', 'VICEPRESIDENCIA DE SERVICIOS HIDROLOGICOS'), ('VPGI', 'VICEPRESIDENCIA GESTION INTERNA')], max_length=255, verbose_name='Ubicacion Admistración')),
                ('oficina', models.CharField(choices=[('ADM', 'GERENCIA DE ADMINISTRACION'), ('BPB', 'GERENCIA DE BIENES PUBLICOS'), ('CEA', 'CENTRO DE ESTUDIOS DEL AGUA'), ('COM', 'GERENCIA DE COMUNICACION'), ('FOR', 'GERENCIA DE FORTALECIMIENTO DEL PODER POPULAR'), ('GDC', 'GERENCIA DE DESARROLLO COMERCIAL'), ('GGC', 'GERENCIA DE COMERCIALIZACIÓN'), ('GGD', 'GERENCIA DEL DESPACHO'), ('GGSG', 'GERENCIA DE SEGURIDAD INTEGRAL SERVICIOS GENERALES'), ('GOC', 'GERENCIA DE OPERACIONES COMERCIALES'), ('GOP', 'GERENCIA DE OPERACIONES MANTENIMIENTO Y CALIDAD DEL AGUA'), ('GST', 'GERENCIA DE SOPORTE TECNICO COMERCIAL'), ('GTA', 'GERENCIA DE TRAMITES ADUANEROS'), ('N/A', 'NO APLICA'), ('PPO', 'GERENCIA DE PLANIFICACION PRESUPUESTO Y ORGANIZACION'), ('PRO', 'GERENCIA DE PROYECTOS'), ('RRH', 'GERENCIA DE TALENTO HUMANO'), ('SEG', 'GERENCIA DE SEGUIMIENTO'), ('TEC', 'GERENCIA DE TECNOLOGIA')], max_length=10, verbose_name='Oficina')),
                ('cargo', models.CharField(choices=[('AN', 'ANALISTA'), ('AS', 'ASISTENTE'), ('CH', 'CHOFER'), ('ESP', 'ESPECIALISTA'), ('GG', 'GERENTE GENERAL'), ('GL', 'GERENTE DE LINEA'), ('JD', 'JEFE DE DIVISIÓN'), ('ND', 'NO DEFINIDO'), ('OB', 'OBRERO'), ('SEC', 'SECRETARIA'), ('SUP', 'SUPERVISOR')], default='DN', max_length=10, verbose_name='Cargo')),
                ('municipio', models.CharField(max_length=30, verbose_name='Municipio')),
                ('parroquia', models.CharField(max_length=30, verbose_name='Parroquia')),
                ('centro', models.TextField(blank=True, null=True, verbose_name='Centro de Votacion')),
                ('votacion', models.BooleanField(default=False, verbose_name='Votacion')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employes.estados', verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'db_table': 'employes',
                'ordering': ['-cedper'],
            },
        ),
    ]

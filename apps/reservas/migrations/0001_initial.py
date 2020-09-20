# Generated by Django 2.2 on 2020-09-17 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=4)),
                ('tipo', models.CharField(max_length=50)),
                ('planta', models.CharField(choices=[('PB', 'Planta baja'), ('1', '1er Piso'), ('2', '2do Piso'), ('3', '3er Piso')], max_length=2)),
                ('activa', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_ingreso', models.DateField()),
                ('fecha_salida', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ServicioIncluido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('detalle', models.TextField(max_length=150)),
                ('incluye', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reservacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adultos', models.IntegerField()),
                ('ninos', models.IntegerField()),
                ('hora_llegada', models.TimeField()),
                ('activa', models.BooleanField(default=True)),
                ('peticion_adicional', models.TextField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reservas.Cliente')),
                ('habitacion', models.ManyToManyField(related_name='habitaciones', to='reservas.Habitacion')),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.Periodo')),
                ('servicio_incluido', models.ManyToManyField(related_name='servicios_incluidos', to='reservas.ServicioIncluido')),
            ],
        ),
    ]

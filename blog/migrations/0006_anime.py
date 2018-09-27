# Generated by Django 2.1.1 on 2018-09-27 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_producto_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, null=True)),
                ('autor', models.CharField(max_length=50)),
                ('descripcion', models.TextField(blank=True)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField(blank=True, null=True)),
                ('genero', models.CharField(max_length=50)),
                ('capitulos', models.IntegerField()),
                ('link', models.CharField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(blank=True, upload_to='img/')),
                ('imagen_portada', models.ImageField(blank=True, upload_to='img/')),
                ('fecha_publicacion', models.DateField(blank=True, null=True)),
            ],
        ),
    ]

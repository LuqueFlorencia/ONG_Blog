# Generated by Django 3.2 on 2022-12-06 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('cuerpo', models.TextField()),
                ('imagen', models.ImageField(upload_to='noticias')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('categoria_noticia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noticias.categoria')),
            ],
        ),
    ]



from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name_plural': 'Student'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name_plural': 'Teacher'},
        ),
        migrations.AddField(
            model_name='student',
            name='phone',
            field=models.IntegerField(blank=True, null=True, verbose_name='Phone Number'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='phone',
            field=models.IntegerField(blank=True, null=True, verbose_name='Phone Number'),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='Username'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]



from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20211011_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirm_password',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=10000),
        ),
    ]

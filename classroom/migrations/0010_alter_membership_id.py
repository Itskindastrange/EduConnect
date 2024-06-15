

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0009_remove_roomstream_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

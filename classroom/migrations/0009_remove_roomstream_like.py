

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0008_roomstream_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomstream',
            name='like',
        ),
    ]

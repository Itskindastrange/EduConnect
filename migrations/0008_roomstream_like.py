

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0007_auto_20210720_0046'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomstream',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]

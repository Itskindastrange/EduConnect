

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0006_classroom_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='cover',
            field=models.ImageField(default='others/class.jpg', null=True, upload_to='others/cover/'),
        ),
    ]

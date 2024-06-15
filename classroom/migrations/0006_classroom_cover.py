

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0005_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='cover',
            field=models.ImageField(default='others/class.jpeg', null=True, upload_to='others/cover/'),
        ),
    ]

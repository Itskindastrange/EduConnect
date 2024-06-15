

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member', to='profiles.student'),
        ),
    ]

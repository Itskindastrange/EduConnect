

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('classroom', '0002_auto_20210711_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='classroom', to='classroom.classroom'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='members', to='profiles.student'),
        ),
    ]



from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, null=True)),
                ('unit', models.CharField(max_length=100, null=True)),
                ('code', models.CharField(blank=True, max_length=8, null=True)),
                ('details', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MemberShip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_join', models.BooleanField(default=False)),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='classroom.classroom')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.student')),
            ],
        ),
        migrations.AddField(
            model_name='classroom',
            name='student',
            field=models.ManyToManyField(related_name='s_room', through='classroom.MemberShip', to='profiles.Student'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='room', to='profiles.teacher'),
        ),
        migrations.CreateModel(
            name='ClassFiles',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('class_files', models.FileField(blank=True, null=True, upload_to='files/')),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='classroom.classroom')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='profiles.teacher')),
            ],
            options={
                'verbose_name': 'Class File',
                'verbose_name_plural': 'Class Files',
            },
        ),
    ]

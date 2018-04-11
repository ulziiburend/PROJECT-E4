# Generated by Django 2.0.2 on 2018-04-07 15:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('connection_id', models.IntegerField(primary_key=True, serialize=False)),
                ('connection_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.IntegerField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=150)),
                ('course_level', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('exercise_id', models.IntegerField(primary_key=True, serialize=False)),
                ('score', models.FloatField()),
                ('difficulty_index', models.FloatField()),
                ('duration_allowed', models.TimeField()),
                ('success_rate', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='LMSUser',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.IntegerField(primary_key=True, serialize=False)),
                ('exercise_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Exercise')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role', models.CharField(choices=[('AD', 'Administrator'), ('TH', 'Teacher'), ('ST', 'Student'), ('AC', 'Anticheat')], default='TH', max_length=2, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Sheet',
            fields=[
                ('sheet_id', models.IntegerField(primary_key=True, serialize=False)),
                ('sheet_name', models.CharField(max_length=25)),
                ('number_exercises', models.IntegerField()),
                ('end_date', models.DateTimeField()),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Student_Course',
            fields=[
                ('student_course_id', models.IntegerField(primary_key=True, serialize=False)),
                ('teacher_feedback', models.CharField(max_length=100)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Course')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student_Exercise',
            fields=[
                ('student_exercise_id', models.IntegerField(primary_key=True, serialize=False)),
                ('number_of_attempts', models.IntegerField()),
                ('number_of_tries', models.FloatField()),
                ('time_spend_by_exercises', models.IntegerField()),
                ('time_spend_succeed', models.IntegerField()),
                ('total_time_spent', models.IntegerField()),
                ('number_abort', models.IntegerField()),
                ('score', models.FloatField()),
                ('number_correct_attempts', models.IntegerField()),
                ('student_level', models.CharField(max_length=2)),
                ('completed_time', models.IntegerField()),
                ('feedback', models.CharField(max_length=100)),
                ('submit_date', models.DateTimeField()),
                ('exercise_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Exercise')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student_Question',
            fields=[
                ('student_question_id', models.IntegerField(primary_key=True, serialize=False)),
                ('question_status', models.IntegerField(choices=[('SK', 'Skipped'), ('CR', 'Correct'), ('IN', 'Incorrect'), ('ST', 'Started'), ('NL', 'Null')], default='NL', null=True)),
                ('time_spent', models.IntegerField()),
                ('submit_date', models.DateTimeField()),
                ('Question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Question')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student_Sheet',
            fields=[
                ('student_sheet_id', models.IntegerField(primary_key=True, serialize=False)),
                ('score', models.FloatField()),
                ('feedback', models.CharField(max_length=100)),
                ('total_time_spent', models.IntegerField()),
                ('sheet_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Sheet')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='lmsuser',
            name='role',
            field=models.ManyToManyField(blank=True, to='login.Role'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='sheet_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Sheet'),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='connection',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

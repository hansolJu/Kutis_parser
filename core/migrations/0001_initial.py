# Generated by Django 2.0.5 on 2018-05-19 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LatestUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latest_update', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentGrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eisu', models.CharField(blank=True, max_length=50, null=True)),
                ('certification', models.CharField(blank=True, max_length=50, null=True)),
                ('yearNsemester', models.CharField(blank=True, max_length=50, null=True)),
                ('subject_code', models.CharField(blank=True, max_length=50, null=True)),
                ('subject', models.CharField(blank=True, max_length=50, null=True)),
                ('score', models.CharField(blank=True, max_length=50, null=True)),
                ('grade_design', models.CharField(blank=True, max_length=50, null=True)),
                ('grade', models.CharField(blank=True, max_length=50, null=True)),
                ('valid', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('hukbun', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('jumin', models.CharField(max_length=30)),
                ('name_Hanja', models.CharField(blank=True, max_length=30, null=True)),
                ('name_English', models.CharField(blank=True, max_length=30, null=True)),
                ('campus', models.CharField(blank=True, max_length=30, null=True)),
                ('dayNight', models.CharField(blank=True, max_length=30, null=True)),
                ('state', models.CharField(blank=True, max_length=30, null=True)),
                ('variance', models.CharField(blank=True, max_length=30, null=True)),
                ('graduationCredit', models.CharField(blank=True, max_length=30, null=True)),
                ('major', models.CharField(blank=True, max_length=30, null=True)),
                ('advisor', models.CharField(blank=True, max_length=30, null=True)),
                ('currentGrade', models.CharField(blank=True, max_length=30, null=True)),
                ('compleSemester', models.CharField(blank=True, max_length=30, null=True)),
                ('earlyGraduation', models.CharField(blank=True, max_length=30, null=True)),
                ('admission', models.CharField(blank=True, max_length=30, null=True)),
                ('enginCertification', models.CharField(blank=True, max_length=30, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('cellPhone', models.CharField(blank=True, max_length=50, null=True)),
                ('parentsPhone', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='studentgrade',
            name='hukbun',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.StudentInfo'),
        ),
        migrations.AddField(
            model_name='latestupdate',
            name='StudentInfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.StudentInfo'),
        ),
    ]

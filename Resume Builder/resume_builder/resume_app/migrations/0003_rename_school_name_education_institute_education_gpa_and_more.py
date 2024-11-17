# Generated by Django 5.1.3 on 2024-11-10 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_app', '0002_remove_resume_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='school_name',
            new_name='institute',
        ),
        migrations.AddField(
            model_name='education',
            name='gpa',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='resume',
            name='Phone_No',
            field=models.PositiveBigIntegerField(default=9663768094),
        ),
        migrations.AddField(
            model_name='resume',
            name='email',
            field=models.EmailField(default='abc@email.com', max_length=254),
        ),
        migrations.AddField(
            model_name='resume',
            name='name',
            field=models.CharField(default='Your Name', max_length=255),
        ),
        migrations.AddField(
            model_name='skill',
            name='proficiency',
            field=models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], default='Beginner', max_length=50),
        ),
        migrations.AlterField(
            model_name='language',
            name='proficiency',
            field=models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], default='Beginner', max_length=50),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='company',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='job_title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='start_date',
            field=models.DateField(null=True),
        ),
    ]

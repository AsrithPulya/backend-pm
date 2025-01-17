# Generated by Django 5.1.3 on 2025-01-07 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_employee_emergency_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeeattachments',
            old_name='created_by',
            new_name='file_name',
        ),
        migrations.RemoveField(
            model_name='employeeattachments',
            name='file',
        ),
        migrations.RemoveField(
            model_name='employeeattachments',
            name='filename',
        ),
        migrations.AddField(
            model_name='employeeattachments',
            name='document_type',
            field=models.CharField(choices=[('aadhar', 'Aadhar Card'), ('pan', 'Pan Card')], default='aadhar', max_length=20),
        ),
        migrations.AlterField(
            model_name='employee',
            name='adhaar_number',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.DeleteModel(
            name='UserFile',
        ),
    ]

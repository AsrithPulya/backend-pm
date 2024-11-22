# Generated by Django 5.1.2 on 2024-11-21 10:39

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_alter_employeeleavesrequests_employee_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeeleavesrequests',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='employeeleavesrequests',
            name='leave_day_type',
        ),
        migrations.RemoveField(
            model_name='employeeleavesrequests',
            name='start_date',
        ),
        migrations.CreateModel(
            name='EmployeeLeavesRequestsDates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('leave_day_type', models.CharField(choices=[('Full day', 'Full day'), ('Half day (1st half)', 'Half day (1st half)'), ('Half day (2nd half)', 'Half day (2nd half)')], default='Full day', max_length=20)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_leaves_requests_dates', to='employee.employee')),
            ],
        ),
    ]

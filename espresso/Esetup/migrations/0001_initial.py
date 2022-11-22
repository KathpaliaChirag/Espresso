# Generated by Django 4.1.1 on 2022-11-21 15:40

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='LiabraryBook',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('book_name', models.CharField(max_length=255)),
                ('publication_name', models.CharField(max_length=255)),
                ('Author_name', models.CharField(max_length=255)),
                ('purchased_on', models.DateTimeField(blank=True)),
                ('book_status', models.BooleanField(default=False)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('session_start', models.CharField(max_length=255)),
                ('session_end', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='staff',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.TextField()),
                ('created_at', models.DateTimeField(blank=True)),
                ('updated_at', models.DateTimeField(blank=True)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(choices=[(1, 'Hod'), (2, 'staff'), (3, 'student')], default=1, max_length=10)),
                ('display_pic', models.ImageField(default='', upload_to='displaypic')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='subjects',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('subjects_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(blank=True)),
                ('updated_at', models.DateTimeField(blank=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Esetup.courses')),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Esetup.staff')),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.TextField()),
                ('gender', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(blank=True)),
                ('updated_at', models.DateTimeField(blank=True)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Esetup.courses')),
                ('session_id', models.ForeignKey(default='timezone.now', on_delete=django.db.models.deletion.DO_NOTHING, to='Esetup.session')),
            ],
        ),
        migrations.CreateModel(
            name='studentFeedback',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('feedback', models.TextField()),
                ('feedback_reply', models.TextField()),
                ('created_at', models.DateTimeField(blank=True)),
                ('updated_at', models.DateTimeField(blank=True)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Esetup.students')),
            ],
        ),
        migrations.CreateModel(
            name='staffFeedback',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('feedback', models.CharField(max_length=255)),
                ('feedback_reply', models.TextField()),
                ('created_at', models.DateTimeField(blank=True)),
                ('updated_at', models.DateTimeField(blank=True)),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Esetup.staff')),
            ],
        ),
        migrations.AddField(
            model_name='staff',
            name='admin',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='NotificationStudent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(blank=True)),
                ('updated_at', models.DateTimeField(blank=True)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Esetup.students')),
            ],
        ),
        migrations.CreateModel(
            name='NotificationStaff',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(blank=True)),
                ('updated_at', models.DateTimeField(blank=True)),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Esetup.staff')),
            ],
        ),
        migrations.CreateModel(
            name='LeaveReportstudent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('leave_date', models.CharField(max_length=255)),
                ('leave_reason', models.TextField()),
                ('leave_status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(blank=True)),
                ('updated_at', models.DateTimeField(blank=True)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Esetup.students')),
            ],
        ),
        migrations.CreateModel(
            name='LeaveReportstaff',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('leave_date', models.CharField(max_length=255)),
                ('leave_reason', models.TextField()),
                ('leave_status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(blank=True)),
                ('updated_at', models.DateTimeField(blank=True)),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Esetup.staff')),
            ],
        ),
        migrations.CreateModel(
            name='Issuedstatusstudent',
            fields=[
                ('issue_id', models.AutoField(primary_key=True, serialize=False)),
                ('issue_date', models.CharField(max_length=255)),
                ('return_date', models.CharField(max_length=255)),
                ('issue_status', models.BooleanField(default=False)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Esetup.students')),
            ],
        ),
        migrations.CreateModel(
            name='Issuedstatusstaff',
            fields=[
                ('issue_id', models.AutoField(primary_key=True, serialize=False)),
                ('issue_date', models.CharField(max_length=255)),
                ('return_date', models.CharField(max_length=255)),
                ('issue_status', models.BooleanField(default=False)),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Esetup.staff')),
            ],
        ),
        migrations.CreateModel(
            name='attendence',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('attendence_date', models.DateTimeField(blank=True)),
                ('created_at', models.DateTimeField(blank=True)),
                ('updated_at', models.DateTimeField(blank=True)),
                ('Student_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Esetup.students')),
            ],
        ),
        migrations.CreateModel(
            name='AttendanceStatus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(blank=True)),
                ('updated_at', models.DateTimeField(blank=True)),
                ('attendence_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Esetup.attendence')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Esetup.students')),
            ],
        ),
        migrations.CreateModel(
            name='AdminHOD',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(blank=True)),
                ('updated_at', models.DateTimeField(blank=True)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]

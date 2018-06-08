# Generated by Django 2.0.6 on 2018-06-08 18:09

from django.db import migrations, models
import foundation.models.shared_user
import starterkit.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='SharedUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('last_modified', models.DateTimeField(auto_now=True, db_index=True)),
                ('salt', models.CharField(blank=True, default=starterkit.utils.generate_hash, help_text='The unique salt value me with this object.', max_length=127, null=True, unique=True, verbose_name='Salt')),
                ('was_email_activated', models.BooleanField(default=False, help_text='Was the email address verified as an existing address?', verbose_name='Was Email Activated')),
                ('pr_access_code', models.CharField(blank=True, default=starterkit.utils.generate_hash, help_text='The access code to enter the password reset page to be granted access to restart your password.', max_length=127, verbose_name='Password Reset Access Code')),
                ('pr_expiry_date', models.DateTimeField(blank=True, default=foundation.models.shared_user.get_expiry_date, help_text='The date where the access code expires and no longer works.', verbose_name='Password Reset Access Code Expiry Date')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'comicscantina_users',
            },
            managers=[
                ('objects', foundation.models.shared_user.SharedUserManager()),
            ],
        ),
    ]

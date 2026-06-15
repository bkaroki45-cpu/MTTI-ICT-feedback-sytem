# Generated for the institutional feedback platform upgrade.

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_remove_ictfeedback_academic_guidance_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.DeleteModel(
            name='ICTFeedback',
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
                ('slug', models.SlugField(max_length=140, unique=True)),
                ('unit_type', models.CharField(choices=[('core', 'Core Department'), ('support', 'Support / Institutional Unit')], default='core', max_length=20)),
                ('description', models.TextField()),
                ('contact_email', models.EmailField(blank=True, max_length=254)),
                ('contact_phone', models.CharField(blank=True, max_length=40)),
                ('staff_contact', models.CharField(blank=True, max_length=160)),
                ('allow_public_feedback', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={'ordering': ['unit_type', 'name']},
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=180)),
                ('body', models.TextField()),
                ('announcement_type', models.CharField(choices=[('notice', 'School Notice'), ('fees', 'Fee Update'), ('exams', 'Exam Schedule'), ('alert', 'General Alert')], default='notice', max_length=20)),
                ('published_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_published', models.BooleanField(default=True)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='announcements', to='feed.department')),
            ],
            options={'ordering': ['-published_at']},
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=160)),
                ('description', models.TextField()),
                ('starts_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('location', models.CharField(max_length=160)),
                ('is_published', models.BooleanField(default=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_events', to=settings.AUTH_USER_MODEL)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events', to='feed.department')),
            ],
            options={'ordering': ['starts_at']},
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_type', models.CharField(choices=[('anonymous', 'Anonymous Feedback'), ('student', 'Identified Feedback (Student)'), ('staff', 'Identified Feedback (Staff)'), ('guest', 'Guest Feedback')], max_length=20)),
                ('category', models.CharField(choices=[('complaint', 'Complaint'), ('suggestion', 'Suggestion'), ('appreciation', 'Appreciation'), ('report', 'Report'), ('other', 'Other')], max_length=20)),
                ('message', models.TextField()),
                ('attachment', models.FileField(blank=True, upload_to='feedback_attachments/')),
                ('admission_number', models.CharField(blank=True, max_length=40)),
                ('student_class', models.CharField(blank=True, max_length=80, verbose_name='Class')),
                ('full_name', models.CharField(blank=True, max_length=120)),
                ('guest_name', models.CharField(blank=True, max_length=120)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('in_review', 'In Review'), ('resolved', 'Resolved')], default='pending', max_length=20)),
                ('admin_reply', models.TextField(blank=True)),
                ('smart_tags', models.CharField(blank=True, help_text='Comma-separated tags generated manually or by a future AI classifier.', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='feedback_items', to='feed.department')),
            ],
            options={'ordering': ['-created_at']},
        ),
        migrations.CreateModel(
            name='EventFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120)),
                ('rating', models.PositiveSmallIntegerField(blank=True, choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')], null=True)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedback_items', to='feed.event')),
            ],
            options={'ordering': ['-created_at']},
        ),
    ]

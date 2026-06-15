# Generated for event image uploads.

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0004_school_management_feedback_platform'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, upload_to='event_images/'),
        ),
    ]

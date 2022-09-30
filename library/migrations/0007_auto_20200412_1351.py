from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_auto_20200409_1651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issuedbook',
            name='enrollment',
        ),
        migrations.RemoveField(
            model_name='issuedbook',
            name='isbn',
        ),
    ]

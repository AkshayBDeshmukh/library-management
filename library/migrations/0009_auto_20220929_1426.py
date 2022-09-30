from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_auto_20200412_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('education', 'Education'),
        ('mechatronics ', 'Mechatronics'),
        ('computerscience ', 'Computer Science '),
        ('mechanical', 'Mechanical'),
        ('electronics', 'Electronics'),
        ('civil', 'Civil'),
        ('automobile', 'Automobile'),
        ('biotechnology', 'Biotechnology'),
        ('software', 'Software'),
        ('power','Power')], default='education', max_length=30),
        ),
    ]

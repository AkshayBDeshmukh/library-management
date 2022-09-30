from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('isbn', models.PositiveIntegerField()),
                ('author', models.CharField(max_length=40)),
                ('category', models.CharField(choices=[('education', 'Education'),('mechatronics ', 'Mechatronics'),
        ('computerscience ', 'Computer Science '),('mechanical', 'Mechanical'),('electronics', 'Electronics'),('civil', 'Civil'),('automobile', 'Automobile'),('biotechnology', 'Biotechnology'),('software', 'Software'),('power','Power')], default='education', max_length=30)),
            ],
        ),
    ]
    
    

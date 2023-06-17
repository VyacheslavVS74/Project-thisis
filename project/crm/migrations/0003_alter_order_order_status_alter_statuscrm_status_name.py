# Generated by Django 4.1.7 on 2023-06-18 00:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_alter_order_order_email_alter_order_order_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.ForeignKey(blank=True, default='Новый', null=True, on_delete=django.db.models.deletion.PROTECT, to='crm.statuscrm', verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='statuscrm',
            name='status_name',
            field=models.CharField(max_length=150, verbose_name='Название статуса'),
        ),
    ]
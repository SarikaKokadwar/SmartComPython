# Generated by Django 5.1.1 on 2024-10-24 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customerrequest', '0013_facilityhasapplink_and_more'),
        ('facilitylinks', '0003_remove_facilityhasapplink_facility_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FacilityHasAppLink',
        ),
    ]

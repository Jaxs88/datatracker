# Generated by Django 4.2.6 on 2023-10-27 17:57

'''
MeetingRegistration reg_type and checkedin fields are not populated for meetings 
prior to 108. For meetings 72-106, all records are for onsite checkedin participants.
For meeting 107 all records are for remote paticipants. Set accordingly.
'''

from django.db import migrations


def forward(apps, schema_editor):
    MeetingRegistration = apps.get_model("stats", "MeetingRegistration")
    MeetingRegistration.objects.filter(meeting__number=107).update(reg_type='remote')
    MeetingRegistration.objects.filter(meeting__number__lte=106, reg_type='').update(reg_type='onsite', checkedin=True)


def reverse(apps, schema_editor):
    MeetingRegistration = apps.get_model("stats", "MeetingRegistration")
    MeetingRegistration.objects.filter(meeting__number=107).update(reg_type='')
    MeetingRegistration.objects.filter(meeting__number__lte=106, reg_type='onsite').update(reg_type='', checkedin=False)


class Migration(migrations.Migration):
    dependencies = [
        ("stats", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(forward, reverse),
    ]
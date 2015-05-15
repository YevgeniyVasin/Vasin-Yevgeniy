# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ApplicationNumber', models.CharField(max_length=200)),
                ('ApplicationDate', models.DateField(max_length=200)),
                ('Act', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Burn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('NamePerson', models.CharField(max_length=200)),
                ('BurnDate', models.DateField(max_length=200)),
                ('BurnPlace', models.CharField(max_length=200)),
                ('LiveStillBurn', models.BooleanField(default=True)),
                ('CertificateSerialNumber', models.CharField(max_length=200)),
                ('IDApplication', models.ForeignKey(to='labkpz.Application')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ChangeName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('NewName', models.CharField(max_length=200)),
                ('IDApplication', models.ForeignKey(to='labkpz.Application')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Die',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('DieDate', models.DateField(max_length=200)),
                ('DiePlace', models.CharField(max_length=200)),
                ('DieReason', models.CharField(max_length=200)),
                ('CertificateSerialNumber', models.CharField(max_length=200)),
                ('IDApplication', models.ForeignKey(to='labkpz.Application')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Marriage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('OldSurnameM', models.CharField(max_length=200)),
                ('NewSurnameM', models.CharField(max_length=200)),
                ('OldSurnameW', models.CharField(max_length=200)),
                ('NewSurnameW', models.CharField(max_length=200)),
                ('Organization', models.CharField(max_length=200)),
                ('CertificateSerialNumber', models.CharField(max_length=200)),
                ('IDApplication', models.ForeignKey(to='labkpz.Application')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name_Person', models.CharField(max_length=200)),
                ('Citizenship', models.CharField(max_length=200)),
                ('SerialNumberPassport', models.CharField(max_length=200)),
                ('Adress', models.CharField(max_length=200)),
                ('Birthday', models.DateField(max_length=200)),
                ('BurnPlace', models.CharField(max_length=200)),
                ('IssueBy', models.CharField(max_length=200)),
                ('DateOfIssue', models.DateField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='marriage',
            name='IDFiance',
            field=models.ForeignKey(related_name='Fiance', to='labkpz.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='marriage',
            name='IDFiancee',
            field=models.ForeignKey(related_name='Fiancee', to='labkpz.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='die',
            name='IDPerson',
            field=models.ForeignKey(to='labkpz.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='burn',
            name='IDFather',
            field=models.ForeignKey(related_name='Father', to='labkpz.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='burn',
            name='IDMother',
            field=models.ForeignKey(related_name='Mother', to='labkpz.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='application',
            name='IDApplicant',
            field=models.ForeignKey(to='labkpz.Person'),
            preserve_default=True,
        ),
    ]

from django.db import models

class Person(models.Model):
    Name_Person = models.CharField(max_length=200)
    Citizenship = models.CharField(max_length=200)
    SerialNumberPassport = models.CharField(max_length=200)
    Adress = models.CharField(max_length=200)
    Birthday = models.DateField(max_length=200)
    BurnPlace = models.CharField(max_length=200)
    IssueBy = models.CharField(max_length=200)
    DateOfIssue = models.DateField(max_length=200)

class Application(models.Model):
    ApplicationNumber = models.DecimalField(max_length=200)
    ApplicationDate = models.DateField(max_length=200)
    IDApplicant = models.ForeignKey(Person)
    Act = models.CharField(max_length=200)

class Marriage(models.Model):
    IDApplication = models.ForeignKey(Application)
    IDFiance = models.ForeignKey(Person)
    IDFiancee = models.ForeignKey(Person)
    OldSurnameM = models.CharField(max_length=200)
    NewSurnameM = models.CharField(max_length=200)
    OldSurnameW = models.CharField(max_length=200)
    NewSurnameW = models.CharField(max_length=200)
    Organization = models.CharField(max_length=200)
    CertificateSerialNumber = models.CharField(max_length=200)

class Die(models.Model):
    IDApplication = models.ForeignKey(Application)
    IDPerson = models.ForeignKey(Person)
    DieDate = models.DateField(max_length=200)
    DiePlace = models.CharField(max_length=200)
    DieReason = models.CharField(max_length=200)
    CertificateSerialNumber = models.CharField(max_length=200)

class Burn(models.Model):
    IDApplication = models.ForeignKey(Application)
    NamePerson = models.CharField(max_length=200)
    BurnDate = models.DateField(max_length=200)
    BurnPlace = models.CharField(max_length=200)
    LiveStillBurn = models.BooleanField(default=True)
    IDFather = models.ForeignKey(Person)
    IDMother = models.ForeignKey(Person)
    CertificateSerialNumber = models.CharField(max_length=200)

class ChangeName(models.Model):
    IDApplication = models.ForeignKey(Application)
    NewName = models.CharField(max_length=200)


    


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
    def __unicode__(self):
        return self.Name_Person

class Application(models.Model):
    ApplicationNumber = models.CharField(max_length=200)
    ApplicationDate = models.DateField(max_length=200)
    IDApplicant = models.ForeignKey(Person)
    Act = models.CharField(max_length=200)
    def __unicode__(self):
        return self.ApplicationNumber

class Marriage(models.Model):
    IDApplication = models.ForeignKey(Application)
    IDFiance = models.ForeignKey(Person, related_name='Fiance')
    IDFiancee = models.ForeignKey(Person, related_name='Fiancee')
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
    IDFather = models.ForeignKey(Person, related_name='Father')
    IDMother = models.ForeignKey(Person, related_name='Mother')
    CertificateSerialNumber = models.CharField(max_length=200)

class ChangeName(models.Model):
    IDApplication = models.ForeignKey(Application)
    NewName = models.CharField(max_length=200)


    


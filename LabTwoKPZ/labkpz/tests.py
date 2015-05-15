from django.test import TestCase
from django.core.exceptions import ObjectDoesNotExist
from models import Person, Application, Marriage, Burn, Die, ChangeName

class PersonTestCase(TestCase):
    def setUp(self):
        self.per = Person.objects.create(Name_Person="Name", Citizenship="Citizen", SerialNumberPassport="CT11111", Adress="Kiev", Birthday="1996-02-02", BurnPlace="Kiev", IssueBy="By", DateOfIssue="2015-02-02")
        self.per1 = Person.objects.create(Name_Person="Name2", Citizenship="Citizen1", SerialNumberPassport="CT111111", Adress="Kiev1", Birthday="1996-02-02", BurnPlace="Kiev1", IssueBy="By1", DateOfIssue="2015-02-02")
        self.app = Application.objects.create(ApplicationNumber="000020", ApplicationDate="2015-02-12", IDApplicant=self.per, Act="Burn")
        self.burn = Burn.objects.create(IDApplication=self.app, NamePerson='Shevchuk Dmitriy', BurnDate='2020-02-28', BurnPlace='Kiev', LiveStillBurn=1, IDFather=self.per, IDMother=self.per1, CertificateSerialNumber='000012')

    def test_insert(self):
        self.assertEqual(self.per.hello(), 'Hi, Name')

    def test_update(self):
        self.per.Name_Person = "Name1"
        self.per.save()
        self.per2 = Person.objects.get(Name_Person="Name1")
        self.assertEqual(self.per, self.per2)

    def test_select(self):
        per1 = Person.objects.get(Name_Person="Name")
        self.assertEqual(per1.hello(), 'Hi, Name')

    def delete(self):
        self.per.delete()
        try:
            self.per2 = Person.objects.get(Name_Person="Name")
        except ObjectDoesNotExist:
            self.assertEqual(self.per, None)

    def test_cascade(self):
        self.burn.delete()
        self.assertIsNotNone(self.per.pk)
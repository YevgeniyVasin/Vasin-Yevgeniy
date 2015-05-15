from django.forms import ModelForm
from models import Person, Application, Burn, Marriage, Die, ChangeName

class AddPerson(ModelForm):
    class Meta:
        model = Person
        fields = ("Name_Person", "Citizenship", "SerialNumberPassport", "Adress", "Birthday", "BurnPlace", "IssueBy", "DateOfIssue")

class AddApplication(ModelForm):
    class Meta:
        model = Application
        fields = ("ApplicationNumber", "IDApplicant", "ApplicationDate", "Act")

class AddBurn(ModelForm):
    class Meta:
        model = Burn
        fields = ("IDApplication", "NamePerson", "BurnDate", "BurnPlace", "LiveStillBurn", "IDFather", "IDMother", "CertificateSerialNumber")

class AddMarig(ModelForm):
    class Meta:
        model = Marriage
        fields = ("IDApplication", "IDFiance", "IDFiancee", "OldSurnameM", "NewSurnameM", "OldSurnameW", "NewSurnameW", "Organization", "CertificateSerialNumber")

class AddDie(ModelForm):
    class Meta:
        model = Die
        fields = ("IDApplication", "IDPerson", "DieDate", "DiePlace", "DieReason", "CertificateSerialNumber")

class AddChang(ModelForm):
    class Meta:
        model = ChangeName
        fields = ("IDApplication", "NewName")

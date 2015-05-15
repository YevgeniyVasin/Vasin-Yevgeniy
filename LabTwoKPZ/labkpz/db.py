import json
from models import Person, Application, Marriage, Die, Burn, ChangeName

class DBWork:

    def getfreeid(self):
        res = Person.objects.all()
        if len(res) == 0:
            return 1
        else:
            return res[len(res)-1].pk+1

    def read_json(self):
        self.clean_db()
        with open('new.json') as f:
            for line in f:
                if line == None:
                    break
                line = json.loads(line)
                if type(line) == list:
                    self.insert_raws(line)

    def insert_raws(self, line):
            db_insert = Person(Name_Person=line[0], Citizenship=line[1], SerialNumberPassport=line[2], Adress=line[3], Birthday=line[4], BurnPlace=line[5], IssueBy=line[6], DateOfIssue=line[7])
            db_insert.pk = self.getfreeid()
            db_insert.save()


    def clean_db(self):
        Application.objects.all().delete()
        Burn.objects.all().delete()
        Marriage.objects.all().delete()
        ChangeName.objects.all().delete()
        Die.objects.all().delete()
        Person.objects.all().delete()



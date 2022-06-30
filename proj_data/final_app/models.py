from django.db import models

# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name

class Wings(models.Model):
    name=models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name

class Role(models.Model):
    name=models.CharField(max_length=100,null=False)

    def __str__(self):
        return self.name


class Studentbody(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100)
    dept=models.ForeignKey(Department,on_delete=models.CASCADE)
    role=models.ForeignKey(Role,on_delete=models.CASCADE)
    wing = models.ForeignKey(Wings, on_delete=models.CASCADE)
    phone=models.IntegerField(default=0)
    #email=models.CharField(max_length=100, null=False)
    #hire_date=models.DateField()
    def __str__(self):
        return "%s %s %s" %(self.first_name,self.last_name,self.phone)

class Equipement(models.Model):
    name=models.CharField(max_length=100, null=False)
    description=models.CharField(max_length=250)
    is_available=models.BooleanField(default=True)
    def __str__(self):
        return "%s %s" %(self.name,self.description)



class Equipment_user(models.Model):
    issue_reason=models.CharField(max_length=250, null=False)
    user = models.ForeignKey(Studentbody, on_delete=models.CASCADE)
    equip=models.ForeignKey(Equipement,on_delete=models.CASCADE)
    wing = models.ForeignKey(Wings, on_delete=models.CASCADE,null=True,blank=True)

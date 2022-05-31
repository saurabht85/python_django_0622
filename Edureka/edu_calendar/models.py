from django.db import models


class Student(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.firstname + " " + self.lastname

    def get_absolute_url(self):
        return "%i/" % self.id


class Venue(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=12)

    def __str__(self):
        return self.name


class Trainer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    venue = models.ForeignKey(Venue, on_delete=models.DO_NOTHING)
    trainer = models.ForeignKey(Trainer, on_delete=models.DO_NOTHING)
    students = models.ManyToManyField(Student)
    description = models.TextField()

    def __str__(self):
        return self.name
from django.db import models

# Create your models here.
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	
# each model is represented by a class that subclasses django.db.models.Model
# each model has class variables, each of which represents a database field in the model
# each field is an instance of the Field class (CharField, DateTimeField, etc.)
# data base uses the field names in the database as the column name
# some Field classes have required arguments: CharField requires max_length
# Field can also have optional arguments
# A relationship is defined using ForeignKey: Choice is related to a single Question
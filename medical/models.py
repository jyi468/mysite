from django.db import models

# Create your models here.

class MedicalInfo(models.Model):
	license_title = models.CharField(max_length=200)
	maintainer = models.CharField(max_length=200)
	private = models.BooleanField()
	maintainer_email = models.EmailField()
	num_tags = models.IntegerField()
	# id is primary key that can be auto generated
	metadata_created = models.DateTimeField()
	license = models.CharField(max_length=200)
	metadata_modified = models.DateTimeField()
	author = models.CharField(max_length=200)
	author_email = models.EmailField()
	state = models.CharField(max_length=200)
	version = models.CharField(max_length=200)
	license_id = models.CharField(max_length=200)
	type = models.CharField(max_length=200)
	ratings_count = models.IntegerField()
	title = models.CharField(max_length=200)
	revision_id = models.CharField(max_length=200)
	num_resources = models.IntegerField()
	organization = models.CharField(max_length=200)
	name = models.CharField(max_length=200)
	isopen = models.BooleanField()
	notes_rendered = models.TextField()
	ckan_url = models.URLField(max_length=200)
	notes = models.TextField()
	owner_org = models.CharField(max_length=200)
	
	

class Relationships(models.Model):
	medical_info = models.ForeignKey(MedicalInfo)

class Resources(models.Model):
	resource_group_id = models.CharField(max_length=200)
	cache_last_updated = models.DateTimeField()
	# id is primary key that can be auto generated
	size = models.CharField(max_length=200)
	last_modified = models.DateTimeField()
	hash = models.CharField(max_length=200, blank=True)
	description = models.CharField(max_length=200, blank=True)
	format = models.CharField(max_length=200)
	mimetype_inner = models.CharField(max_length=200)
	cache_url = models.URLField(max_length=200)
	webstore_url = models.URLField(max_length=200)
	position = models.IntegerField()
	resource_type = models.CharField(max_length=200)
	ratings_count = models.IntegerField()
	title = models.CharField(max_length=200)
	

class Tags(models.Model):
	medical_info = models.ForeignKey(MedicalInfo)
	tags = models.CharField(max_length=200)
	
class TrackingSummary(models.Model):
	medical_info = models.ForeignKey(MedicalInfo)
	total = models.IntegerField()
	recent = models.IntegerField()
	
class Groups(models.Model):
	tracking_summary = models.ForeignKey(TrackingSummary)
	groups = models.CharField(max_length=200)
	def __str__(self):
		return self.groups

class Extras(models.Model):
	medical_info = models.ForeignKey(MedicalInfo)
	coverage_period_start = models.DateTimeField()
	unit_of_analysis = models.CharField(max_length=200)
	hd2_workflow_id = models.IntegerField()
	agency = models.CharField(max_length=200)
	bureau_code =models.CharField(max_length=200)
	geographic_granularity = models.CharField(max_length=200)
	technical_documentation = models.URLField(max_length=200)
	collection_frequency = models.CharField(max_length=200)
	agency_program_url = models.URLField(max_length=200)
	date_updated = models.DateTimeField()
	date_released = models.DateTimeField()
	author_id = models.URLField(max_length=200)
	migration_notes_json = models.TextField()
	subject_area_1 = models.CharField(max_length=200)
	
	
	

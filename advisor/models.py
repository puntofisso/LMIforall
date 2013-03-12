from __future__ import unicode_literals

from django.db import models

class Courses(models.Model):
    id = models.IntegerField(primary_key=True)
    provider = models.CharField(max_length=100L, blank=True)
    title = models.CharField(max_length=250L, blank=True)
    jacs_code = models.CharField(max_length=10L, blank=True)
    url = models.CharField(max_length=250L, blank=True)
    class Meta:
        db_table = 'courses'

class JacsCodes(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=10L)
    name = models.CharField(max_length=100L)
    description = models.CharField(max_length=250L, blank=True)
    class Meta:
        db_table = 'jacs_codes'

class Onetskills(models.Model):
    name = models.CharField(max_length=11L, primary_key=True)
    description = models.CharField(max_length=100L, blank=True)
    class Meta:
        db_table = 'onetskills'

class Socs(models.Model):
    code = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255L, blank=True)
    description = models.TextField(blank=True)
    tasks = models.TextField(blank=True)
    qualifications = models.TextField(blank=True)
    class Meta:
        db_table = 'socs'

class SocsSkills(models.Model):
    code = models.IntegerField()
    skill_name = models.CharField(max_length=11L)
    skill_importance = models.FloatField(null=True, blank=True)
    skill_importance_rank = models.IntegerField(null=True, blank=True)
    skill_level = models.FloatField(null=True, blank=True)
    skill_level_rank = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'socs_skills'

# -*- coding:utf-8 -*-
from django.db import models

AUDIENCE_TYPES = (
	(0, u"Половые"),
	(1, u"Профессиональные"),
	(2, u"Возрастные"),
	(3, u"Другие"),
)

class AudienceType(models.Model):
	name = models.CharField(max_length=200)
	type_of = models.ChoiceField(choices=AUDIENCE_TYPES)

	def __unicode__(self):
		return u"%s (%s)" % (self.name, AUDIENCE_TYPES[self.type_of][1])

class SiteAim(models.Model):
	name = models.CharField(max_length=200)
	desc = models.TextField(blank=True, null=True)

class SiteTask(models.Model):
	name = models.CharField(max_length=200)
	desc = models.TextField(blank=True, null=True)

class SiteType(models.Model):
	name = models.CharField(max_length=200)
	desc = models.TextField(blank=True, null=True)

class SiteLanguage(models.Model):
	name = models.CharField(max_length=200)

class SiteAccent(models.Model):
	name = models.CharField(max_length=200)
	desc = models.TextField(blank=True, null=True)

class ScreenResolution(models.Model):
	width = models.IntegerField()
	height = models.IntegerField()

	def __unicode__(self):
		return u"%sx%s" % (self.width, self.height)

class Brief(models.Model):

	contact_name = models.CharField(max_length=50)
	contact_phone = models.CharField(max_length=20)
	contact_email = models.EmailField()
	contact_city = models.CharField()
	contact_address = models.TextField()

	project_name = models.CharField(max_length=150)
	sphere = models.TextField()

	contact_site = models.URLField(blank=True, null=True)
	contact_domain_name = models.URLField(u"Планируемый адрес сайта", blank=True, null=True)

	created_date = models.DateTimeField(auto_now_add=True)
	deadline_date = models.DateField()

	deadline_info = models.TextField(
					u"Внешние обстоятельства, влияющие на сроки",
					help_text=u"Например: PR-компания, выставка, ежегодный отчет и т.д.",
					blank=True, null=True)

	marketing_events = models.TextField(
					u"Какие маркетинговые мероприятия для продвижения компании или бренда уже проводились?",
					blank=True, null=True)

	target_audience = models.ManyToManyField(AudienceType)
	target_audience_other = models.CharField(max_length=200)

	products_and_services = models.TextField(blank=True, null=True)

	advantage = models.TextField(blank=True, null=True)

	site_aims = models.ManyToManyField(SiteAim)
	site_tasks = models.ManyToManyField(SiteTask)

	brand = models.BooleanField(default=False)
	brand_curves = models.BooleanField(default=False)
	brand_logo = models.BooleanField(default=False)
	brand_logo_curves = models.BooleanField(default=False)
	brand_characters = models.BooleanField(default=False)
	brand_characters_curves = models.BooleanField(default=False)
	brand_colors = models.CharField(max_length=200)

	site_type = models.ForeignKey(SiteType)
	site_type_other = models.CharField(max_length=200)

	site_languages = models.ManyToManyField(SiteLanguage)
	site_accent = models.ManyToManyField(SiteAccent)

	screen_resolution = models.ManyToManyField(ScreenResolution)


class Competitor(models.Model):
	brief = models.ForeignKey(Brief)
	name = models.CharField(max_length=200)
	site = models.URLField(blank=True, null=True)

	def __unicode__(self):
		return u"%s: %s" % (self.brief.project_name, self.name)


class Companion(models.Model):
	brief = models.ForeignKey(Brief)
	name = models.CharField(max_length=200)
	site = models.URLField(blank=True, null=True)

	def __unicode__(self):
		return u"%s: %s" % (self.brief.project_name, self.name)


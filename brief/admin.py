from brief.models import *
from django.contrib import admin

class CompanionInline(admin.StackedInline):
	model = Companion
	extra = 5

class CompetitorInline(admin.StackedInline):
	model = Competitor
	extra = 5

class LikedSiteInline(admin.StackedInline):
	model = LikedSite
	extra = 5

class BriefAdmin(admin.ModelAdmin):
	inlines = [CompanionInline, CompetitorInline, LikedSiteInline]

admin.site.register(Brief, BriefAdmin)
admin.site.register(AudienceType)
admin.site.register(SiteAim)
admin.site.register(SiteTask)
admin.site.register(SiteType)
admin.site.register(SiteLanguage)
admin.site.register(SiteAccent)
admin.site.register(ScreenResolution)
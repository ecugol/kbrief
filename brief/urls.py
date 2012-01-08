from django.conf.urls.defaults import patterns, include, url
from brief.forms import BriefForm1, BriefForm2
from brief.views import BriefWizard

urlpatterns = patterns('',
    url(r'^wizard', BriefWizard([BriefForm1, BriefForm2])),
)
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('brief.views',
	url(r'$', 'index', name='brief-index'),
)
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pagetest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'frontend.views.index'),
    url(r'^analizar/', include('frontend.urls')),
)

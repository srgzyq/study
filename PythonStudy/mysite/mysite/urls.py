from django.conf.urls import patterns, include, url
from django.contrib import admin
from mysite.views import hello,current_datetime,hours_ahead,display_meta
from mysite.books import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$',hello),
    url(r'^time/$',current_datetime),
    url(r'^meta/$',display_meta),
    url(r'^time/plus/(\d{1,2})/$',hours_ahead),
    url(r'^search-form/$',views.search_form),
    url(r'^search/$',views.search),
    url(r'^contact/$',views.contact),
)

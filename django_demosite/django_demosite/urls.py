from django.conf.urls import patterns, include, url
# from article.views import HelloTemplate

from django.contrib import admin
admin.autodiscover()

from django_demosite.forms import ContactForm1, ContactForm2, ContactForm3
from django_demosite.views import ContactWizard

urlpatterns = patterns('',
	(r'^articles/', include('article.urls')),
	
    # Examples:
    # url(r'^$', 'django_demosite.views.home', name='home'),
    # url(r'^hello/$', 'article.views.hello'),
    # url(r'^hello_template/$', 'article.views.hello_template'),
    # url(r'^hello_class_view/$', HelloTemplate.as_view()),

    url(r'^admin/', include(admin.site.urls)),

    # user auth urls
    url(r'^accounts/login/$', 'django_demosite.views.login'),
    url(r'^accounts/auth/$', 'django_demosite.views.auth_view'),
    url(r'^accounts/logout/$', 'django_demosite.views.logout'),
    url(r'^accounts/loggedin/$', 'django_demosite.views.loggedin'),
    url(r'^accounts/invalid/$', 'django_demosite.views.invalid_login'),

    # registration
    url(r'^accounts/register/$', 'django_demosite.views.register_user'),
    url(r'^accounts/register_success/$', 'django_demosite.views.register_success'),

    # contact forms
    url(r'^contact/$', ContactWizard.as_view([ContactForm1, ContactForm2, ContactForm3])),


)

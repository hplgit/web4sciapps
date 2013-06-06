from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^hw1/', 'django_apps.hw1.views.index'),
    url(r'^hw2/', 'django_apps.hw2.views.index'),
    url(r'^vib1/', 'django_apps.vib1.views.index'),
    url(r'^vib2/', 'django_apps.vib2.views.index'),
)

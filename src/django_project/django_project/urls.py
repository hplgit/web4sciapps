from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^hw1/', 'hw1_django.views.index'),
    url(r'^hw2/', 'hw2_django.views.index'),
    url(r'^vib1/', 'vib1_django.views.index'),
    url(r'^vib2/', 'vib2_django.views.index'),
)

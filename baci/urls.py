from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from training.views import handle_page_not_found_404

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'newdj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^training/', include('training.urls', namespace="training")),
    url(r'^', include('login.urls', namespace="login")),


)
handler404 = handle_page_not_found_404
handler500 = handle_page_not_found_404
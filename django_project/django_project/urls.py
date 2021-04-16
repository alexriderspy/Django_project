from django.contrib import admin
from django.conf.urls import include,url
#helps us include all our files

urlpatterns = [
    
    url(r'^admin/', admin.site.urls),
    url(r'^music/', include('music.urls')),
]

from django.contrib import admin
from django.urls import include, re_path

from adminactions import actions

admin.autodiscover()
actions.add_to_site(admin.site)

urlpatterns = (
    re_path(r'admin/', admin.site.urls),
    re_path(r'as/', include('adminactions.urls')),
    re_path(r'', admin.site.urls),
)

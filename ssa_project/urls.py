from django.contrib import admin
from django.urls import include, path #path to the admin usability in backend

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(("users.urls", "users"), namespace="users")), #route to users app (what is searched)
	path('chipin/', include(("chipin.urls", "chipin"), namespace="chipin")), #route to chipin app (what is searched)
]

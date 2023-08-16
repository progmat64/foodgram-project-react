from django.urls import include, path

urlpatterns = [
    path("api/auth/", include("djoser.urls.authtoken")),
    path("api/", include("djoser.urls")),
]

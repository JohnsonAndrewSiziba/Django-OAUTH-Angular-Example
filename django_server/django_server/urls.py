from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include('microblog.urls')),  # add this
    path(r'api-token-auth/', obtain_jwt_token),
    path(r'api-token-refresh/', refresh_jwt_token),
]

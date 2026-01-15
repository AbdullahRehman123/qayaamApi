from django.urls import re_path, include 
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Qayaam API",
        default_version='v1',
        description="API documentation for Qayaam project",
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include('listings.urls')),
    re_path(r'^', include('listingsFeedback.urls')),
    re_path(r'^', include('tenantsFeedback.urls')),
    re_path(r'^', include('booking.urls')),
    re_path(r'^', include('accounts.urls')),
    path('swagger/schema', schema_view.with_ui('swagger', cache_timeout=0), name='schema-json'),
]
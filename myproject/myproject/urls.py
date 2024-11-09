from django.contrib import admin
from django.urls import path
from myapp.views import upload_file, home  # Import the home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Redirect to the upload page
    path('upload/', upload_file, name='upload_file'),
]

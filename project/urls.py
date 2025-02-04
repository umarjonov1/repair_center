from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('about', TemplateView.as_view(template_name='about.html'), name='about'),
    path('service', TemplateView.as_view(template_name='service.html'), name="service"),
    path('users/', include('users.urls')),
    path('repairs/', include('repairs.urls'), name="repairs"),
]

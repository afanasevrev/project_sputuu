
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('materials/', views.materials_list, name='materials_list'),
    path('materials/<int:id>/', views.material_detail, name='material_detail'),
    path('homework/', views.homework_list, name='homework_list'),
    path('homework/<int:id>/upload/', views.homework_upload, name='homework_upload'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
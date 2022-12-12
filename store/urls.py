from django.conf.urls.static import static
from school import settings
from . import views
from django.urls import path

urlpatterns = [
    path('',views.content,name='content'),
    path('Register', views.Register, name='register'),
    path('Login', views.Login, name='login'),
    path('Logout', views.Logout, name='logout'),
    path('Newpg',views.detailspg,name='newpg'),
    path('person/add/', views.gform_create, name='add'),
    path('person/<int:pk>/', views.update_person, name='change'),
    path('person/ajax/update_course/', views.update_course, name='ajax_update_course'),  # AJAX
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

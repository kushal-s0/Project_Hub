from django.contrib import admin
from django.urls import path,include
from student import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'student' 

urlpatterns = [
    path('',views.homePage,name='Homepage'),
    
    path('search/',views.search,name = 'Search'),
    path('resources/',views.resources,name = 'Resources'),
    
    path('homepage/file/',views.group_file,name = 'File'),
    path('homepage/groups/',views.group_groups,name = 'Groups'),
    
    # path('upload/',views.code,name = 'code'),
    # path('upload/document/', views.document_view, name='document'),
    # path('upload/additional/', views.additional_view, name='additional'),
    # path('upload/database/', views.database_view, name='database'),
    # path('upload/view/', views.view_files, name='view'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from .views import upload_file, view_files, edit_file

urlpatterns = [
    path('upload/<str:file_type>/', upload_file, name='upload_file'),
    path('files/<str:file_type>/', view_files, name='view_files'),
    path('edit/<str:file_type>/<int:file_id>/', edit_file, name='edit_file'),
]

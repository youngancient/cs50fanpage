from django.urls import path
from .views import index_view ,comments, cswall, gallery, alumni_view, json_view

app_name = 'home'
urlpatterns = [
    path('', index_view,name='index'),
    path('comments', comments,name='comments'),
    path('cswall', cswall,name='cswall'),
    path('gallery', gallery,name='gallery'),
    path('total_alumni', alumni_view),
    path('all_json', json_view),
]

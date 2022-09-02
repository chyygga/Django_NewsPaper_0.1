from django.urls import path
from .views import *

urlpatterns = [
    path('', NewsHome.as_view(), name='home'),
    path('add/', AddPost.as_view(), name='add'),
    path('search/', NewsSearch.as_view(), name='search'),
    path('<int:pk>/', NewsDetail.as_view(), name='index'),
    path('<int:pk>/edit/', NewsUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete', NewsDelete.as_view(), name='post_delete'),
    path('<int:pk>/sub/', SubMe.as_view(), name='sub'),
]

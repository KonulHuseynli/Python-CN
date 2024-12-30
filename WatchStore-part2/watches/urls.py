from django.urls import path

from watches import views as wacthes_views


urlpatterns=[
    path('',wacthes_views.all_watches,name = 'all_watches'),  #127.0.0.1:8000/watches/
    path('create/',wacthes_views.create_watch, name = 'create_watch'), #127.0.0.1:8000/watches/create
    path('detail/<int:pk>',wacthes_views.detail_watch, name = 'detail_watch'), #127.0.0.1:8000/watches/detail
    path('update/<int:pk>',wacthes_views.update_watch, name = 'update_watch'), #127.0.0.1:8000/watches/update
    path('delete/<int:pk>',wacthes_views.delete_watch, name = 'delete_watch'), #127.0.0.1:8000/watches/delete
]
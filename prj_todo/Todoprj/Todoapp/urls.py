from django.urls import path, include

from Todoapp import views

urlpatterns = [
    # path('',views.add,name='add'),
    # path('delete/<int:taskid>/', views.delete, name='delete'),
    # path('update/<int:id>/', views.update, name='update'),

    path('home/',views.TaskView.as_view(),name='home'),
    path('detail/<int:pk>/',views.TaskDetail.as_view(),name='detail'),
    path('update/<int:pk>/',views.TaskUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',views.TaskDelete.as_view(),name='delete'),
]
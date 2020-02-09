from django.urls import path
from .views import register, login,home, task_edit,task_delete, filter_period_view,logout   

urlpatterns =[
    path("register/", register, name='register'),
    path('', login, name='login'),
    path('logout/', logout, name='logout' ),
    path('home/', home, name='home'),
    path('task/edit/<int:id>', task_edit, name='task_edit' ),
    path('task/delete/<int:id>', task_delete, name='task_delete'),
    path('task/<str:slug>', filter_period_view, name='filter-period'),
]
from django.urls import path,include
from . import views
urlpatterns = [
    path('stuinfo/<int:pk>',views.student_detail),
    path('stulist/',views.student_list),
]
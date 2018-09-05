from django.urls import path

# from face_traking.urls import urlpatterns
# from face_traking.urls import urlpatterns

from . import views

app_name = 'process'

urlpatterns = {
    path('process/', views.index, name = 'process'),
    path('process/<int:user_id>', views.show, name = 'destroy'),
}
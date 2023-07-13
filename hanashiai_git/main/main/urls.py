from django.contrib import admin
from django.urls import path
#from hanashiai_web import views
from hanashiai_web.views import Homepage 
from hanashiai_web.views import Submit_post 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Homepage.as_view(), name="homepage"),
    path('submit_post/', Submit_post.as_view(), name="submit_post"),
]

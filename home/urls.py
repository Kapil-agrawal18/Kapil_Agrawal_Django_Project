from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name='home'),
    path("index_2", views.index_2, name='index_2'),
    path("about", views.about, name='about'),
    path("help", views.help, name='help'),
    path("login", views.login, name='login'),
    path("items", views.items, name='items'),
    path("checkout", views.checkout, name='checkout'),
    path("product/<int:myid>", views.productView, name='ProductView'),
    path("Category", views.category, name="Category"),
    path("category/furnishing", views.category_furnishing, name="furnishing"),
    path("category/Lighting", views.category_lighting, name="category_lighting"),
    path("category/Walls_&_Floor", views.category_wf,
         name="category_Walls_Floor"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

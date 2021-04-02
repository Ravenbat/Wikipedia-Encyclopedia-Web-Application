from django.urls import path
from . import util


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<entryname>", views.title, name="title"),
    path("wiki/search/", views.search, name='search'),
    path("wiki/search/<entryname>", views.title),
    path("wiki/create/", views.create, name="create"),
    path("wiki/", views.save, name="save"),
    path("wiki/r/", views.random_page, name="randompage"),
    path("wiki/edit/<title>", views.edit_entry, name="editEntry"),
    path("wiki/update/<titlee>", views.update_entry, name="updateEntry")
]

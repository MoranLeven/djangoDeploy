from django.urls import path
from .views import crudOpsHome, createUser, readUser, updateUser, deleteUser, getDataById
urlpatterns =[
    path("",crudOpsHome,name="home"),
    path("create",createUser,name="create"),
    path("read",readUser.as_view(),name="read"),
    path("update",updateUser,name="update"),
    path("delete",deleteUser,name="delete"),
    path("get/<id>/",getDataById,)
]
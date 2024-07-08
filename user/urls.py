from django.urls import path
from user import views as VIEW_USER

urlpatterns = [
    path('get-usertype/', VIEW_USER.getUsertype, name='get-usertype'),
    path('add-usertype/', VIEW_USER.addUsertype, name='add-usertype'),
    path('update-usertype/<int:usertypeid>', VIEW_USER.updateUsertype, name='update-usertype'),
    path('delete-usertype/<int:usertypeid>', VIEW_USER.deleteUsertype, name='delete-usertype'),
    
    
    path('get-user/', VIEW_USER.getUser, name='get-user'),
    path('add-user/', VIEW_USER.addUser, name='add-user'),
]

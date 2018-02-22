from django.conf.urls import url
from pswdApp import views

# TEMPLATE URLS!

app_name = 'display'

urlpatterns=[
	url(r'^register/$',views.register,name='register'),
	url(r'^user_login/$',views.user_login,name='user_login'),
]
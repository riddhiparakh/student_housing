from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
urlpatterns = [
   
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('search/',views.search,name='search'),
    path('house/',views.room_property,name='house'),
    # path('api/',views.api_room,name='api'),
    path('host/',views.host,name='host'),
    path('addproperty/',views.AddProperty,name='addproperty'),
    path('propertydetail/<str:room>/',views.Propertydetail,name='detail'),
    path('updateproperty/<str:id>/',views.Propertyupdate,name='update'),
    path('deleteproperty/<str:id>/',views.PropertyDelete,name='delete'),
    path('booknow/',views.booknow,name='booknow'),
    path('fav/',views.fav,name='fav'),
    path('share/',views.share,name='share'),
    
    path('reset_password/',auth_views.PasswordResetView.as_view(),name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="account/password_reset_done.html"),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset_password/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('getdata/',views.getData),
    path('setting/',views.setting,name='setting'),
    
    
    
    
    
    

    
    
    
    
    
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
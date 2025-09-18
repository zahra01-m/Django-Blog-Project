from.import views
from django.urls import path

urlpatterns = [
    path("",views.StartingPageView.as_view(),name="home"),
    path("signup/",views.signup,name="signup"),
    path("login/",views.login,name="login"),
    path("post/",views.AllPostView.as_view(),name="Post"),
    path("post/<slug:slug>/",views.SinglePostView.as_view(), name="detail_post"),
    path("read-later",views.ReadLaterView.as_view(),name="read-later")

]

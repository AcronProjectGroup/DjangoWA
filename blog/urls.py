from django.urls import path
from . import views


urlpatterns =[
    path('', views.BlogView.as_view(), name="blog"),
    path('<int:pk>', views.BlogDetailView.as_view(), name="blog_detail_view"),
    path('new/', views.NewPostBlog.as_view(), name="post_new_post"),
    path('<int:pk>/update/', views.UpdatePostBlog.as_view(), name="update_post"),
    path('<int:pk>/delete/', views.DeletePostBlog.as_view(), name="delete_post"),
]


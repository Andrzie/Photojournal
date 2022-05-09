from django.urls import path
from photojournal.views import MainPageView, PostDetailView, blog_post_like

urlpatterns = [
    path('', MainPageView.as_view()),
    path('<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post-like/<int:pk>', blog_post_like, name="post_like"),
]
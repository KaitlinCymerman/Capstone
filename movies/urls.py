from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("movie/<int:movie_id>", views.movie, name="movie"),
    path("add_review/<int:movie_id>", views.add_review, name="add_review"),
    path("watchlist", views.displaywatchlist, name="watchlist"),
    path("add/<int:movie_id>", views.add, name="add"),
    path("remove/<int:movie_id>", views.remove, name="remove"),
    path("profile/<str:username>", views.profile, name="profile"),
    path("profile/<str:username>/reviews", views.user_reviews, name="user_reviews"),
    path("edit/<str:review_id>", views.edit, name="edit"),
    path("add_movie", views.add_movie, name="add_movie"),
]

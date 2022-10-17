from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from datetime import datetime

from .models import User, Movies, Reviews


def index(request):
    movies = Movies.objects.all()
    paginator = Paginator(movies, 4)
    page_number = request.GET.get('page')
    return render(request, "movies/index.html", {
        "movies": Movies.objects.filter,
        "page_obj": paginator.get_page(page_number)
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "movies/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "movies/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "movies/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "movies/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "movies/register.html")


def movie(request, movie_id):
    movie_data = Movies.objects.get(pk=movie_id)
    isMovie_InWatchList = request.user in movie_data.watchlist.all()
    allreviews = Reviews.objects.filter(movie=movie_data)
    return render(request, "movies/movie.html", {
        "movies": movie_data,
        "isMovie_InWatchList": isMovie_InWatchList,
        "allreviews": allreviews,
    })

def add_review(request, movie_id):
    #Allow users to write and add reviews
    user = request.user
    review = request.POST["new_reviews"]
    rating = request.POST['rating']
    movie_data = Movies.objects.get(pk=movie_id)
    new_reviews = Reviews(
        author=user,
        movie=movie_data,
        review=review,
        rating=rating
    )
    new_reviews.save()
    return HttpResponseRedirect(reverse("movie",args=(movie_id, )))


def displaywatchlist(request):
    #Watchlist displays all listings added to that page
    return render(request, "movies/watchlist.html",{
        "movies": request.user.watch_listing.all()
    })

def add(request, movie_id):
    #Add to watchlist
    movie_data = Movies.objects.get(pk=movie_id)
    user = request.user
    movie_data.watchlist.add(user)
    return HttpResponseRedirect(reverse("movie",args=(movie_id, )))

def remove(request, movie_id):
    #Remove from watchlist
    movie_data = Movies.objects.get(pk=movie_id)
    user = request.user
    movie_data.watchlist.remove(user)
    return HttpResponseRedirect(reverse("movie", args=(movie_id, )))


def profile(request, username):
    if request.method == "GET":
        requested_user = User.objects.get(username=username)
        isMovie_InWatchList = Movies.objects.filter()
        requested_user_reviews = Reviews.objects.filter(author=requested_user)
        return render(request, "movies/profile.html", {
            "requested_user": requested_user,
            "isMovie_InWatchList": isMovie_InWatchList,
            "reviews": requested_user_reviews[:5],
        })


def user_reviews(request, username):
    if request.method == "GET":
        requested_user = User.objects.get(username=username)
        # Gets all reviews from user
        user_reviews = Reviews.objects.filter(author=requested_user)
        return render(request, "movies/user_reviews.html", {
            "requested_user": requested_user,
            "reviews": user_reviews
        })


@csrf_exempt
def edit(request, review_id):
    review = Reviews.objects.get(pk=review_id)
    # Allow users to edit reviews
    if request.method == "PUT":
        data = json.loads(request.body)
        data.get("review")
        reviews.review = data["review"]
        review.save()
        return HttpResponse(status=204)

def add_movie(request):
    if request.method == "POST":
        title = request.POST["title"]
        year = request.POST["year"]
        image = request.POST["image"]
        about = request.POST["about"]
        # Attempt to save new movie entry
        try:
            movie = Movies(title=title, year=year, image=image, about=about)
            movie.save()
        except ValueError:
            return render(request, "movies/add_movie.html", status=500)

        return render(request, "movies/add_movie.html")

    return render(request, "movies/add_movie.html")




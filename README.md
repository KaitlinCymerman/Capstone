# CS50's Web Programming with Python and JavaScript Capstone

This is a project called Movie Mayhem. This is an app where people can find movies, create lists, review, and rate movies. I love watching movies and dicussing them so I wanted to create an app where you can review movies and all add movies to a list that you haven't seen yet.

To build this project, I used the languages and technologies I learned in this course. I used HTML, CSS, Bootstrap, JavaScript on the front end and used Python and Django on the backend.

This project features a responsive nagivation bar, movie listings, movie page, abability to review/rate movies, a profile page, and a add movie page.

# Layout-(Layout.html)

Using the layout, I created a navbar using Bootstap that can be seen for the entire website. On this navbar, I utlized navigation buttons that lead to each different page such as the profile, add new movie, list, all movies, regisiter, and the login/logout functions.

# Index page

In the index page, I included some content regarding this website. I also included movie cards that show which movie is on this app that you can review. I also included pragnaiton to go between pages.

# Register/Login/Logout

In the navbar, there is the login, logout, and register buttons. I used the standard authentication system used within Django authentication funcionalities.

# Movie Detail Page-(movie.html)

Displays movie information such as title, poster, and the synposis.

# Review/Rate

On the movie page, users are able to review and rate movies. They are able to provide a rating between 0-10 and write down their thoughts about the movie.

# User Profile

When the user clicks on their username on the navbar, the user profile page is displayed. On this page, users can go to their list and also see all their review they have made. Each review will allow users to click on the movie title and be taken back to that movie page. Users can click on all reviews which will take them to a seperate page that reveals all the reviews made on any movie. On this page, users can chose to edit any of their reviews.

# Add Movie

If there happens to be a movie that is not present on the app, users are able to add a new movie posting. Users will be able to fill out the movies title, year, poster image, and about syposis. Once submitted, it will be added to the all movies page.

# Distinctiveness and Complexity

I think that this project satisfies all the project requriements. Before starting this project, I thought of my own idea and wrote down different bullet points for what I wanted to have in this project. I think it's intersting in that you can look at movies already on the app but also add some that might not be popular to others while having the option to review and rate them.

Also, I think it's intersting as I used a lot the langauges that we learned during this course, however, it's different from other projects I have done. As I did this project from scratch as this time, there was no starter code provided, I did a lot of research of how to do things and even looked back on past lectures. I feel like I was able to implement different details. I had a lot of fun using what I've learned from this course.

# How to run this project

cd into the project directory

Run "python manage.py runserver" to run this project

# File and Directories Structure

- movies is the app where all required files are present
- movies/static contains CSS and JS for this project
- movies/templates contain all the HTML files for this project
- movies/views.py contains all the views
- movies/urls.py contains all the URL patterns
- movies/models.py contains all the models created for this project such as user, movies, and reviews.

# Demonstration on Youtube

For this project, you have to make a video showing your project: https://www.youtube.com/watch?v=WfBokxB300E

# Finally

Thanks to all the people for making [CS50's Web Programming with Python and JavaScript](https://www.edx.org/course/cs50s-web-programming-with-python-and-javascript) for us.

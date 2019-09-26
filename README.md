# Interest-Blog
This project contains the deep implementation of a blog cum photo sharing platform, designed to show off various features of the Django web framework. Used MongoDB as a backend database for this Django project, without changing the Django ORM by using Djongo API. Project is currently deployed on Heroku cloud service.<br />
Used Bootstrap CSS to make our project responsive, which can render excellently on multiple device sizes. A single website which runs on different device sizes such as on large desktop devices, laptop devices, tablet devices and on mobile devices.<br />
##### Link https://interestblog.herokuapp.com/login/
##### Version 2.0 Link: http://goplaybook-1.herokuapp.com/login/
---
### Prerequisites:
  * dj-database-url==0.5.0
  * Django==2.1.4
  * django-heroku==0.3.1
  * djongo==1.2.32
  * pillow==5.1.0
  * pymongo==3.7.2
  * MongoDB
---

Heroku is a cloud platform as a service supporting several programming languages.<br />
Because the Heroku does not grant unlimited dynos for a free account, any uploaded images will be lost when the dyno restarts. The entire project will be shifted to a paid account to add more persistence for posts in the later phase.

### Getting Started

The new user can register using [this link](https://interestblog.herokuapp.com/register/). For the primary phase of development, the registration process is kept pretty simple and will be made more authentic later.<br />
![Screenshot (62)](https://user-images.githubusercontent.com/42863227/58197209-67127d80-7ce9-11e9-8e3f-15d4e268ab13.png)

<br />

Once a user is registered, the user can log in using [this link](https://interestblog.herokuapp.com/login/) .
All the validation is taken care of so please be sure of the specific fields before logging in.<br />
![Screenshot (61)](https://user-images.githubusercontent.com/42863227/58197270-85787900-7ce9-11e9-91d8-88576f96d846.png)
<br />
<br />
<br />

Here we can have a view at users latest feeds and posts.
the structure of the blog is kept quite manageable and user-friendly.
<br />

### How do I run this project locally?
1. Clone the repository:<br />
`git clone https://github.com/RanaRauff/Interest-Blog.git`
2. Run migrations:<br />
`python manage.py migrate`
3. Create a user:<br />
`python manage.py createsuperuser`
4. Run the server:<br />
`python manage.py runserver`
5. And open 127.0.0.1:8000/login in your web browser.


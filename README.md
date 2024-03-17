# Filmofiles

Filmofiles is a film review app designed to encourage movie fans to come together and share their opinions. The app is targeted towards users who wish to contribute to and engage in discourse with other like-minded individuals: users can browse and select other users' contributions to read, and, having completed a simple registration process, can post comments as well as submit their own film reviews.<br>

<img src="README images/page-home.png">

The live link can be found here - [FILMOFILES](https://filmofiles-de31d62f91c0.herokuapp.com/)

## User Experience (UX)

### User Stories

#### Epic: General User Experience

* Browse film reviews<br>
As a User I can view a paginated list of film review posts in order to select one to view in full.<br>
AC1 - When a user clicks a 'Browse' link in the main page a list of contributed film reviews is displayed, newest first.<br>
AC2 - The user sees all film review posts with pagination.<br>

* Read a film review<br>
As a User I can click on a film review post in order to read the full content.<br>
AC1 - When a film review title is clicked, a new page opens displaying a full view of the film review.<br>

* View comments on a film review<br>
As a User I can view comments on a film review so that I can read and follow a conversation about films that interest me.<br>
AC1 - Given one or more user comments, the user can view them.<br>
AC2 - The user can click on the comment thread to read the conversation.<br>

* Register an account<br>
As a User I can register an account so that I can make contributions and therefore have an active role in the site.<br>
AC1 - Given a (valid) username and password, a user can register an account.<br>
AC2 - The user can log in.<br>
AC3 - Given a logged-in user, they can post a film review and/or leave a comment on a film review.<br>
AC4 - Given a logged in user, they can log out.<br>

#### Epic: Registered User Profile

* Contribute a film review<br>
As a Registered User I can submit a film review so that I can participate in the film review community.<br>
AC1 - Fields for completion: title, genre, year, director name, image.<br>
AC2 - When a registered user's film review is approved, it should be displayed to the site.<br>

* Contribute a comment<br>
As a Registered User I can leave comments on a film review so that I can contribute to a conversation.<br>
AC1 - When a user's comment is approved, it should be displayed below the review.<br>
AC2 - Users can reply to existing comments to continue the conversation.<br>
AC3 - If more than one comment is present, a threaded conversation is established.<br>

* Modify or delete my contributions<br>
As a Registered User I can edit and delete my film reviews and comments so that I can control my contributions, e.g. correct mistakes, embellish content and remove altogether.<br>
AC1 - Given a logged in user, they can edit their film reviews/comments.<br>
AC2 - Given a logged in user, they can delete their film reviews/comments.<br>

* View my profile page<br>
As a Registered User I can view a profile page that displays the film reviews and comments I have submitted so that I can keep track of my contributions.<br>
AC1 - A profile page opens when a relevant link is clicked.<br>
AC2 - Lists of "my film reviews" and "my comments" are displayed with items ordered newest first.<br>
AC3 - Items in the list are all clickable links to the relevant places/pages.<br>

#### EPIC: Site Administration

* Manage contributions as an Admin<br>
As an Admin I can create, read, update and delete film reviews and comments so that the site's content aligns with the vision of the site owner and maintains quality and relevance.<br>
AC1 - Admin can create film reviews and comments.<br>
AC2 - Admin can view all film reviews and comments, including pending and approved ones.<br>
AC3 - Admin can edit film reviews and comments.<br>
AC4 - Admin can delete film reviews and comments.<br>

* Control publication of content as an Admin<br>
As an Admin I can approve or disallow film reviews and comments so that I can responsibly manage the content.<br>
AC1 - Admin can approve film reviews and comments.<br>
AC2 - Admin can disallow film reviews and comments.<br>

#### User stories not yet implemented

The following user story was scoped out of the project due to time constraints:

* Search for film reviews<br>
As a User I can search for a film by title, genre, year and director so that I can read reviews of films of my choosing.<br>
AC1 - A search bar is displayed with an enter key.<br>
AC2 - The user can input a case-insensitive search criterion (title, genre, year, director name).<br>
AC3 - Upon submission, the database is queried and returns a list of film titles matching the submitted search criterion.<br>
AC4 - The list items are clickable links of film title and slug that open a full view of the film review.<br>
AC5 - If there is no match, an appropriate message is displayed.<br>


## Agile Methodology

The Projects functionality in Github was used to manage the process of creating the site using an Agile approach, with a kanban board for tracking the progress and completion of User Stories. Github Issues were created for each User Story with defined acceptance criteria to make the execution as straightforward as possible.


## Design

The site's design was based on supporting the theme and the experience of film-watching:

### Colour

The colour scheme could be described as deep and rich as it features a charcoal grey and a dark teal colour; accent colours are a vibrant orange-red, golden yellow and cornflower blue. The colours were chosen to emulate the sense of being in a cinema, with subdued lighting and heavy, plush velvet curtains and seats. There is therefore a strong contrast between the background colours and accents, and the bright red text headings have a background shadow effect, resembling artificial light in the darkness. Regular text is off-white. Pure white is used for enhancing contrast in the logo, the site's tagline ("Film review community and social network for film lovers"), all links on hover and form fields.<br><br>
<img src="README%20images/colours.png" height="50px">

### Imagery

A static image on the home page in monochrome depicts a view of an empty cinema from the perspective of a viewer looking towards the screen.<br><br>
<img src="README%20images/movie-theater-4609877_1920.webp" width="50%"><br><br>
In the review cards, a placeholder image of cinema tickets and a bag of popcorn furthers the association with the cinema-going experience to appeal to the Users and reinforce the theme of the site.<br><br>
<img src="README%20images/popcorn-898154_1280.webp" width="200px"><br><br>
The rest of the imagery is in the form of the individual film poster covers.<br><br>
<img src="README%20images/film-anatomy-of-a-fall.webp" width="180px">&nbsp;&nbsp;<img src="README%20images/film-inglourious-basterds.webp" width="180px">&nbsp;&nbsp;<img src="README%20images/film-the-village.webp" width="180px">

### Typography

The site uses just two fonts, imported from Google Fonts: Workbench for the Filmofiles logo and Montserrat for the remaining text. Workbench has a somewhat grainy character with horizontal streaks running through it, making the logo reminiscent of an old VHS label and thus tying in another medium of film-watching.<br><br>
<img src="README%20images/logo-nav-items.png">

### Favicon

From the initial letter of the logo, F, a favicon was created via favicon.io. This looks simple and bold, and will keep the name of the site and its related theme in visitors' vision and minds.<br><br>
<img src="README%20images/favicon.png">


## Data Models

This project follows Object-Oriented Programming principles and employs Django's Class-Based Generic Views. It includes three custom models: Film, representing film details (title, director, genre, year, image); Review, for film reviews with one-to-many relationships to the User & Film models and an implicit many-to-many relationship with the Comment model; and Comment with one-to-many relationships to User and Review models, which allows registered Users to post comments on reviews.

The database schema are illustrated by the ERD diagram below:<br><br>
<img src="README%20images/ERD.png">


## Features

This is a Film Review application where Users read and write reviews and view contributions from others. They can engage with the community by posting comments on reviews and joining a conversation.

- CRUD Functionality: registered Users have the freedom to create, read, update and delete all of their individual contributions to Filmofiles.
- Admin Panel: through the Django admin panel, Admin personnel have the control to manage User accounts and site content with the authority to approve Users' contributions for publishing and to remove content if necessary. Admins create Film objects for Users to review in order to maintain order and consistency and to prevent errors, keeping the database tidy.
- User Registration and Authentication: Users can sign up, log in and out, and manage their profiles securely.
- User Profiles: each registered User has a profile page displaying their submitted reviews and comments. Items waiting for approval are marked accordingly.

### Features to implement

- Responsive Design: the project is not yet optimised for smaller screens such as mobile devices.
- Search: the app would benefit greatly from the ability for Users to search the database for films, e.g. by title, genre, director.
- Filter: similarly, the addition of a filter system would be expected as the site and contents grow.
- User Profile: additions and improvements to the my_profile area would enhance the experience and appeal for Users. For example: the option to delete their account, to upload a profile picture, to change their username and password.
- Social Media: the site could be extended to work like a social media app whereby Users could add Likes and mark films and other Users as Favourites.
- Film objects: rather than inputting films to the database manually, this could be done using an API to automate the process, getting film data from sources like IMDb, for example. This would promote efficiency and accuracy, and allow for scalability and cost-effective operations.


### Header

<strong>Logo</strong>: a logo was created using the Workbench font from Google fonts. It is positioned in the top left of the navigation bar and is linked to the home page for ease of navigation for the User.<br><br>
<strong>Navigation bar</strong>: the navbar is present at the top of every page and displays all links to the other pages. On hover, these links become highlighted via a darkening of the background and a lightening of the text. The Account link is a dropdown menu which includes Sign Up and Log In. When the User is logged in, the dropdown menu links change to the My Profile and Log Out pages. Additionally, on medium screens and above, a line of text shows "Logged in as ((username))". On smaller screens, the navigation items reduce into a hamburger menu.<br><br>
<img src="README%20images/logo-nav-items.png">&nbsp;<img src="README%20images/navbar-logged-in.png">

### Footer

A simple footer was created to mirror the header style. It includes link icons to Instagram, Facebook and YouTube. These can be set up to open a separate browser tab to avoid leading the User away from the site.<br><br>
<img src="README%20images/footer.png">

### Home page

The homepage has a dramatic backdrop created by the image of the cinema interior. On top are textual headings and three cards which establish the colour scheme. The information in the cards lets the site visitors know what the application does and is for, in a short phrase with a filmroll icon from Font Awesome: first, the BROWSE card informs the User that they can navigate through published film reviews, with the word itself linking to the Browse page in case the User expects it; second, the READ card encourages the User to sample the content; and third, the JOIN card prompts the User to become fully involved and interact with other like-minded film fans - this word also functions as a link and will load the Sign Up page. Underneath the cards is a bright coloured button which means that signing up is only one click away and is easy for the User to navigate to.<br><br>
<img src="README%20images/page-home.png">

### Browse page

The next page is where all of the published (approved by the Admin) film reviews are stored, again in cards. Users can see a summary in the form of an image, either the film poster or a placeholder image of popcorn; the film's title, the review's slug, the review author's name, the date, and finally a READ button which links to the review_detail page for that particular review. The page has pagination and displays six review cards per page. The pagination links change from red to yellow on hover to show they are interactive elements.<br><br>
<img src="README%20images/page-browse.png">

### Add review page

This page presents a form in which Users can enter their review for submission. The fields include: Film (a dropdown menu which displays the film title and genre), Review content, slug (labelled as Tagline to be more user-friendly), Rating /10 (a dropdown) and finally a Submit button. Upon successful submission, an appropriate message appears.<br><br>
<img src="README%20images/page-submit_review.png">&nbsp;&nbsp;<img src="README%20images/page-submit_review2.png"><br>
<img src="README%20images/success-message-review-pending-approval.png">

### Sign Up and Log In pages

These pages both also present simple forms for their respective purposes. Upon successful signup, the homepage is loaded; upon successful login, the My Profile page. Both redirected pages steer the User towards establishing their next options.<br><br>
<img src="README%20images/page-sign_up.png">&nbsp;&nbsp;<img src="README%20images/page-log_in.png">

### My Profile page

This page displays all of the registered Users' contributions to the site - all reviews and comments. Each item, except those reviews not yet approved, can be edited and deleted here. The Edit and Delete buttons direct to appropriate pages and Users can confirm deletions before losing their content. Upon successful updates or deletions, relevant messages are displayed.<br><br>
<img src="README%20images/page-my_profile.png"><br>
<img src="README%20images/page-edit_comment.png"><br>
<img src="README%20images/page-confirm_delete_review.png"><br>
<img src="README%20images/success-message-edit-comment.png"><br>


## Testing

The Filmofiles application was subjected to manual testing in Google Chrome, Mozilla Firefox, Microsoft Edge and Safari browsers, and Samsung Internet and Safari on mobile.
Documentation can be found <a href="README%20images/Filmofiles%20testing.pdf">here</a>.


## Security

Django's built-in user authentication system is utilised to handle user registration, login, and profile management. The @login_required decorator ensures that certain views are accessible only to authenticated Users. The submission of forms relies on validated data and error messages are in place for missing or incorrect data. Cross-Site Request Forgery (CSRF) tokens are used on forms throughout this site. The database url and secret key are stored in the env.py file to prevent unwanted connections to the database. Custom Error Pages (400, 403, 404, 500) were created to provide information on any such error and include links to direct the User back to the site.


## Deployment - Heroku

To deploy this page to Heroku from its GitHub repository, the following steps were taken:
#### In IDE = begin the Setup:

1. SET UP THE DIRECTORY:<br>
i) Open a new workspace from a repository that uses the full CI template.<br>
ii) Install the Django Python package:<br>
	pip3 install Django~=4.2.1<br>
iii) Add Django to requirements.txt:<br>
	pip3 freeze --local > requirements.txt (Verify the installation.)<br>

2. CREATE A PROJECT:<br>
i) Create a Django project named "filmofiles":<br>
	django-admin startproject filmofiles .<br>
ii) Start the Django server:<br>
	python3 manage.py runserver<br>
iii) Copy the hostname from the browser following "Invalid HTTP_HOST header."<br>
iv) In my_project/settings.py, paste this hostname between the square brackets of ALLOWED_HOSTS and save.<br>
v) Refresh the browser to view a basic Django project.<br>
vi) Stop the server using ctrl+c in the terminal.<br>

3. CREATE AN APP:<br>
i) Create a Django app named "core":<br>
python3 manage.py startapp core (Verify the directory was created.)<br>
ii) Add this to the list of INSTALLED_APPS in settings.py:<br>
	'core',

#### JUMP to ElephantSQL:

4. Create a database:<br>
i) ElephantSQL Setup:<br>
	Create a new instance of PostgreSQL:<br>
	Set up the plan (name, tiny turtle plan, select region).<br>
	Verify PostgreSQL version (must be 12 or higher).<br>
	Copy the URL from the DETAILS section.<br>


#### JUMP back to IDE:

5. SETUP ENVIRONMENT VARIABLES AND SECRET KEY:<br>
i) Create a file named env.py at the top level of the project.<br>
ii) Add it to .gitignore.<br>
iii) Import os and set the secret_key:<br>
	import os<br>
	os.environ.setdefault("SECRET_KEY", "(value)")<br>
iv) Update settings.py to use the secret key:<br>
	SECRET_KEY = os.environ.get("SECRET_KEY")<br>

6. CONNECT DATABASE TO CODE in env & settings:<br>
i) Set DATABASE_URL in env.py using the ElephantSQL URL.<br>
ii) Install the 2 packages required to connect to your database:<br>
	pip3 install dj-database-url~=0.5 psycopg2~=2.9<br>
iii) Add them to requirements.txt:<br>
	pip3 freeze --local > requirements.txt<br>
iv) In settings.py, import the necessary packages:<br>
	import os<br>
	import dj_database_url<br>
v) And add underneath;<br>
	if os.path.isfile('env.py'):<br>
	    import env<br>
vi) Comment out the local SQlite3 database and add:<br>
	DATABASES = {<br>
	    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))<br>
	}
vii) Migrate database:<br>
	python3 manage.py migrate<br>

#### JUMP to HEROKU:

7. CREATE THE HEROKU APP:<br>
i) Visit your Heroku dashboard and create a new app with a unique name.<br>
ii) In the Settings tab, add a config var with key DISABLE_COLLECTSTATIC and value 1 to prevent static file uploads during the build.<br>
iii) Add the SECRET_KEY as a config var.<br>
iv) Add the DATABASE_URL as a config var.<br>
v) Remove Heroku's PostgreSQL DATABASE_URL if present.<br>

#### JUMP back to IDE:

8. UPDATE CODE FOR DEPLOYMENT:<br>
i) Install a production-ready web server for Heroku:<br>
	pip3 install gunicorn~=20.1<br>
ii) Add gunicorn==20.1.0 to requirements:<br>
	pip3 freeze --local > requirements.txt<br>
iii) Create a Procfile at the project's root and enter on line 1:<br>
	web: gunicorn filmofiles.wsgi<br>
iii) In settings.py, set DEBUG=False, then add your Heroku hostname to ALLOWED_HOSTS<br>
iv) Add, commit and push changes.<br>

#### JUMP to HEROKU:

9. DEPLOY:<br>
i) Return to the Heroku dashboard, go to the Deploy tab, and click to connect to GitHub.<br>
ii) Enter your GitHub repo, deploy the main branch manually, and monitor the build output in the Activity tab.<br>
iii) In the Resources tab, select an eco dyno for lightweight container deployment.<br>
iv) Verify and delete any existing Postgres database add-on to avoid unnecessary usage costs.<br>


## Languages used

- Python
- HTML
- CSS


## Programs, Frameworks & Libraries used

- [GitHub](https://github.com) - used for version control and the Projects tool for agile approach.
- [Codeanywhere](https://app.codeanywhere.com) - used as an IDE for the project.
- [Gitpod](https://gitpod.io) - used as a secondary IDE.
- [ElephantSQL](https://www.elephantsql.com) - used to create the PostgreSQL database for this app.
- [Heroku](https://dashboard.heroku.com/login) - used as a cloud-based platform to deploy the site.
- [Django](https://www.djangoproject.com) - used as a Python framework.
- [Bootstrap 4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction)- used as a CSS Framework.
- [Gunicorn](https://gunicorn.org) - used as a production-ready web server for Heroku.
- [WhiteNoise](https://whitenoise.readthedocs.io/en/stable/django.html) - used for serving the static files.
- [Summernote](https://summernote.org) - used as a WYSIWYG editor for users' posts.
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest) - used to manage Django Forms.
- [Cloudinary](https://cloudinary.com) - used to host images.
- [Font Awesome](https://fontawesome.com) - used for icons.
- [Convertio](https://) - used to convert images to webp files.
- [Favicon.io](https://favicon.io/favicon-converter/) - used to generate a favicon.
- Chrome Developer Tools - used for general troubleshooting.
- [ChatGPT](https://chat.openai.com) - used for general troubleshooting.
- [W3C](https://www.w3.org) - used for CSS code validation.


## Credits

Code Institute - I Think Therefore I Blog walkthrough project.<br>
[Python docs](https://docs.python.org/3/library/re.html) - for import re (used to check for numbers, uppercase and lowercase letters, and special characters in passwords).<br>
[Django docs](https://docs.djangoproject.com/en/3.2/_modules/django/forms/widgets/) - for info on django forms (widgets).

#### Images:
[Pixabay](https://pixabay.com/de/users/onkelglocke-12931647/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=4609877) - for cinema background image.<br>
[Pixabay](https://pixabay.com/de/users/agoss-432408/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=898154) - for popcorn placeholder image.


## Acknowledgments

With big thanks to my mentor Antonio Rodriguez for his valued support.

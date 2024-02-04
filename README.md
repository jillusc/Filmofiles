# Filmofiles

Filmofiles is a film review app designed to encourage movie fans to come together and share their opinions. The app is targeted towards users who wish to contribute to and engage in discourse with other like-minded individuals: users can browse and select other users' contributions to read, and, having completed a simple registration process, can post comments as well as submit their own film reviews.<br>

<img src="README images/page-home.png">

The live link can be found here - [FILMOFILES](https://filmofiles-de31d62f91c0.herokuapp.com/)

## User Experience (UX)

### User Stories

#### Epic: General User Experience

Browse film reviews<br>
As a User I can view a paginated list of film review posts in order to select one to view in full.<br>
AC1 - When a user clicks a 'Browse' link in the main page a list of contributed film reviews is displayed, newest first.<br>
AC2 - The user sees all film review posts with pagination.<br>

Read a film review<br>
As a User I can click on a film review post in order to read the full content.<br>
AC1 - When a film review title is clicked, a new page opens displaying a full view of the film review.<br>

View comments on a film review<br>
As a User I can view comments on a film review so that I can read and follow a conversation about films that interest me.<br>
AC1 - Given one or more user comments, the admin can view them.<br>
AC2 - The user can click on the comment thread to read the conversation.<br>

Register an account<br>
As a User I can register an account so that I can make contributions and therefore have an active role in the site.<br>
AC1 - Given a (valid) username and password, a user can register an account.<br>
AC2 - The user can log in.<br>
AC3 - Given a logged-in user, they can post a film review and/or leave a comment on a film review.<br>
AC4 - Given a logged in user, they can log out.<br>

#### Epic: Registered User Profile

Contribute a film review<br>
As a Registered User I can submit a film review so that I can participate in the film review community.<br>
AC1 - Fields for completion: title, genre, year, director name, image.<br>
AC2 - When a registered user's film review is approved, it should be displayed to the site.<br>

Contribute a comment<br>
As a Registered User I can leave comments on a film review so that I can contribute to a conversation.<br>
AC1 - When a user's comment is approved, it should be displayed below the review.<br>
AC2 - Users can reply to existing comments to continue the conversation.<br>
AC3 - If more than one comment is present, a threaded conversation is established.<br>

Modify or delete my contributions<br>
As a Registered User I can edit and delete my film reviews and comments so that I can control my contributions, e.g. correct mistakes, embellish content and remove altogether.<br>
AC1 - Given a logged in user, they can edit their film reviews/comments.<br>
AC2 - Given a logged in user, they can delete their film reviews/comments.<br>

View my profile page<br>
As a Registered User I can view a profile page that displays the film reviews and comments I have submitted so that I can keep track of my contributions.<br>
AC1 - A profile page opens when a relevant link is clicked.<br>
AC2 - Lists of "my film reviews" and "my comments" are displayed with items ordered newest first.<br>
AC3 - Items in the list are all clickable links to the relevant places/pages.<br>

#### EPIC: Site Administration

Manage contributions as an Admin<br>
As an Admin I can create, read, update and delete film reviews and comments so that the site's content aligns with the vision of the site owner and maintains quality and relevance.<br>
AC1 - Admin can create film reviews and comments.<br>
AC2 - Admin can view all film reviews and comments, including pending and approved ones.<br>
AC3 - Admin can edit film reviews and comments.<br>
AC4 - Admin can delete film reviews and comments.<br>

Control publication of content as an Admin<br>
As an Admin I can approve or disallow film reviews and comments so that I can responsibly manage the content.<br>
AC1 - Admin can approve film reviews and comments.<br>
AC2 - Admin can disallow film reviews and comments.<br>

#### User stories not yet implemented

The following user story was scoped out of the project due to time constraints:

Search for film reviews<br>
As a User I can search for a film by title, genre, year and director so that I can read reviews of films of my choosing.<br>
AC1 - A search bar is displayed with an enter key.<br>
AC2 - The user can input a case-insensitive search criterion (title, genre, year, director name).<br>
AC3 - Upon submission, the database is queried and returns a list of film titles matching the submitted search criterion.<br>
AC4 - The list items are clickable links of film title and slug that open a full view of the film review.<br>
AC5 - If there is no match, an appropriate message is displayed.<br>

## Design

The site's design was based on supporting the theme and the experience of film-watching.

### Colour

The colour scheme could be described as deep and rich as it features a charcoal grey and a dark teal colour; accent colours are a vibrant orange-red, golden yellow and cornflower blue. The colours were chosen to emulate the sense of being in a cinema, with subdued lighting and heavy, plush velvet curtains and seats. There is therefore a strong contrast between the background colours and accents, and the bright red text headings have a background shadow effect, resembling artificial light in the darkness.

### Imagery
A static image on the home page in monochrome depicts a view of an empty cinema from the perspective of a viewer looking towards the screen.<br>
<img src="README images/movie-theater-4609877_1920.webp">

In the review cards, a placeholder image of cinema tickets and a bag of popcorn furthers the association with the cinema-going experience to appeal to the users and reinforce the theme of the site.<br>
<img src="README images/popcorn-898154_1280.png">

The rest of the imagery is in the form of the individual film covers.
<img src="README images/film-anatomy-of-a-fall.webp"><img src="README images/film-inglourious-basterds.webp."><img src="README images/the-village.webp">

### Typography

The site uses just two fonts, imported from Goole Fonts: Workbench for the Filmofiles logo and Montserrat for the remaining text. Workbench has a somewhat grainy character with horizontal streaks running through it, making the logo reminiscent of an old VHS label and thus tying in another medium of film-watching.
<img src="README images/logo-nav-items.png">


## Agile Methodology

The Projects functionality in Github was used to manage the process of creating the site using an Agile approach, with a kanban board for tracking the progress and completion of User Stories. Github Issues were created for each User Story with defined acceptance criteria to make the execution as straightforward as possible.


## Data Models

This project follows Object-Oriented Programming principles and employs Django's Class-Based Generic Views. It includes three custom models: Film, representing film details (title, director, genre, year, image); Review, for film reviews with one-to-many relationships to the User & Film models and an implicit many-to-many relationship with the Comment model; and Comment with one-to-many relationships to User and Review models, which allows users to post comments on reviews.

The database schema are illustrated by the ERD diagram below:
<img src="README images/ERD.png">


## Testing

## Credits
https://docs.python.org/3/library/re.html for import re used to check for numbers, uppercase and lowercase letters, and special characters in passwords

POPCORN Bild von <a href="https://pixabay.com/de/users/agoss-432408/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=898154">agoss</a> auf <a href="https://pixabay.com/de//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=898154">Pixabay</a>

CINEMA Bild von <a href="https://pixabay.com/de/users/onkelglocke-12931647/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=4609877">Andreas Glöckner</a> auf <a href="https://pixabay.com/de//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=4609877">Pixabay</a>

https://docs.djangoproject.com/en/3.2/_modules/django/forms/widgets/ for info on django forms not using textfield, but this being controlled instead by a widget
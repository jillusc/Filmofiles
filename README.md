# Filmofiles

Filmofiles is a film review app designed to encourage movie fans to come together and share their opinions. The app is targeted towards users who wish to contribute to and engage in discourse with other like-minded individuals: users can browse and select other users' contributions to read, and, having completed a simple registration process, can post comments as well as submit their own film reviews.

The live link can be found here - [FILMOFILES](https://filmofiles-de31d62f91c0.herokuapp.com/)

## User Experience (UX)

### User Stories

#### Epic: General User Experience

Browse film reviews
As a User I can view a paginated list of film review posts in order to select one to view in full.
AC1 - When a user clicks a 'Browse' link in the main page a list of contributed film reviews is displayed, newest first.
AC2 - The user sees all film review posts with pagination.

Read a film review
As a User I can click on a film review post in order to read the full content.
AC1 - When a film review title is clicked, a new page opens displaying a full view of the film review.

View comments on a film review
As a User I can view comments on a film review so that I can read and follow a conversation about films that interest me.
AC1 - Given one or more user comments, the admin can view them.
AC2 - The user can click on the comment thread to read the conversation.

Register an account
As a User I can register an account so that I can make contributions and therefore have an active role in the site.
AC1 - Given a (valid) username and password, a user can register an account.
AC2 - The user can log in.
AC3 - Given a logged-in user, they can post a film review and/or leave a comment on a film review.
AC4 - Given a logged in user, they can log out.

#### Epic: Registered User Profile

Contribute a film review
As a Registered User I can submit a film review so that I can participate in the film review community.
AC1 - Fields for completion: title, genre, year, director name, image.
AC2 - When a registered user's film review is approved, it should be displayed to the site.

Contribute a comment
As a Registered User I can leave comments on a film review so that I can contribute to a conversation.
AC1 - When a user's comment is approved, it should be displayed below the review.
AC2 - Users can reply to existing comments to continue the conversation.
AC3 - If more than one comment is present, a threaded conversation is established.

Modify or delete my contributions
As a Registered User I can edit and delete my film reviews and comments so that I can control my contributions, e.g. correct mistakes, embellish content and remove altogether.
AC1 - Given a logged in user, they can edit their film reviews/comments.
AC2 - Given a logged in user, they can delete their film reviews/comments.

View my profile page
As a Registered User I can view a profile page that displays the film reviews and comments I have submitted so that I can keep track of my contributions.
AC1 - A profile page opens when a relevant link is clicked.
AC2 - Lists of "my film reviews" and "my comments" are displayed with items ordered newest first.
AC3 - Items in the list are all clickable links to the relevant places/pages.

#### EPIC: Site Administration

Manage contributions as an Admin
As an Admin I can create, read, update and delete film reviews and comments so that the site's content aligns with the vision of the site owner and maintains quality and relevance.
AC1 - Admin can create film reviews and comments.
AC2 - Admin can view all film reviews and comments, including pending and approved ones.
AC3 - Admin can edit film reviews and comments.
AC4 - Admin can delete film reviews and comments.

Control publication of content as an Admin
As an Admin I can approve or disallow film reviews and comments so that I can responsibly manage the content.
AC1 - Admin can approve film reviews and comments.
AC2 - Admin can disallow film reviews and comments.

#### User stories not yet implemented

The following user story was scoped out of the project due to time constraints:

Search for film reviews
As a User I can search for a film by title, genre, year and director so that I can read reviews of films of my choosing.
AC1 - A search bar is displayed with an enter key.
AC2 - The user can input a case-insensitive search criterion (title, genre, year, director name).
AC3 - Upon submission, the database is queried and returns a list of film titles matching the submitted search criterion.
AC4 - The list items are clickable links of film title and slug that open a full view of the film review.
AC5 - If there is no match, an appropriate message is displayed.

## Design

The site's design was based on supporting the theme and the experience of film-watching.

### Colour

The colour scheme could be described as deep and rich as it features a charcoal grey and a dark teal colour; accent colours are a vibrant orange-red and golden yellow. The colours were chosen to emulate the sense of being in a cinema, with subdued lighting and heavy, plush velvet curtains and seats. There is therefore a strong contrast between the background colours and accents, and the bright red text headings have a background shadow effect, resembling artificial light in the darkness.

### Imagery

A static image on the home page site depicts ... In the review cards, a placeholder image of cinema tickets and a bag of popcorn furthers the association with the cinema-going experience to appeal to the users and reinforce the theme of the site. The rest of the imagery will be uploaded by users with each film review submission.

### Typography

Two fonts were imported from Goole Fonts: Workbench for the Filmofiles logo and Montserrat for the headings. The remaining text across the site uses the Helvetica Neue font. Workbench has a somewhat grainy character with horizontal streaks running through it, making the logo reminiscent of an old VHS label and thus tying in another medium of film-watching.

## Agile Methodology

The Projects functionality in Github was used to manage the process of creating the site using an Agile approach, with a kanban board for tracking the progress and completion of User Stories.
Github Issues were created for each User Story with defined acceptance criteria to make the execution as straightforward as possible.

## Data Models

The principles of Object-Oriented Programming and Django’s Class-Based Generic Views were used throughout this project:

AllAuth was used for the user authentication system.
The custom model, Film,  ... A ... can only have one user and one ... and is therefore linked to the User and ... models through foreign keys.
The second custom model, Review, was implementedn order for users to submit reviews . The review's author is a ForeignKey to the User model given a recipe can only have one author...
The other custom model, Comment, allows users to comment on a review and ... is a foreign key in the comment model given a comment can only be linked to one recipe.

The the database schema are illustrated by the diagram below:

## Testing
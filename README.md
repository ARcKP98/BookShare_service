# Bookkeeping Service

The Bookkeeping service is a command line interface application that uses the Heroku terminal. The purpose of this app is to allow users to explore new books by checking them out of the library and to donate books that can be used by others. This service acts as intermediary between people who would like to read books and people who would like to donate books for others to read by managing the collection and storage of books.   

<!-- ![The landing page on different devices]() -->

<br>

### The [link](https://bookkeeping.herokuapp.com/) to the live project 
---
## Contents
* [User Experience](#user-experience)
  * [Client Objective](#client-objective)
  * [User Stories](#user-stories)

* [Design](#design)
  * [Flowchart](#flowchart)

* [Features](#features)
  * [General Features](#general-features)
  * [Future Implementations](#future-implementations)
  * [Database](#database)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Libraries and Programs Used](#libraries-and-programs-used)

* [Testing](#testing)
  * [Issues Discovered](#issues-discovered)
  * [PEP8 Validation](#pep8-validation)

* [Deployment & Local Development](#deployment--local-development)
  * [Deployment](#deployment)
  * [Local Development](#local-development)
    * [Fork](#fork)
    * [Clone](#clone)

* [Credits](#credits)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgments](#acknowledgments)
------

## User Experience
  ### Client Objective
  The aim of this ficticious service is to provide users with the ability to share books using a central database. The user can then choose to view the books available in the database and can then choose to checkout a book of their choice. In the event that the user would like to donate a book, they can do so by donating a book of their choice to the central database. 

  ### User Stories
  #### New User Goals
  * I want to find out what kind of books the service has.
  * I want the abiliity to checkout a book from the database with minimal effort.
  * I want the ability to donate a book to the database with minimal effort. 
  * I want this app to be easy to use with clear instructions. 

    #### Returning User Goals 
  * I want the database to be up to date with all the books it has.
  * I want the program to tell me if the book I am donating is in the database or not.

  ## Design 
  ### Flowchart
  ![Flowchart](/readme-images/bookkeeping.drawio%20.png)
  Flow of how the program runs.

  ## Features 
  ### General features 
  <br>

   The program starts with a welcome message. This area outlines what the service does and how the user can benefit from it. 
  ![The welcome screen](/readme-images/welcome-screen.png)

  <br>

  The next section is where the user can decide what they would like to do. The user can either decide to view the book collection that already exists or they can choose to donate to the collection for others to see. 
  ![Purpose of visit](/readme-images/purpose.png)

    <br>

  If the user decides to view the collection by pressing 1, the user is then taken to the collection where they can view all the books that are currently available. The user here can see the code to checkout the book of their choice, the name of the book, and the author of the book. The user has two options: To check out a book using the code or to leave the program. If they don't want to leave, the user then enters the code to checkout the book of their choice and then gets a confirmation of the book they checked out.
  ![View the collection](/readme-images/collection.png)
  ![View the collection and borrow a book](/readme-images/checkout.png)

    <br>

  If the user decides to donate instead of checking out a book, they are first asked to enter the name of the book they want to donate. This name is then used to search the Google worksheet to see if it exists. If the book does not exist, the user is asked for the author's name and then the book is added to the collection. If the book does exist in the collection, the user is informed that the book exists and then has the option to view the collection or leave the program.
  ![Donation section](/readme-images/donation.png)
  ![Donation section but the book exists](/readme-images/donation-exists.png)


  ### Future Implementations
  <br>
  In the future, I would like to add more functionality and features to the program to improve overall user experience. Features like: 
  * More genres of books which can be organised in their respective sections so the user only looks at books that are relevant to them. 
  * Use an actual database to store books instead of a Google sheet for better data management.
  * Add a log to tracks users checkout and donation history to provide a more traditional library experience.

<br>

### Database
 ![Donation section](/readme-images/donation.png)
 
 A Google sheet was used for this app to function properly. The sheet was used to keep track of all the books that were available for checkout and all the books that were donated were added to this worksheet. 
<br>

## Technologies used
### Language used
* The program was primarily created using **Python 3**. 

### Libraries and Programs Used
The following python libraries were used: 
* gspread: Access google sheets.
* time: To create a buffer in code execution. 
* regex: Convert input to regualr expression for scanning the worksheet.
* pyfiglet: For the service logo.
* colorama: To style the terminal text.
* tabulate: To display all the data in a table format.

The following Programs were used:
* Google Sheets: To store all the data.
* Draw.io: To create the flowchart.
* Gitpod: To edit code and READ.ME file.
* Git: Version control.
* Heroku: Deployment of the final app. 

<br>




  












  

 
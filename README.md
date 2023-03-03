# Bookkeeping Service

The Bookkeeping service is a command line interface application that uses the Heroku terminal. The purpose of this app is to allow users to explore new books by checking them out of the library and to donate books that can be used by others. This service acts as intermediary between people who would like to read books and people who would like to donate books for others to read by managing the collection and storage of books.   

![The landing page](/readme-images/appview.png)

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
  * [User Goal Testing](#user-goal-testing)
  * [Manual Testing](#manual-testing)
  * [Issues Discovered](#issues-discovered)
  * [PEP8 Validation](#pep8-validation)

* [Deployment & Local Development](#deployment--local-development)
  * [Deployment](#deployment)
  * [Local Development](#local-development)
    * [Fork](#fork)
    * [Clone](#clone)

* [Credits](#credits)
  * [Acknowledgments](#acknowledgments)
------

## User Experience

### Client Objective
The aim of this ficticious service is to provide users with the ability to share books using a central database. The user can then choose to view the books available in the database and can then choose to checkout a book of their choice. In the event that the user would like to donate a book, they can do so by donating a book of their choice to the central database. 
<br>

### User Stories
#### New User Goals

* I want to find out what kind of books the service has.
* I want the abiliity to checkout a book from the database with minimal effort.
* I want the ability to donate a book to the database with minimal effort. 
* I want this app to be easy to use with clear instructions. 

<br>

#### Returning User Goals 

* I want the database to be up to date with all the books it has.
* I want the program to tell me if the book I am donating is in the database or not.

<br>

## Design 

### Flowchart
![Flowchart](/readme-images/bookkeeping.drawio%20.png)
Flow of how the program runs.

<br>

## Features 

### General features 
The program starts with a welcome message. This area outlines what the service does and how the user can benefit from it. 
![The welcome screen](/readme-images/welcome-screen.png)

<br>

The next section is where the user can decide what they would like to do. The user can either decide to view the book collection that already exists or they can choose to donate to the collection for others to see. 
![Purpose of visit](/readme-images/purpose.png)

<br>

If the user decides to view the collection by pressing 1, the user is then taken to the collection where they can view all the books that are currently available. The user here can see the code to checkout the book of their choice, the name of the book, and the author of the book. The user has two options: To check out a book using the code or to leave the program. If they don't want to leave, the user then enters the code to checkout the book of their choice and then gets a confirmation of the book they checked out.
![View the collection](/readme-images/collection.png)
![View the collection and borrow a book](/readme-images/checkout.png)
The user then has to press the run program button to start a new session.

<br>

If the user decides to donate instead of checking out a book, they are first asked to enter the name of the book they want to donate. This name is then used to search the Google worksheet to see if it exists. If the book does not exist, the user is asked for the author's name and then the book is added to the collection. If the book does exist in the collection, the user is informed that the book exists and then has the option to view the collection or leave the program.
![Donation section](/readme-images/donation.png)
![Donation section but the book exists](/readme-images/donation-exists.png)

The user then has to press the run program button to start a new session.

<br>


### Future Implementations

In the future, I would like to add more functionality and features to the program to improve overall user experience. Features like: 
* More genres of books which can be organised in their respective sections so the user only looks at books that are relevant to them. 
* Use an actual database to store books instead of a Google sheet for better data management.
* Add a log to tracks users checkout and donation history to provide a more traditional library experience.
* Allow user to restart the application without pressing the run program button.

<br>

### Database

![Google Sheets database](/readme-images/sheets.png)
 
A Google sheet was used for this app to function properly. The sheet was used to keep track of all the books that were available for checkout and all the books that were donated were added to this worksheet. 
<br>

## Technologies used
### Language used
* The program was primarily created using **Python 3**. 

<br>

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
* [Draw.io](https://app.diagrams.net/): To create the flowchart.
* Gitpod: To edit code and READ.ME file.
* Git: Version control.
* Heroku: Deployment of the final app. 
* [CI python Linter](https://pep8ci.herokuapp.com/): To validate the code in accordance with PEP8. 

<br>

## Testing 
### User Goals Testing
The table outlines first-time users goals and whether they were accomplished or not.
| First-time User Goals| How was it addressed | Accomplished
| ------ | --------- | -----------
| I want to find out what kind of books the service has. |The user can brose the collection before deciding upon a book. | Yes
| I want the abiliity to checkout a book from the database with minimal effort.| The user can checkout a book simply by pressing the code associated with the book.| Yes
| I want the ability to donate a book to the database with minimal effort.| The user can donate a book effortlessly by providing the name of the book and the author. | Yes
| I want this app to be easy to use with clear instructions. | The program starts with instructions regarding what the service is about and throughout the app the user is not required to enter large inputs to use the app. They just have to enter numbers or small words. | Yes 

<br>

The table outlines returning users goals and whether they were accomplished or not.
| Returning User Goals| How was it addressed | Accomplished
| ------ | --------- | -----------
| I want the database to be up to date with all the books it has. | The google sheet used is always updated when a book is donated or checked out so always providing the user with up to date information. | Yes
| I want the program to tell me if the book I am donating is in the database or not.| The user will be informed if the book they have entered already exists in the google sheets. | Yes
<br>

### Manual Testing
The table below outlines tetsing done on different parts of the program. Testing done in order of flow of the program. 
|Expectation| How was it tested| Result
| -------- | ----------- | ---------------
| The user cannot proceed if the input is: less than three characters, just numbers, or left blank| By entering wrong input to see if the program continues or not. | The input section works as intended.
|When the user is asked to pick between browsing books or donating books, the user cannot proceed unless they enter the right number.| By entering wrong numbers or random text to see if the program accepts that input.| The input works as intended. 
|If the user wants to leave when they are done browsing, they cannot leave until they enter 'Yes'.| By trying to enter other words or numbers instead of yes/no.| The input works as intended. 
|If the user wants to checkout a book, they cannot enter text instead of numbers. | By trying to enter letters to see if the program accepts that input.| The input works as intended. 
|If the user wants to donate, the program does not accept books that already exist in the database.| By entering names of the books that already exist to see if they are added to the collection or not. | The code works as intended.
|If the user donates a book and it does not exist, the user is asked for more information before adding the book to the collection.| By entering a book that does not exists and providing the neccesary information. Then check the google worksheet to see if the entry was appended. | The code works as intended.

<br>

### Issues Discovered 
|Bug|Solve|
|-----|---------|
|The google sheet was not being searched by python when user picked a number. The code would return only location or would just not parse. | Convert the input to RegEx when working with find(). To get the values in that row, use row.values, using the var where find parameter was saved to pull value from that row. |
|The purpose function was not using the return value from user_input once the functions were added to the main function. | Store the return value of user_input in a user variable which is in the main function. Pass that variable as an argument in the purpose function.|
|The name variable was not accepting valid input for names unless users entered their full name. | Remove the isalnum() check and only keep the check for not entering names.|
|The program would crash if the user input was invalid. | Add try and except statements.|
|The colection data was not presented properly on Heroku. | Switch to tabulate and use maxcols. |
|When donating, the code for making sure the book was not present led to AttributeError(AttributeError: 'NoneType' object has no attribute 'row'). | The first part was to use the keyword **is**. The second part was to convert the input to string. |
|If the input, when checking out a book was wrong, it would lead to an AttributeError. | One of the elif statements was in the wrong code block and the input(along with its RegEx conversion) was added to the except block again.|
|The checkout code would be duplicated if there were more books that were checkedout. | Add a + 5 to the variable which takes the length of the dataset and adds 5 to give a checkout code. This is not a perfect solution but for the programs purpose and time constraints, this solution is valid.|
|Character length exceeding 80 characters. | Use string concatenation and break text up.|

<br>

### PEP8 Validation
 ![PEP8 validation](/readme-images/pep8.png)

 
 No major errors were found when the code was tested. 

<br>

 ## Deployment & Local Development
 ### Deployment 
 This is a backend application made using python which cannot be deployed using GitHub pages. This project therefore was deployed using Heroku. Follow the steps below.
 1. Login to your Heroku account.
 2. On your dashboard, click on the new button which is at the top right corner. 
 3. Select **Create new app**. 
 4. Give your app a name, select your region and press **Create app**.
 5. Go to the *settings* tab and scroll down to *Config Vars* and click **Reveal Config Vars**
 6. Here, enter **PORT** in the KEY field and **8000** in the VALUE field. Press Add after.
 7. In the second KEY field, enter **CREDS** and in the VALUE field enter all the contents of your **creds.json** file.
 8. Next, scroll down to *buildpacks* and select **Add buildpacks**. 
 9. Select and add Python and node.js buildpack. Make sure they are in that order. If not re-arrange them using the hamburger icon. 
 10. Scroll up and select the *Deploy* tab and choose GitHub. 
 11. Search the repository you want to use and then click **Connect**. Now your repository is connected to Heroku.
 12. Scroll to the bottom of the page and pick either *Manual* or *Automatic* deployment. Click **Deploy branch** and wait for the app to be deployed. 
 <br>

 ### Local Development
 #### Fork
1. Log in with your Github account or make one if you don't have one.
2. Find the repository: mcu_quiz.
3. Click the Fork button on the top right corner. 
<br>

#### Clone
1. Log in with your Github account or make one if you don't have one. 
2. Find the repository: mcu_quiz.
3. Click the **Code** button next to the Gitpod button and **copy** the HTTPS link. 
4. Open the terminal. 
5. Make sure that the current directory is the one where you want the cloned repository to be. 
6. Use the command ```git clone``` and paste the link. 
7. Press Enter. Now the repository is cloned.
<br>

## Credits 
* [Tabulate](https://pypi.org/project/tabulate/) for formatting the tables.
* [Time](https://docs.python.org/3/library/time.html) for using sleep. 
* W3Schools for various python methods. 
* [StackOverflow](https://stackoverflow.com/questions/8949252/why-do-i-get-attributeerror-nonetype-object-has-no-attribute-something) for helping with None.
<br> 

### Acknowledgements
* Adegbenga Adeye, my CI mentor for feedback and testing the program with me. 
* Tutor support for all their time and guidance. 
* Code Institute for the python template.
























  












  

 
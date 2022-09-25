# TASK 1 (Agile Techniques)

### Question 1

##### SCRUM CEREMONIES

**1. Product Backlog Refinement**

The product backlog refinement is the process of adding details and order to the items
in th product backlog. The product owner creates a prioritised list of user stories. 

**2. Sprint Planning**
Scrum progresses in a series of “Sprints” that typically take 1-3 weeks. 
In each sprint we build, plan, test and review a potentially shippable product.
Then everyone meets to discuss user stories and estimate their relative sizes.


**3. Daily Scrum**

Daily scrum is an event for the developers of the scrum team
This event is held daily to inspect the progress towards the 
sprint goals and includes discussion around the project progress, 
current work and any blockers.

**4. Sprint Review**

In a sprint review a demo of completed work is presented to product owner 
and discusses how things can be improved.

**5. Sprint retrospective**


##### SCRUM ROLES

**1. Scrum Master**

A scrum master is accountable fot the scrum teams effectiveness. They do this by enabling
the scrum team to improve practices, within the scrum framework. 

**2. Product Owner**

The product owner is responsible for defining the features needed in the product.
They are also responsible for effective backlog management
including communicating the product goal.

**3. Development Team**

This is a cross-platform functional team of individuals who are 
at the core of the scrum development team structure. They are responsible
for building the actual product increments and meeting sprint goals.


### Question 2

Feature: Booking a yoga session

**As a** user I,

**want to** be able to log in,

**so that** I can book a yoga session.

Scenario: The user logs into the system to book a session

**Given** I want to book a yoga session 

**When** I log in to the system

**Then** my login details are accepted

- As a user I want to be able to input my booking details so that I can see the classes' information.

- As a user I want to be able to view my bookings, appointments and schedules so that I can plan ahead.

Breaking this down into executable, scope-bound task based on the user stories.

Front-end to build the user interface 

- Define Sign-up/Login form style using HTML and CSS
- Develop HTML and Javascript Sign-Up/Login presentation layer code
- Develop form to accept user input using HTML and CSS
- Display classes information using HTML 

Sever Side (Database) and Backend code (Python)
- Create an SQL database to store information
- create a table in the database to store all booking, appointments and schedules
- Create a table in the SQL database for user information
- Establishing database connectivity with Python to access information from the database server
- Write and run regression tests


# TASK 2 (SQL)

### Question 1

#### Cinema Booking System

**Key Requirements**

- It should be able to list the different cinema locations.
- Each cinema can have multiple theatres and each theatre can run one show at a time
- Each movie will have multiple show time
- Selection of movies to choose from
- Users should be able to search movies by their title, release date, genre, and language
- When a customer selects a movie, the system should display the cinema location running the movie
- Users should be able to select a movie at a particular cinema and book their tickets
- The system should display the seating arrangement of their cinema theatre
- The system should allow users to select their seating preferences 
- The user should be able to distinguish between the available and booked seats
- The system should display the number of ticket the user is booking
- Users should be able to pay with credit card.
- Users should be able to view the amount of their tickets
- Users should be able to add discount codes when checking out 
- Users should be able to receive notifications when there is a new movie available, as well as when they
have made or cancelled a booking

  
**Main Considerations**
- For the system to not be abused, we can restrict users to not book more than ten seats at a time
- To assume that traffic would spike on much anticipated movies and seats are expected to
fill up pretty quickly. The system should be scalable to handle to the heavy traffic. 

**Common problems**

- We want to ensure that no two users reserve the same seat
- As the system takes card payments, this means it should the database should be secure

**Tools to consider**

- We would use a simple user interface to create a responsive user-friendly interface using HTML, CSS and JavaScript
- Python for backend logic and database (SQL) to store users details, cinema details and back up results


# IU-Habit-Tracking-Application-OOFPP
***
# Table of Contents
- [Habit Tracker](#habit-tracker)
  * [Habit Tracker's Core Functionality](#habit-tracker-s-core-functionality)
    + [Progress and Streak Tracker](#progress-and-streak-tracker)
- [Getting Started](#getting-started)
  * [Dependencies](#dependencies)
  * [Installing](#installing)
    + [Packages for running tests](#packages-for-running-tests)
  * [How To Run the Program](#how-to-run-the-program)
  * [Running Tests](#running-tests)
- [Usage](#usage)
  * [Add/Remove Habit OR Category](#add-remove-habit-or-category)
      - [1. Adding a habit](#1-adding-a-habit)
      - [2. Remove Habit](#2-remove-habit)
      - [3. Delete Category](#3-delete-category)
      - [4. Back to Main Menu](#4-back-to-main-menu)
  * [Modify Habit's Periodicity](#modify-habit-s-periodicity)
  * [Mark Habit as Completed](#mark-habit-as-completed)
  * [Show Habits (All or Sort by Periodicity)](#show-habits--all-or-sort-by-periodicity-)
      - [1. View All Habits](#1-view-all-habits)
      - [2. View Daily Habits](#2-view-daily-habits)
      - [3. View Weekly Habits](#3-view-weekly-habits)
      - [4. View Monthly Habits](#4-view-monthly-habits)
      - [5. Back to Main Menu](#5-back-to-main-menu)
  * [Analytics](#analytics)
      - [1. View All Habit's Streaks](#1-view-all-habit-s-streaks)
      - [2. View Longest Streak of Specific Habit](#2-view-longest-streak-of-specific-habit)
      - [3. View Streak Log of Specific Habit](#3-view-streak-log-of-specific-habit)
      - [4. Back to Main Menu](#4-back-to-main-menu-1)
  * [Exit](#exit)
- [Contributing](#contributing)
- [Contact](#contact)

# What is a habit tracking Application ?

 A habit monitoring/tracking application  helps users create and maintain healthy routines, allowing them to monitor their development by tracking their streaks and enhance their general well-being and productivity.The app allows users to keep track of their daily routines and habits by creating a new habit , and keep track of good habits to form and bad ones to break.

 This work is a part of *IU University's* *object oriented and functional programming with python* course.


## Core Features of the Application
The habit tracker essentially allows a user to:

* Create a habit 
* Remove a habit 
* Set Periodicity of habits (Daily or weekly)
* Mark the habit as completed

### Analytics
Moreover, the user will also be able to:
* View all of their created habits
* Among all defined habits, view habits which are of the same periodicity.
* Among all defined habits, view the habit which has the longest streak.
* Among all defined habits, view the longest streak of a specific habit.



# Guide to the installation of the application

## Tools required 
* Python 3.7 + : Python is a high-level, interpreted programming language known for its simplicity and readability.
* Inquirer : Inquirer is a Python module for creating interactive command-line user interfaces. It makes it easier to create interactive prompts and collect user input from the command line.
* Pytest : Pytest is a Python code testing framework that makes it easy to write and execute tests, making it easier to ensure the quality and correctness of your code.

## Installing
 Make sure that Python 3.7 + is installed on your OS. You can download the latest version of Python from [this link.](https://www.python.org/downloads/)<br>

<br> After installing Python, you can proceed and install the following libraries. <br>
To clone the repository, navigate to the desired directory. Use this code to clone the repository and download the habit tracker application:
```

```
<br>[Questionary](https://www.python.org/downloads/) - Questionary is a Python library for building pretty command line interfaces. 
<br>Install by running the below command:<br>
```
pip install questionary
```

### Packages for running tests
To run the tests, you will need the following packages installed:
<br>Pytest - For testing functions:<br>
```
pip install -U pytest
```
<br>Freezegun - For freezing time: <br>
```
pip install freezegun
```

## How To Run the Program
After installing the dependencies, download the files from this repository (if not downloaded already) and store them in a separate folder. Open your command/terminal window and [cd](https://www.alphr.com/change-directory-in-cmd/) to your downloaded folder. After that, type the following command to execute the program:
```
python main.py
```
For Python 3.10+
```
python3 main.py
```
Doing so will launch the CLI and then you'll be able to see and choose from the following options in your Habit Tracker:

```
*** Welcome to the Habit Tracker ***

What do you want to do? (Use arrow keys)
 » Add/Remove Habit OR Category
   Modify Habit's Periodicity
   Mark Habit as Completed
   Show Habits (All or Sort by Periodicity)
   Analytics
   Exit
```

## Running tests
To run the test; navigate to the test folder (included with the repository) through command/terminal by using [cd](https://www.alphr.com/change-directory-in-cmd/) and then type ```pytest```. 

# Usage

**Important**: You can choose to keep or remove the **main.db** file as it contains the following pre-defined habits: Coding, Workout, Grocery, Piano, and Hiking. <br>

## Add/Remove Habit OR Category
#### 1. Adding a habit
Your first action should start by creating an habit and you can do so by launching the program and selecting:
```
 Add/Remove Habit OR Category
```
It will further expose the user to a sub-menu, where you'll have to choose *Add habit* and enter the required information:
```
Would you like to Add, Remove Habit or Category? (Use arrow keys)
 » Add Habit
   Remove Habit
   Delete Category
   Back to Main Menu

```
https://user-images.githubusercontent.com/48772669/179855439-e20830dc-1c75-41cf-aa57-a2c7b0c12a7a.mp4

#### 2. Remove Habit
This option will show you a list of habits that you have created, you'll have to simply choose the habit you want to delete and press enter.

#### 3. Delete Category
Similar to removing habit; a list of created categories will be shown for the user to select.

#### 4. Back to Main Menu
Takes the user back to main menu.

## Modify Habit's Periodicity
User will have to select the habit they'd like to change the periodicity of and then a new prompt will ask the user to select the new periodicity for the habit.

## Mark Habit as Completed
The user can use this option to mark their habit as completed. <br> Note: A habit can be marked as completed only once during the defined period. <br>
<br>Note: If the user failed to complete their habit within the specified periodicity; then marking the habit as completed will the reset the streak to 1. <br>
<br>Why 1 though? Because the user invoked the mark as completed function to complete their habit thus the function takes this into account and resets the habit to 1 to register the very current streak.

https://user-images.githubusercontent.com/48772669/179856460-19a87cb4-4750-413c-89fa-16bd2b85be7d.mp4

## Show Habits (All or Sort by Periodicity)

#### 1. View All Habits
Lists all the created habits along with their information like *Name, Periodicity, Category and Date/Time*.

https://user-images.githubusercontent.com/48772669/179857285-921aea0b-e517-4e7b-a58a-0d83e9cefbe6.mp4

#### 2. View Daily Habits
Lists all the habits in the daily period.
#### 3. View Weekly Habits
Lists all the habits in the weekly period.
#### 4. View Monthly Habits
Lists all the habits in the monthly period.
#### 5. Back to Main Menu
Obvious function.



## Analytics
#### 1. View All Habit's Streaks
Lists all the habits and their streaks.

https://user-images.githubusercontent.com/48772669/179857969-61c3de26-bb0f-4624-a075-7f407d971547.mp4

#### 2. View Longest Streak of Specific Habit
Lists the longest streak ever achieved by a specific habit.
#### 3. View Streak Log of Specific Habit
Shows the streak history of the specific habit.
#### 4. Back to Main Menu
And menu it is!

## Exit
Exits the program.

# Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


# Contact

Izaan Zubair - [Email](mailto:izkidy@yahoo.com)

Project Link: [https://github.com/izaanz/habit_tracker](https://github.com/izaanz/habit_tracker)

<p align="right">(<a href="#top">back to top</a>)</p>


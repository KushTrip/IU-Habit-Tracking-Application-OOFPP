# IU-Habit-Tracking-Application-OOFPP
***
# Table of Contents
- [What is a habit tracking Application ?](#What is a habit tracking Application ?)
  * [Core Features of the Application](#Core Features of the Application)
    + [Analytics](#Analytics)
- [Guide to the installation of the application](#Guide to the installation of the application)
  * [Tools required ](#Tools required )
  * [Installing the tools](#Installing the tools)
    + [Packages for running tests](#packages-for-running-tests)
  * [How To Run the Program](#how-to-run-the-program)
  * [Running Tests](#running-tests)
- [Usage](#usage)
  * [1.Creating a new  habit](#1.Creating a new  habit)
  * [2.Remove a Habit](#2.Remove a Habit)
  * [3.Mark your habit as completed(Check-off habit)](#3.Mark your habit as completed(Check-off habit))
  * [4.Analyze your habit](#4.Analyze your habit)
- [Contributing](#contributing)
- [Contact](#contact)

# What is a habit tracking Application ?

 A habit monitoring/tracking application  helps users create and maintain healthy routines, allowing them to monitor their development by tracking their streaks and enhance their general well-being and productivity.The app allows users to keep track of their daily routines and habits by creating a new habit , and keep track of good habits to form and bad ones to break.

 This work is developed as  a part of *IU University of applied Science's* *object oriented and functional programming with python* module.


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

## Installing the tools
 Make sure that Python 3.7 + is installed on your OS. You can download the latest version of Python from [this link.](https://www.python.org/downloads/)<br>

<br> After installing Python, you can proceed and install the following libraries. <br>

<br>Inquirer : Inquirer is a Python module for creating interactive command-line user interfaces.
<br>Install it by running the below command:<br>
```
pip install inquirer
```

### Packages for running tests
To run the tests, you will need the following packages installed:
<br>Pytest - For testing functions:<br>
```
pip install pytest
```


## How To Run the Program
After installing the required tools, download the files from this repository and store them in a separate folder.
<br>
To clone the repository, navigate to the desired directory. Use this code to clone the repository and download the habit tracker application:
```
https://github.com/KushTrip/IU-Habit-Tracking-Application-OOFPP.git
```

Open your command/terminal window and change directory [cd] to your downloaded folder.By changing directories, you can navigate to the specific location where the files or folders are located and perform operations on them.<br>
<br>
After that, type the following command to execute the program:
```
python main.py
```
For Python 3.10+
```
python3 main.py
```
Doing so will launch the CLI and then you'll be able to see and choose from the following options in your Habit Tracker:

```
*** Welcome to the Habit Tracking Application ***

What do you wish to do? (Use arrow keys for navigation)
 » Create a new habit
   Mark your habit as completed(Check-off)
   Analyze your habit 
   Delete your habit
```

## Running tests
To run the test: navigate to the test folder (included with the repository) through command/terminal by using [cd](https://www.alphr.com/change-directory-in-cmd/) and then type ```pytest```. 

# Usage

**Important**: You can choose to keep or remove the **main.db** file as it contains the following pre-defined habits: Coding, Workout, Grocery, Piano, and Hiking. <br>

## 1. Creating a new  habit
Your first action should start by creating a habit and you can do so by launching the program and selecting:
```
 Create a new habit
```
It will further expose the user to a sub-menu, where you'll have to enter name, goal of the habit and also set its periodicity to either daily or weekly.
```
Enter the name of your habit : 
Enter the goal of your habit : 
Set the periodicity of your habit to either Daily or weekly : 
 »Daily 
 Weekly
```

## 2. Remove a Habit
Choose "Delete your habit" from the main screen and type the name of the habit you wish to remove.
```
Enter the name of the habit you wish to delete :
```


## 3. Mark your habit as completed(Check-off habit)
To check-off or mark habit as complete, choose "Mark your habit as completed(Check-off)" from the main screen, then enter the name of the habit you want to check-off.
```
Enter the name of the habit you wish to check-off :
```


## 4.Analyze your habit
The application also  provides the functionality to the users to analyze their habits. To analyze the habit, choose "analyze your habit" from the main screen and then choose their desirable analytical option.
```
Select your desirable analytical option among the following :
* Display all of my created habits
* Display habits which are of the same periodicity.
* Display the habit which has the longest streak.
* Display the longest streak of a specific habit.
```


# Contributing

Contributions are eagerly welcomed! If you have any cutting-edge suggestions, troublesome bug reports, or awe-inspiring feature requests, please open an issue or surprise me  with a fascinating pull request. Your feedback will be greatly appreciated!

# Contact

Kush Tripathi - [Email](tripathikush10@gmail.com)

Project Link: [https://github.com/KushTrip/IU-Habit-Tracking-Application-OOFPP](https://github.com/KushTrip/IU-Habit-Tracking-Application-OOFPP)



import re
import inquirer
from habit import Habit
from db import connect_db, check_if_habit_exists, get_period, add_predefined_habits
from analytics import return_all_habits_data, return_longest_streak_of_all, return_longest_streak_of_habit, \
    return_habits_with_same_periodicity

print("\n")
print("\n")

#  CLI Interface
def main():
  """
    CLI Interface utilized with inquirer library to
    display the contents of the habit tracking Application for the user.
   """
   print("\n")
    print("**************************HABIT TRACKING APPLICATION**************************")
    print("\n")
    
     connection = connect_db()
    try:
        add_predefined_habits(connection)
         # Shows 6 choices for the user to choose from
        choice = inquirer.list_input("What do you wish to do? (Use arrow keys for navigation): ",
                                     choices=["Create a new habit", "Mark your habit as completed(Check-off habit)", "Analyze your habits",
                                              "Delete your habit", ])
        
        
         # Creating new habit accordingly to the user's input
        if choice == "Create a new habit":
            habit_name = input("Enter the name of your habit : ")
            habit_description = input("Enter Goal of your habit: ")
            print("\n")

            # checks if the input given by user is empty or numbers
            while not re.match("^[a-z A-Z]+$", habit_name):
                print("\n")
                print('\x1b[6;30;42m' + "Please enter TEXT ONLY" + '\x1b[0m')
                habit_name = input("Enter the name of your habit: ")
                print("\n")
                print('\x1b[6;30;42m' + "Now, please enter TEXT ONLY" + '\x1b[0m')
                habit_description = input("Enter Goal of your habit: ")
                print("\n")

            periodicity_choice = [
                inquirer.List('period', message="Set the periodicity of your habit to either Daily or weekly :", choices=['Daily', 'Weekly']),
            ]

            periodicity = inquirer.prompt(periodicity_choice)
            habit_periodicity = periodicity["habit_periodicity"]
            print('\x1b[6;30;42m' + "You set the periodicity to ", periodicity["habit_periodicity"] + '\x1b[0m')
            print('\x1b[6;30;42m' + f"'{habit_name}'CONGRATULATIONS! YOU HAVE NOW SUCCESSFULLY CREATED A HABIT" + '\x1b[0m')
            print("\n")

            habit = Habit(habit_name, habit_goal, habit_periodicity)
            habit.create_new_habit(connection)
            main()
            
            
             # Marking a habit as completed
        elif choice == "Mark your habit as completed(Check-off habit)":

            habit_name = input("Enter the name of the habit you wish to mark as completed : ")
            habit_periodicity = get_period(connection, habit_name)

            while not re.match("^[a-z A-Z]+$", habit_name):
                print('\x1b[6;30;42m' + "Please enter TEXT ONLY" + '\x1b[0m')
                habit_name = input("Enter the name of the habit you wish to mark as completed : ")

            if check_if_habit_exists(connection, habit_name):
                print('\x1b[6;30;42m' + "can't check-off as your input is non-existant" + '\x1b[0m')
                print("\n")
            else:
                habit = Habit(habit_name, "NULL", habit_periodicity)
                habit.checkoff_habit(connection)
                main()
                
                
                  # analyze your habits
        elif choice == "Analyze your habits":

            analytics_choice = [
                inquirer.List('analyze', message="Select your desirable analytical option among the following : ", choices=[
                    '* Display all of my created habits',
                    '* Display habits which are of the same periodicity.',
                    '* Display the habit which has the longest streak.',
                    '* Display the longest streak of a specific habit.',
                    

                ])
            ]
            analytics = inquirer.prompt(analytics_choice)

            if analytics["analyze"] == '* Display all of my created habits':
                return return_all_habits_data(connection)

            elif analytics["analyze"] == '* Display habits which are of the same periodicity.':
                periodicity_choice = [
                    inquirer.List('habit_periodicity', message="select the  periodicity to analyze", choices=['Daily', 'Weekly']),
                ]

                periodicity = inquirer.prompt(periodicity_choice)
                period = periodicity["habit_periodicity"]
                print('\x1b[6;30;42m' + "you selected", periodicity["habit_periodicity"] + '\x1b[0m')
                print("\n")
                return return_habits_with_same_periodicity(connection, habit_periodicity)

            elif analytics["analyze"] == '* Display the habit which has the longest streak':
                return return_longest_streak_of_all(connection)

            elif analytics["analyze"] == '* Display the longest streak of a specific habit.':

                get_name = [
                    inquirer.Text('name', message="Enter name of the habit")
                ]
                hb_name = inquirer.prompt(get_name)
                habit_name = hb_name["name"]
                return return_longest_streak_of_habit(connection, habit_name)

            
        # Deletes your habit
        elif choice == "Delete your habit":

            habit_name = input("Enter the name of the habit you wish to delete: ")

            while not re.match("^[a-z A-Z]+$", habit_name):
                print('\x1b[6;30;42m' + "Please enter TEXT ONLY" + '\x1b[0m')
                habit_name = input("Enter the name of the habit you wish to delete: ")

            habit = Habit(habit_name, "NULL", "NULL")

            if check_if_habit_exists(connection, habit_name):
                print('\x1b[6;30;42m' + " deletion of habit is unsuccessful as the User's input is non-existant" + '\x1b[0m')
                main()
            else:
                habit.remove_habit(connection)
                print('\x1b[6;30;42m' + f"'{habit_name}' deleted successfully" + '\x1b[0m')
                main()

                if __name__ == '__main__':
    main()

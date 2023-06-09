"""
The analytics module: Gathers, evaluates and displays the analytical data.

Module is called when the user chooses "analyze your habits".
"""
from db import get_habits_data, get_longest_streak, get_longest_streak_of_habit, get_habit_with_periodicity, \
    check_if_habit_exists, get_checked_at, get_longest_streak_of_periodicity

def return_all_habits_data(connection):
    """
    all data of the habits that are currently being tracked
    connection: a connection to a sqlite3 database
    return: list of all habits data
    """

    habits_info = get_habits_data(connection)
    print(f"At present you have {len(habits_info)} habits:")
    print("\n")
    habits_list = []
    for habits in habits_info:
        print(f"Habit Name        : {habits[1]}")
        print(f"Habit Goal : {habits[2]}")
        print(f"Periodicity of habit           : {habits[3]}")
        print(f"Date Created      : {habits[4]}")
        print(f"Streak            : {habits[5]}")
        print("\n")
        habits_list.append(habits)
    return habits_list
  
  
  def return_longest_streak_of_all(connection):
    """
    connection: a connection to a sqlite3 database
    return: the longest streak of all habits
    """
    habits_info = get_longest_streak(connection)
    print("----------Longest streak among all habits----------")

    length_of_habits_list = len(habits_info)
    print(f"You have {length_of_habits_list} habit with longest streak")

    longest_streaks = []
    for habits in habits_info:
        streak = habits[1]
        if streak == 0:
            print("longest streak not found")
            break
        else:
            print("\n")
            print(f"Habit Name              : {habits[0]}")
            print(f"Streak                  : {habits[1]}")
            print("\n")
            longest_streaks.append(habits[1])
    return longest_streaks[0]
  
  
  def return_longest_streak_of_habit(connection, habit_name):
    """
    returns the longest streak of given habit
    connection: a connection to a sqlite3 database
    habit_name: the name of the habit
    return: the longest streak of specific habit
    """
    longest_habit_streak = get_longest_streak_of_habit(connection, habit_name)
    streak = longest_habit_streak
    checked_at = get_checked_at(connection, habit_name)

    if check_if_habit_exists(connection, habit_name):
        print('\x1b[6;30;42m' + "Habit doesn't exists please enter correct habit name" + '\x1b[0m')

    elif not checked_at:
        print('\x1b[6;30;42m' + "habit you entered doesn't have any streak" + '\x1b[0m')

    else:
        logs_list = [i[0] for i in checked_at]
        last_checked = logs_list[-1]
        print("\n")
        print('\x1b[6;30;42m' + f"Longest streak of {habit_name} is {streak} which was last checked on {last_checked}" + '\x1b[0m')
        print("\n")
    return streak
  
  
  def return_habits_with_same_periodicity(connection, habit_periodicity):
    """
    returns the habits with same periodicity
    connection: a connection to a sqlite3 database
    habit_periodicity: periodicity of the habit
    return: list of all habits with specific periodicity
    """

    habits_info = get_habit_with_periodicity(connection, habit_periodicity)

    if len(habits_info) == 0:
        print('\x1b[6;30;42m' + f"no '{habit_periodicity}' habits found" + '\x1b[0m')
    else:
        print('\x1b[6;30;42m' + f"Your List of {habit_periodicity} habits are:" + '\x1b[0m')

        habit_names = []

        for habits in habits_info:
            print(f"------------------{habits[1]}-------------------")
            print(f"Habit Goal : {habits[2]}")
            print(f"Date Created      : {habits[4]}")
            print(f"Streak            : {habits[5]}")
            print("\n")
            habit_names.append(habits[1])
        return habit_names

      
    

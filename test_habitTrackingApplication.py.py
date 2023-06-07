import pytest
from db import connect_db, insert_habit_into_db, check_off_habit, get_streak, get_habit_name, \
    delete_habit, check_if_habit_exists, add_predefined_habits, update_habit_streak
from analytics import return_all_habits_data, return_longest_streak_of_habit, return_longest_streak_of_all
 
import os
from datetime import datetime, timedelta

class TestHabitTracker:

    db = None

    def setup_method(self):
        self.db = connect_db(name="test.db")
        add_predefined_habits(self.db)

    def test_create_checkoff_update(self):
        insert_habit_into_db(self.db, "Excercise", "Do excercise daily", "Daily")
        insert_habit_into_db(self.db, "Learn Flute", "go to Flute classes weekly", "Weekly")

        # checks if habit is successfully inserted into database
        assert check_if_habit_exists(self.db, "Excercise") is False
        assert check_if_habit_exists(self.db, "Learn Flute") is False

        # test check-off and update habit methods in db.py file
        check_off_habit(self.db, "Excercise", "Daily", 1, "2023-06-05 00:00:00")
        update_habit_streak(self.db, "Excercise", 1)
        check_off_habit(self.db, "Learn Flute", "Daily", 1, "2023-06-05 00:00:00")
        update_habit_streak(self.db, "Learn Flute", 1)

        assert get_streak(self.db, "Excercise") == 1
        assert get_streak(self.db, "Learn Flute") == 1
        
        
        
    def test_all_habit_class_methods(self):

        # creating Habit objects with Habit class and testing all habit functions
        daily_habit = Habit("Cooking", "Cooking breakfast", "Daily")
        daily_habit.create_new_habit(self.db)
        # test if habit is created
        assert get_habit_name(self.db, "cooking")

        # tests if streak can get incremented twice a day,
        # im calling checkoff_habit method twice but streak gets incremented only 1 time
        daily_habit.checkoff_habit(self.db)
        daily_habit.checkoff_habit(self.db)

        # checkoff_method called twice but streak is only one
        assert get_streak(self.db, "Cooking") == 1

        # to increments streak again you need to wait 1 day, so change today to tomorrow and test the checkoff_habit method again
        test_date = datetime.now().date() + timedelta(days=1)
        daily_habit.checkoff_habit(self.db, test_date)

        # test if streak of "playing" is 2 now
        assert get_streak(self.db, "Cooking") == 2

        # TESTING WEEKLY HABITS
        weekly_habit = Habit("Coding", "Learn coding", "Weekly")
        weekly_habit.create_new_habit(self.db)
        assert get_habit_name(self.db, "Coding")

        # tests if streak can be increments twice in a week, expected: increases only once a week
        weekly_habit.checkoff_habit(self.db)
        weekly_habit.checkoff_habit(self.db)

        assert get_streak(self.db, "Coding") == 1

        # changing date to next week to test if checkoff_method works as expected
        test_date = datetime.now().date() + timedelta(days=7)
        weekly_habit.checkoff_habit(self.db, test_date)

        assert get_streak(self.db, "Coding") == 2

        # test remove habit
        daily_habit.remove_habit(self.db)
        assert get_habit_name(self.db, "Cooking") is None

        weekly_habit.remove_habit(self.db)
        assert get_habit_name(self.db, "Coding") is None
        
        
        
         def test_get_all_defined_habits(self):
        # four habits were already pre-defined in db.py
        all_habits = return_all_habits_data(self.db)
        assert len(all_habits) == 4

    def test_longest_streak(self):
        # the longest streak of all habits
        longest_streak_of_all_habits = return_longest_streak_of_all(self.db)

        # the longest streak of specific habit
        longest_streak_of_habit = return_longest_streak_of_habit(self.db, "Community Service"")

        # Gym has the longest streak of all (5)
        assert longest_streak_of_all_habits == 5
        # longest streak of Community Service is 3
        assert longest_streak_of_habit == 3

    def test_get_habit_with_period(self):
        # get daily habits
        get_habits_with_same_periodicity_daily = return_habits_with_same_periodicity(self.db, "Daily")
        daily_list = ["Maintain a Diary", "Gym"]
        assert set(get_habits_with_same_periodicity_daily) == set(daily_list)

        # get weekly habits
        get_habits_with_same_periodicity_weekly = return_habits_with_same_periodicity(self.db, "Weekly")
        weekly_list = ["Community Service", "Limit Excessive screen time"]
        assert set(get_habits_with_same_periodicity_weekly) == set(weekly_list)
                                                                 
  

    def test_delete_habit(self):
        delete_habit(self.db, "Limit Excessive screen time")
        assert get_habit_name(self.db, "Limit Excessive screen time") is None
        delete_habit(self.db, "Maintain a Diary")
        assert get_habit_name(self.db, "Maintain a Diary") is None

    def teardown_method(self):
        self.db.close()
        os.remove("test.db")

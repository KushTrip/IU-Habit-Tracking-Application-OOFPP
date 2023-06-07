"""
The database module: Primarily creates database tables, stores information and returns data.
"""
import sqlite3
from datetime import datetime

def create_tables(connection):
    """
    generates the necessary database tables
    connection: a connection to a sqlite3 database
    """
    c = connection.cursor()
    
     c.execute
      ("""
    CREATE TABLE IF NOT EXISTS habits_data
    (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    habit_name TEXT,
    habit_goal TEXT,
    habit_periodicity TEXT,
    date_created DATETIME,  
    streak INTEGER 
    )
    """)
      
          c.execute
        ("""
    CREATE TABLE IF NOT EXISTS habits_tracker 
    (
    habit_name TEXT,
    period TEXT,
    current_streak INTEGER,
    checked_at DATETIME,
    FOREIGN KEY (habit_name) REFERENCES habits_data(habit_name),
    FOREIGN KEY (period) REFERENCES habits_data(period) 
    )
    """)

    connection.commit()
    
    def connect_db(name="main.db"):
    """
    connection :establishes the connection to the sqlite3 database.
    name: the database's title
    return: creates a sqlite3 database and establishes a connection to it.
    """
    connection = sqlite3.connect(name)
    create_tables(connection)
    return connection
  
  def insert_habit_into_db(connection, habit_name, habit_goal, habit_periodicity, streak=0):
    """
    inserts a new habit into the database
    conn: an association with a sqlite3 database
    habit_name: The name of the habit
    habit_description: explanation of the goal of habit
    habit_periodicity: The period of the habit
    streak: streak of the habit
    """
    c = connection.cursor()
    c.execute("SELECT habit_name FROM habits_data WHERE habit_name=?", (habit_name,))
    record = c.fetchone()
    if record:
        print("Habit already exists in database")
    else:
        date_created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        c.execute("INSERT INTO habits_data VALUES (NULL,?,?,?,?,?)",
                  (str(habit_name), str(habit_goal), str(habit_periodicity), date_created, streak))
        connection.commit()
        
        
        def check_off_habit(conn, habit_name, habit_periodicity, current_streak=0, checked_at=None):
    """
    Increases a habit streak by one after checking a habit.
     period: period of the habit
     checked_at: the time when habit was checked-off
     conn: a connection to a sqlite3 database
     habit_name: The name of the habit
     current_streak: current streak of the habit
    """
    if not checked_at:
        checked_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c = connection.cursor()
    c.execute("INSERT INTO habits_tracker VALUES(?,?,?,?)", (habit_name, period, current_streak, checked_at))
    conn.commit()

   
  def update_habit_streak(connection, habit_name, streak):
    """
    updates the streak value in the habits_data table.
    conn: a connection to a sqlite3 database
    habit_name: The name of the habit
    streak: streak of the habit to update
    """
    c = connection.cursor()
    c.execute("UPDATE habits_data SET streak=? WHERE habit_name=?", (streak, habit_name))
    connection.commit()
    
    
    def update_habit_tracker_streak(conn, habit_name, current_streak):
    """
     conn: a connection to a sqlite3 database
     habit_name: The name of the habit
     current_streak: streak of the habit to update
    """
    c = connection.cursor()
    c.execute("UPDATE habits_tracker SET current_streak=? WHERE habit_name=?", (current_streak, habit_name))
    connection.commit()
    
    
    def delete_habit(connection, habit_name):
    """
    Removes the given habit from the database.
    conn: a connection to a sqlite3 database
    habit_name: The name of the habit
    """
    c = connection.cursor()
    c.execute("DELETE FROM habits_data WHERE habit_name=?", (habit_name,))
    c.execute("DELETE FROM habits_tracker WHERE habit_name=?", (habit_name,))
    connection.commit()
    
  
  def check_if_habit_exists(connection, habit_name):
    """
    checks to see if a specific habit is already present in the database.
    connection: a connection to a sqlite3 database
    habit_name: The name of the habit
    return: True, only if the habit already has a record in the database
    """
    c = connection.cursor()
    c.execute("SELECT habit_name FROM habits_data WHERE habit_name=?", (habit_name,))
    record = c.fetchall()
    if not record:
        return True
    else:
        return False
      
    
    def get_habits_data(connection):
    """
    retrieves all habits data from database
    connection: a connection to a sqlite3 database
    return: every entry from the habits_data table
    """
    c = connection.cursor()
    c.execute("SELECT * FROM habits_data")
    return c.fetchall()
  
  
  def get_streak(connection, habit_name):
    """
    retrieve the streak from the habit_data table
    conn: a connection to a sqlite3 database
    habit_name: The name of the habit
    return: streak from habits_data table
    """
    c = conn.cursor()
    c.execute("SELECT streak FROM habits_data WHERE habit_name=?", (habit_name,))
    streaks = c.fetchall()
    return streaks[0][0]
  
  
  def get_period(connection, habit_name):
    c = connection.cursor()
    c.execute("SELECT period FROM habits_data WHERE habit_name=?", (habit_name,))
    return c.fetchall()[0][0]


def get_checked_at(connection, habit_name):
    c = connection.cursor()
    c.execute("SELECT checked_at FROM habits_tracker WHERE habit_name=?", [habit_name])
    return c.fetchall()


def get_longest_streak(connection):
    """
    returns the longest streak of all defined habits
    conn: a connection to a sqlite3 database
    return: the longest streak of all habits in the habits_data table.
    """
    c = connection.cursor()
    c.execute(
        "SELECT DISTINCT habit_name,current_streak FROM habits_tracker WHERE current_streak=(SELECT MAX(current_streak) FROM habits_tracker)")
    return c.fetchall()
  
  
  def get_longest_streak_of_habit(connection, habit_name):
    """
    the longest streak of specific habit
    connection: a connection to a sqlite3 database
    habit_name: The name of the habit
    return: the longest streak from habits_tracker table
    """
    c = connection.cursor()
    c.execute("SELECT MAX(current_streak) FROM habits_tracker WHERE habit_name=?", (habit_name,))
    return c.fetchall()[0][0]


def get_habit_with_periodicity(connection, habit_periodicity):
    """

     connection: a connection to a sqlite3 database
     habit_periodicity: periodicity of habit
     return: habits information with a specific periodicity
    """
    c = connection.cursor()
    c.execute("SELECT * FROM habits_data WHERE habit_periodicity=?", (habit_periodicity,))
    return c.fetchall()
  
  
  def get_longest_streak_of_periodicity(connection, habit_periodicity):
    """
    returns the longest streak of habit with same periodicity
    connection: a connection to a sqlite3 database
    habit_periodicity: duration of habit
    return: the longest streak of habit with specific periodicity
    """
    c = connection.cursor()
    c.execute("SELECT DISTINCT MAX(current_streak),habit_name FROM habits_tracker WHERE habit_periodicity=?", (habit_periodicity,))
    return c.fetchall()


def get_habit_name(connection, habit_name):
    c = connection.cursor()
    c.execute("SELECT habit_name FROM habits_data WHERE habit_name=?", (habit_name,))
    return c.fetchone()

  
  def add_predefined_habits(connection):
    predefined_habits = [
        ("Limit Excessive screen time", "limit your screen time significantly once per week", "Weekly"),
        ("Gym", "Go to the Gym Daily", "Daily"),
        ("Community Service", " Dedicate one day per week to engage in volunteer activities or community service", "Weekly"),
        ("Maintain a Diary", "Write on your Diary Daily", "Daily")
    ]
    for habit in predefined_habits:
        if check_if_habit_exists(connection, habit[0]) is True:
            insert_habit_into_db(connection, habit[0], habit[1], habit[2])

            if habit[0] == "Limit Excessive screen time":
                # Limitation of Screen exposure 4-weeks data
                check_off_habit(connection, "Limit Excessive screen time", "Weekly", 1, "2023-06-05 00:00:00")
                check_off_habit(connection, "Limit Excessive screen time", "Weekly", 1, "2023-06-11 00:00:00")
                check_off_habit(connection, "Limit Excessive screen time", "Weekly", 1, "2023-06-17 00:00:00")
                check_off_habit(connection, "Limit Excessive screen time", "Weekly", 1, "2023-06-24 00:00:00")
                update_habit_streak(connection, "Limit Excessive screen time", 1)

       

            if habit[0] == "Gym":
                # Gym 4-weeks data
                check_off_habit(connection, "Gym", "Daily", 3, "2023-06-05 00:00:00")
                check_off_habit(connection, "Gym", "Daily", 1, "2023-06-06 00:00:00")
                check_off_habit(connection, "Gym", "Daily", 3, "2023-06-07 00:00:00")
                check_off_habit(connection, "Gym", "Daily", 2, "2023-06-08 00:00:00")
                check_off_habit(connection, "Gym", "Daily", 2, "2023-06-19 00:00:00")
                check_off_habit(connection, "Gym", "Daily", 3, "2023-06-24 00:00:00")
                check_off_habit(connection, "Gym", "Daily", 1, "2023-06-28 00:00:00")
                check_off_habit(connection, "Gym", "Daily", 1, "2023-06-29 00:00:00")
                check_off_habit(connection, "Gym", "Daily", 2, "2023-06-30 00:00:00")
                check_off_habit(connection, "Gym", "Daily", 3, "2023-07-01 00:00:00")
                check_off_habit(connection, "Gym", "Daily", 2, "2023-07-02 00:00:00")
                update_habit_streak(connection, "Gym", 2)

                
           if habit[0] == "Community Service":
                # community service 4-weeks data
                check_off_habit(connection, "Community Service", "Weekly", 2, "2023-06-05 00:00:00")
                check_off_habit(connection, "Community Service", "Weekly", 2, "2023-06-11 00:00:00")
                check_off_habit(connection, "Community Service", "Weekly", 3, "2023-06-17 00:00:00")
                check_off_habit(connection, "Community Service", "Weekly", 1, "2023-06-24 00:00:00")
                update_habit_streak(connection, "Community Service", 1)
                
                
            if habit[0] == "Maintain a Diary":
                # Maintain a dairy 4-weeks data
                check_off_habit(connection, "Maintain a Diary", "Daily", 2, "2023-06-05 00:00:00")
                check_off_habit(connection, "Maintain a Diary", "Daily", 3, "2023-06-06 00:00:00")
                check_off_habit(connection, "Maintain a Diary", "Daily", 3, "2023-06-07 00:00:00")
                check_off_habit(connection, "Maintain a Diary", "Daily", 3, "2023-06-08 00:00:00")
                check_off_habit(connection, "Maintain a Diary", "Daily", 2, "2023-06-09 00:00:00")
                check_off_habit(connection, "Maintain a Diary", "Daily", 1, "2023-06-10 00:00:00")
                check_off_habit(connection, "Maintain a Diary", "Daily", 1, "2023-06-15 00:00:00")
                check_off_habit(connection, "Maintain a Diary", "Daily", 2, "2023-06-19 00:00:00")
                check_off_habit(connection, "Maintain a Diary", "Daily", 2, "2023-06-21 00:00:00")
                check_off_habit(connection, "Maintain a Diary", "Daily", 1, "2023-06-22 00:00:00")
                check_off_habit(connection, "Maintain a Diary", "Daily", 1, "2023-06-26 00:00:00")
                check_off_habit(connection, "Maintain a Diary", "Daily", 1, "2023-06-27 00:00:00")
                check_off_habit(connection, "Maintain a Diary", "Daily", 3, "2023-06-28 00:00:00")
                update_habit_streak(connection, "Maintain a Diary", 3)
                
                

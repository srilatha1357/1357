"""
Practice with sequences and dictionaries.

Authors:
  - https://github.com/mihaelasabin
  - https://github.com/sualeh

Implementation requirements:
   1. MUST use a for ... in ... loop
   1. MUST NOT use list comprehensions
   2. MUST NOT use lambda functions
   3. MUST NOT call built-in functions or methods that
      eliminate the use of a for loop
   4. MUST NOT use for ... in ... range(len(...))
"""


class Schedule():
    """
    Represent a class schedule.

    Illustrates methods that transform input collections
        (sequences, dictionaries) into something else.
    """
    def __init__(self, days, classes):
        """
        Make a class schedule.
        """
        self.class_schedule = {}
        self.make_schedule(days, classes)

    def make_schedule(self, days, classes):
        """
        Make a class schedule.

        days: list of days of the week
        classes: list of strings with classes for each day of the week
        Returns: a dictionary to lookup class for a given day of the week

        Example:
        make_schedule(['Mon', 'Tue'], [['Math', 'Bio'], ['Eng']])
        returns
        {'Mon': ['Math', 'Bio'], 'Tue': ['Eng']}
        """
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    def classes_for(self, day):
        """
        Looks up the class for a given day.

        day: string, name of day
        Returns: list of strings, classes for the day,
        or ["Free day"] if there are no classes
        or ["No such day"] if there is no such day of the week

        Example:
        sch = Schedule(['Mon', 'Tue'], [['Math', 'Bio'], ['Eng']])
        sch.classes_for('Mon') returns ['Math', 'Bio']
        sch.classes_for('Sun') returns ["Free day"]
        sch.classes_for('Holiday') returns ["No such day"]
        """
        for classes_for in Schedule:


    def __str__(self):
        """
        Return a printable string representation of the schedule.

        Example:
        sch = Schedule(['Mon', 'Tue'], [['Math', 'Bio'], ['Eng']])
        print(sch)
        will print (on multiple lines)
        Mon: Math, Bio
        Tue: Eng
        """


def main():
    """Run example code. (Tests are in a different module.)"""
    sch = Schedule(['Mon', 'Tue'], [['Math', 'Bio'], ['Eng']])
    print(sch)
    print(f"sch.classes_for('Mon') return {sch.classes_for('Mon')}")
    print(f"sch.classes_for('Sun') return {sch.classes_for('Sun')}")
    print(f"sch.classes_for('Holiday') return {sch.classes_for('Holiday')}")


if __name__ == '__main__':
    main()

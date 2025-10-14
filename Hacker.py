"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
class Hacker:
    def __init__(self, name: str):
        self.__name = name
        self.__inventory = []
        self.__rig = None
        self.__trace_level: int = 0
        self.__trace_threshold: int = 5


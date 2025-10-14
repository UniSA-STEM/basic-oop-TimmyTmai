"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
class Rig:
    def __init__(self, name: str):
        self.__name = name
        self.__damage = 0
        self.__broken = False
        self.__storage = []
        self.__upgrade_level = 0
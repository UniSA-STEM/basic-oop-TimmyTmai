"""
File: Asset.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
class Asset:
    def __init__(self, name: str, description: str, encrypted: bool = False):
        self.__name = name
        self.__description = description
        self.__encrypted = encrypted

    def __str__(self):
        if self.__encrypted:
            return f"{self.__name}, {self.__description} [Encrypted]"
        else:
            return f"{self.__name}, {self.__description}"

    def get_name(self) -> str:
        return self.__name

    def is_encrypted(self) -> bool:
        if self.__encrypted:
            return True
        return False

    def set_encrypted(self):
        self.__encrypted = True


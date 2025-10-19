"""
File: Asset.py
Description: Represents a digital asset in the game world.
Author: Le Tuan Mai
ID: 110439345
Username: maily015
This is my own work as defined by the University's Academic Misconduct Policy.
"""
class Asset:
    def __init__(self, name: str, description: str, encrypted: bool = False):
        self.__name = name
        self.__description = description
        self.__encrypted = encrypted

    # --------- String Representation ---------
    def __str__(self):
        if self.__encrypted:
            return f"{self.__name}, {self.__description} [Encrypted]"
        else:
            return f"{self.__name}, {self.__description}"

        # ---------- Getters ----------

    def get_name(self) -> str:
        """Return the asset's name."""
        return self.__name

    def is_encrypted(self) -> bool:
        """True if the asset is currently encrypted; otherwise False."""
        return self.__encrypted

        # ---------- Setters ----------

    def set_encrypted(self):
        """Mark the asset as encrypted (protected)."""
        self.__encrypted = True

    def set_decrypted(self):
        """Mark the asset as decrypted (movable/transferable)."""
        self.__encrypted = False

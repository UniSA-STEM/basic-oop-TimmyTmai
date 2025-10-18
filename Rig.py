"""
File: Rig.py
Description: Rig (computer) object that can take damage, store assets, be upgraded or repaired,
             and generate/use assets.
Author: Le Tuan Mai
ID: 110439345
Username: maily015
This is my own work as defined by the University's Academic Misconduct Policy.
"""
import random
from Asset import Asset

class Rig:
    def __init__(self, name: str):
        self.__name = name
        self.__damage = 0
        self.__broken = False
        self.__storage: list[Asset] = [
            Asset("Data Spike", "Used in battles."),
            Asset("Data Spike", "Used in battles."),
            Asset("Removable Drive", "Found in rigs and used for extraction."),
        ]
        self.__storage_limit = 6
        self.__upgrade_level = 0
        self.__damage_threshold = 2

        # --------- Getters / Info ---------
    def add_asset(self, asset: Asset, time: int):
        """adds asset to the storage list for testing"""
        i = 0
        while i <= time - 1:
            self.__storage.append(asset)
            i = i + 1

    def get_name(self) -> str:
        """Return rig name."""
        return self.__name

    def get_damage(self) -> int:
        """Return current damage counter."""
        return self.__damage

    def get_assets(self) -> list[Asset]:
        """Return the storage list."""
        return self.__storage

    def get_condition(self):
        """Return current condition."""
        if self.__damage == 0:
            return f"Pristine (Level {self.__upgrade_level})"
        elif self.__damage > 0 and not self.__broken :
            return f"Damaged (Level {self.__upgrade_level})"
        else:
            return f"Broken (Level {self.__upgrade_level})"

    def is_broken(self) -> bool:
        """Return True if rig is broken."""
        return self.__broken

    def reach_limit(self):
        if len(self.__storage) >= self.__storage_limit:
            return True
        else:
            return False

    def display_storage(self):
        """Print all assets currently in storage (for quick checking/debug)."""
        if not self.__storage:
            print("(storage empty)")
            return
        for a in self.__storage:
            print(a)

    def check_asset(self, asset_name: str) -> int:
        """Check if asset is available."""
        for i, a in enumerate(self.__storage):
            if a.get_name() == asset_name:
                return i
        return -1

    # --------- Battle / Damage ---------

    def take_damage(self):
        """Increase damage counter by 1, if damage reaches the threshold mark as broken."""
        if self.__broken:
            return
        self.__damage += 1
        if self.__damage >= self.__damage_threshold:
            self.__broken = True
            print(f"{self.__name} is broken!")

    def launch_data_spikes(self, target_rig):
        """Use one Data Spike to deal 1 damage to the target rig"""
        #Check if broken
        if self.__broken:
            print(f"Cannot launch data spike, Rig is broken")
            return False

        #Check for available Data Spike
        data_index = self.check_asset("Data Spike")
        if data_index == -1:
            print("No Data Spike available to launch")
            return False

        #Consume Data Spike and deal damage
        self.__storage.pop(data_index)
        print("launch successful")
        target_rig.take_damage()
        return True

        # --------- Upgrades / Repair ---------

    def upgrade(self):
        """Increase level by one raise damage threshold and storage's limit"""
        self.__upgrade_level += 1
        self.__damage_threshold += 1
        self.__storage_limit += 1
        print(f"Rig current level: {self.__upgrade_level}")
        print(f"Rig current damage threshold: {self.__damage_threshold}")
        print(f"Rig current storage limit: {self.__storage_limit}")

    def repaired(self):
        """Repair the rig if broken or damaged"""
        if self.__damage == 0:
            print(f"{self.__name}: no repair needed.")
            return False
        self.__damage = 0
        self.__broken = False
        print(f"{self.__name} repaired!")
        return True

    # --------- Storage Operations ---------

    def store(self, asset: Asset):
        """For Hacker to use to store assets"""
        if not self.reach_limit():
            self.__storage.append(asset)
            return
        else:
            print("Storage is full")

    def remove(self, asset: Asset):
        """For Hacker to use to retrieve assets"""
        self.__storage.remove(asset)

    def encrypt_storage(self):
        """Encrypt assets in storage"""
        #Check for available chip
        chip_idx = self.check_asset("Security Chip")
        if chip_idx == -1:
            print("Not enough Security Chip to encrypt assets")
            return
        else:
            self.__storage.pop(chip_idx)

        for a in self.__storage:
            if not a.is_encrypted():
                a.set_encrypted()
        print("Encrypted all assets in storage")


    def decrypt_assets(self):
        """Decrypt assets in storage"""
        chip_idx = self.check_asset("Security Chip")
        if chip_idx == -1:
            print("Not enough Security Chip to encrypt assets")
            return
        else:
            self.__storage.pop(chip_idx)

        for a in self.__storage:
            if a.is_encrypted():
                a.set_decrypted()
        print("Decrypted all assets in storage")

    def generate_assets(self):
        """Generate one random asset, add it to storage"""
        pool = [
            Asset("Hardware Patch", "Used to upgrade rigs."),
            Asset("CryptoToken", "Used to acquire or repair rigs."),
            Asset("Data Spike", "Used in battles."),
            Asset("Removable Drive", "Found in rigs and used for extraction."),
            Asset("Security Chip", "Used to encrypt or decrypt assets.")
        ]
        if not self.reach_limit():
            a = random.choice(pool)
            self.__storage.append(a)
            print(f"Generated one {a.get_name()}")
            return
        else:
            print("Storage is full")

    # --------- String Representation ---------

    def __str__(self):
        name = self.__name
        condition = self.get_condition()
        level= self.__upgrade_level
        header = f"\n##########\n{name.upper()}\nCondition: {condition.upper()}\nUpgrade level: {level}\nStorage:"
        lines = [str(a) for a in self.__storage]
        if len(self.__storage) == 0:
            return f"There are no assets in rig's storage"
        else:
            return header + "\n" + "\n".join(lines)
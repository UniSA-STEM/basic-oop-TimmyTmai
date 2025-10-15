from Asset import Asset
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
        self.__storage: list[Asset] = [
            Asset("Data Spike", "Used in battles."),
            Asset("Data Spike", "Used in battles."),
            Asset("Removable Drive", "Found in rigs and used for extraction.."),
        ]
        self.__upgrade_level = 0
        self.__damage_threshold = 2

#---------Getter--------
    def get_name(self) -> str:
        return self.__name

    def get_damage(self) -> int:
        return self.__damage

    def get_assets(self) -> list[Asset]:
        return self.__storage


    def store(self, asset: Asset):
        self.__storage.append(asset)

    def remove(self, asset: Asset):
        self.__storage.remove(asset)

    def is_broken(self) -> bool:
        return self.__broken

    def display_storage(self):
        for i in self.__storage:
            print(i.get_name())

    def take_damage(self):
        if self.__broken:
            return
        self.__damage += 1
        if self.__damage >= self.__damage_threshold:
            self.__broken = True
            print(f"{self.__name} is broken")

    def launch_data_spikes(self, target_rig):
        if self.__broken:
            print(f"Cannot launch data spike, Rig is broken")
            return

        data_index = None
        for i, d in enumerate(self.__storage):
            if d.get_name() == "Data Spike":
                data_index = i
                break
        if data_index is None:
            print("Not enough Data Spike to launch")
            return
        self.__storage.pop(data_index)
        print("launch successful")
        target_rig.take_damage()

    def upgrade(self):
        self.__upgrade_level += 1
        self.__damage_threshold += 1
        print(f"Rig current level: {self.__upgrade_level}")
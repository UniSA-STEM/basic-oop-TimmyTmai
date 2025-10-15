from Asset import Asset
from Hacker import Hacker
from Rig import Rig

"""
File: main.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

target_rig = Rig("Target Rig")
hacker = Hacker("Hacker123")
hacker.acquire_rig()
hacker.attack(target_rig)
hacker.attack(target_rig)
hacker.extract_assets(target_rig)

hacker.display_inventory()

print(hacker)

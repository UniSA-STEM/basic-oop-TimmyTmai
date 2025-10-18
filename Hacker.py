"""
File: Hacker.py
Description: Represents a hacker who can own a single active rig, maintain an inventory of assets,
    and perform actions like acquiring a rig, attacking, extracting assets, encrypting/decrypting,
    storing/retrieving items, upgrade rig, and repairing their rig.
Author: Le Tuan Mai
ID: 110439345
Username: maily015
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Rig import Rig
from Asset import Asset

class Hacker:
    def __init__(self, name: str):
        self.__name = name
        self.__inventory : list[Asset] = [
            Asset("CryptoToken", "Used to acquire or repair rigs."),
        ]
        self.__rig = None
        self.__trace_level: int = 0
        self.__trace_threshold: int = 5

        # ---------- Simple getters / displays ----------

    def get_rigs(self):
        """Return the currently rig."""
        return self.__rig

    def get_inventory(self) -> list[Asset]:
        """Return inventory list."""
        return self.__inventory

    def display_inventory(self):
        """Print each asset in inventory (for quick checking/debug)."""
        if not self.__inventory:
            print("(inventory empty)")
            return
        for a in self.__inventory:
            print(a)

    def add_asset(self, asset: Asset, time: int):
        """adds asset to the inventory list for testing"""
        i = 0
        while i < time:
            self.__inventory.append(asset)
            i = i + 1

    def set_trace_level(self, level: int):
        """manually set trace level for testing"""
        self.__trace_level = level

        # ---------- Trace / exposure ----------

    def is_exposed(self) -> bool:
        """Return True if the hacker is currently exposed (trace too high)."""
        return self.__trace_level > self.__trace_threshold


    def check_asset(self, asset_name: str) -> int:
        """Check if asset is available."""
        for i, a in enumerate(self.__inventory):
            if a.get_name() == asset_name:
                return i
        return -1

    # ---------- Core actions ----------

    def acquire_rig(self, rig: Rig = None):
        """Acquire a rig using one CryptoToken"""
        #Check if there is Cryptotoken
        token_index = self.check_asset("CryptoToken")
        if token_index == -1:
            print("Not enough tokens to acquire rig")
            return

        # Consume one CryptoToken
        self.__inventory.pop(token_index)

        # Create a default rig if none was provided
        if rig is None:
            rig = Rig("Default Rig")

        self.__rig = rig
        print(f"#### {rig.get_name().upper()} ACTIVATED ####")

    def attack(self, target_rig: Rig):
        """Attacking a target rig using the rig's launch data spike method"""
        if self.is_exposed():
            print("Cannot attack while being exposed")
            return
        if self.__rig is None:
            print("No rig available to attack")
            return

        if self.__rig.launch_data_spikes(target_rig):
            self.__trace_level += 1

        if self.is_exposed():
            print("The Hacker is exposed")

    def extract_assets(self, target_rig: Rig = None):
        """Extract unencrypted assets from a target rig using one Removable Drive"""
        target = target_rig
        rig = self.__rig

        #Check if target rig is broken or None
        if target is None:
            print("Extraction failed: No target rig.")
            return False
        if not target.is_broken():
            print("Target rig is not broken, cannot extract assets.")
            return False

        #Check for Removable Drive
        drive_idx = self.check_asset("Removable Drive")
        if drive_idx == -1:
            print("Not enough Removable Drive to extract assets")
            return False
        self.__inventory.pop(drive_idx)

        # Move unencrypted assets from target rig storage to hacker inventory
        storage = target.get_assets()
        moved = 0
        # Iterate backwards when popping
        for i in range(len(storage) - 1, -1, -1):
            a = storage[i]
            if not a.is_encrypted():
                self.__inventory.append(storage.pop(i)) #Removes asset and append to hacker's inventory
                moved += 1
        print(f"Extracted {moved} assets from {target.get_name()}")
        return True

    def encrypt_inventory(self):
        """Encrypt hacker's inventory using one Security Chip. Encrypted asset cannot be extract, store or retrieve"""
        #Check for security chip
        chip_idx = self.check_asset("Security Chip")
        if chip_idx == -1:
            print("Not enough Security Chip to encrypt assets")
            return
        else:
            self.__inventory.pop(chip_idx)

        #Check if assets not encrypted and encrypt
        for i in self.__inventory:
            if not i.is_encrypted():
                i.set_encrypted()
        print("Encrypted all assets in inventory")


    def decrypt_inventory(self):
        """Decrypt hacker's inventory using one Security Chip"""
        #Check for security chip
        chip_idx = self.check_asset("Security Chip")
        if chip_idx == -1:
            print("Not enough Security Chip to encrypt assets")
            return
        else:
            self.__inventory.pop(chip_idx)

        #Check if asset is encrypted and decrypt
        for i in self.__inventory:
            if i.is_encrypted():
                i.set_decrypted()
        print("Decrypted all assets in inventory")


    def upgrade_rig(self):
        """Upgrade rig using one Hardware Patch and rig's upgrade method"""
        #Check if there is rig
        if self.__rig is None:
            print("No rig to upgrade")
            return

        #Check for Hardware Patch
        patch_idx = self.check_asset("Hardware Patch")
        if patch_idx == -1:
            print("Not enough Hardware Patch to upgrade rig")
            return

        self.__inventory.pop(patch_idx)
        self.__rig.upgrade()

    def scan(self,asset_name: str):
        """Find asset by name remove it and return it, None if no match."""
        assets = self.__inventory
        for i,asset in enumerate(self.__inventory):
            if asset.get_name() == asset_name:
                return self.__inventory.pop(i)
        return None

    def store(self, asset_name: str | None = None):
        """Store all unencrypted assets or specific asset by name using rig's store method"""
        # Check if hacker is exposed
        if self.is_exposed():
            print("Cannot transfer items while being exposed")
            return

        # Check if there is rig
        if self.__rig is None:
            print("Store failed: No rig available.")
            return
        rig = self.__rig

        moved = 0

        # Move all assets if hacker doesn't specify
        if asset_name is None:
            # iterate backwards so popping/removing is safe
            for i in range(len(self.__inventory) - 1, -1, -1):
                asset = self.__inventory[i]
                if asset.is_encrypted():
                    print(f"Cannot move encrypted asset ({asset.get_name()})")
                    continue
                rig.store(asset)
                self.__inventory.pop(i)
                moved += 1

            if moved > 0:
                print("Moved all unencrypted items to rig's storage")
                self.__trace_level += 1
            else:
                print("No unencrypted assets to store")
            return

        # Move asset by name
        asset = self.scan(asset_name)  # removes first match from inventory
        if asset:
            if asset.is_encrypted():
                print(f"Cannot move encrypted asset ({asset_name})")
                self.__inventory.append(asset)  # put back since blocked
                return
            rig.store(asset)
            print(f"Moved {asset_name} to rig's storage")
            self.__trace_level += 1
        else:
            print(f"No matching asset found to store: '{asset_name}'")

    def retrieve(self, asset_name: str | None = None):
        # Check if hacker is exposed
        if self.is_exposed():
            print("Cannot transfer items while being exposed")
            return

        # Check if there is rig
        if self.__rig is None:
            print("Retrieve failed: No rig available.")
            return
        rig = self.__rig

        storage = rig.get_assets()
        moved = 0

        # Retrieve all assets if hacker doesn't specify
        if asset_name is None:
            # iterate over a copy so removing from storage is safe
            for asset in storage[:]:
                if asset.is_encrypted():
                    print(f"Cannot move encrypted asset ({asset.get_name()})")
                    continue
                self.__inventory.append(asset)
                storage.remove(asset)
                moved += 1

            if moved > 0:
                print("Retrieved all items to hacker's inventory")
                self.__trace_level += 1
            else:
                print("No unencrypted items to retrieve")
            return

        # Retrieve asset by name
        target = asset_name
        found = False
        for asset in storage[:]:
            if asset.get_name() == target:
                found = True
                if asset.is_encrypted():
                    print(f"Cannot move encrypted asset ({target})")
                else:
                    self.__inventory.append(asset)
                    storage.remove(asset)
                    print(f"Retrieved {target} to hacker's inventory")
                    self.__trace_level += 1
                break  # stop after handling the first match

        if not found:
            print(f"No item named '{target}' found in rig storage")

    def repair_rig(self):
        # Check if there is CryptoToken
        token_index = self.check_asset("CryptoToken")
        if token_index == -1:
            print("Not enough tokens to repair rig")
            return
        #Check if there is rig
        if self.__rig is None:
            print("Repair failed: no rig to repair.")
            return
        #Delegate the effect to Rig.repair(); consume token only on success
        rig = self.__rig
        if rig.repaired():
            self.__inventory.pop(token_index)
            return

    # ---------- String representation ----------
    def __str__(self):
        name = self.__name
        rig = self.__rig
        trace = self.__trace_level

        rig_name = rig.get_name().upper() if rig is not None else "NO RIG"
        if self.is_exposed():
            header = f"\n##########\n{name.upper()}\nRig: {rig_name}\nTrace level: {trace} [EXPOSED]\nInventory:"
        else:
            header = f"\n##########\n{name.upper()}\nRig: {rig_name}\nTrace level: {trace}\nInventory:"

        if len(self.__inventory) == 0:
            return header + "\n(inventory empty)"
        else:
            lines = [str(a) for a in self.__inventory]
            return header + "\n" + "\n".join(lines)
from Rig import Rig
from Asset import Asset

class Hacker:
    def __init__(self, name: str):
        self.__name = name
        self.__inventory : list[Asset] = [
            Asset("CryptoToken", "Used to acquire or repair rigs."),
            Asset("Data Spike", "Used in battles.")
        ]
        self.__rig = None
        self.__trace_level: int = 0
        self.__trace_threshold: int = 5


    def get_rigs(self):
        return self.__rig

    def get_inventory(self) -> list[Asset]:
        return self.__inventory

    def display_inventory(self): #use to check hacker's inventory
        for i in self.__inventory:
            print(i.get_name())

    def is_exposed(self) -> bool:
        return self.__trace_level > self.__trace_threshold

    def acquire_rig(self, rig: Rig = None):
        #Check if there is Cryptotoken
        token_index = None
        for i, t in enumerate(self.__inventory):
            if t.get_name() == "CryptoToken":
                token_index = i
                break
        if token_index is None:
            print("Not enough tokens to acquire rig")
            return

        #consume token
        self.__inventory.pop(token_index)
        #instantiated default rig if no rigs passed
        if rig is None:
            rig = Rig("Default Rig")
        self.__rig = rig
        print(f"#### {rig.get_name().upper()} ACTIVATED ####")

    def attack(self, target_rig: Rig):
        if self.is_exposed():
            print("Cannot attack while being exposed")
            return
        if self.__rig is None:
            print("No rig available to attack")
            return

        self.__rig.launch_data_spikes(target_rig)
        self.__trace_level += 1
        if self.is_exposed():
            print("The Hacker is exposed")

    def extract_assets(self, target_rig: Rig = None):
        target = target_rig
        rig = self.__rig

        #Check if rig is broken
        if target is None:
            print("Extraction failed: No target rig.")
            return False
        if not target.is_broken():
            print("Target rig is not broken, cannot extract assets.")
            return False

        #Check for Removable Drive
        drive_idx = None
        #Check rigs inventory
        for idx, item in enumerate(rig.get_assets()):
            if item.get_name() == "Removable Drive":
                drive_idx = idx
                rig.get_assets().pop(drive_idx)
                break

        if drive_idx is None:
            print("Extraction failed: No Removable Drive available.")
            return False

        storage = target.get_assets()
        moved = 0
        for i in range(len(storage) - 1, -1, -1):
            a = storage[i]
            if not a.is_encrypted():
                self.__inventory.append(storage.pop(i)) #Removes asset and append to hacker's inventory
                moved += 1
        print(f"Extracted {moved} assets from {target.get_name()}")
        print("Hacker's Inventory:")
        self.display_inventory()
        return True

    def encrypt_assets(self, asset: Asset):
        pass

    def upgrade_rig(self):
        patch_idx = None
        rig = self.__rig
        for idx, p in enumerate(self.__inventory):
            if p.get_name() == "Hardware Patch":
                patch_idx = idx
                self.__inventory.pop(patch_idx)
                rig.upgrade()

        if patch_idx is None:
            print("Upgrade failed: No Hardware Patch available.")

    def scan(self,asset_name: str):
        assets = self.__inventory
        for i,asset in enumerate(self.__inventory):
            if asset.get_name() == asset_name:
                return self.__inventory.pop(i)
        return None

    def store(self, asset_name: str | None = None):
        if self.is_exposed():
            print("Cannot transfer items while being exposed")
            return

        rig = self.__rig

        if self.__rig is None:
            print("Store failed: No rig available.")
            return False

        if asset_name is None:
            for asset in self.__inventory:
                rig.store(asset)
            self.__inventory = []
            print("Moved all items to rig's storage")
        else:
            asset = self.scan(asset_name)
            if asset:
                rig.store(asset)
                print(f"Moved {asset_name} to rig's storage")
        self.__trace_level += 1

    def retrieve(self, asset_name: str | None):
        if self.is_exposed():
            print("Cannot transfer items while being exposed")
            return

        rig = self.__rig
        if asset_name is None:
            for asset in rig.get_assets():
                self.__inventory.append(asset)
            print("Retrieved all items to hacker's inventory")
        else:
            for asset in rig.get_assets():
                if asset.get_name() == asset_name:
                    self.__inventory.append(asset)
                    rig.remove(asset)
                    print(f"Retrieved {asset_name} to hacker's inventory")
        self.__trace_level += 1

    def __str__(self):
        name = self.__name
        rig = self.__rig
        trace = self.__trace_level
        header = f"\n##########\n{name.upper()}\nRig: {rig.get_name().upper()}\nTrace level: {trace}\nInventory:"
        lines = [str(a) for a in self.__inventory]
        if len(self.__inventory) == 0:
            return f"There are no assets in hacker's inventory"
        else:
            return header + "\n" + "\n".join(lines)
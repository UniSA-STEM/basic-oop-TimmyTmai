"""
File: main.py
Description: Import classes and instantiate hackers, rigs, and assets. Simulate battles, upgrades, encryption, and trace management.
            Include edge cases
Author: Le Tuan Mai
ID: 110439345
Username: maily015
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Asset import Asset
from Hacker import Hacker
from Rig import Rig

hardware_patch = Asset("Hardware Patch","Used to upgrade rigs.")
crypto_token =  Asset("CryptoToken","Used to acquire or repair rigs.")
data_spike =  Asset("Data Spike","Used in battles.")
removable_drive =  Asset("Removable Drive","Found in rigs and used for extraction.")
security_chip =  Asset("Security Chip","Used to encrypt or decrypt assets.", True)

print("========== STARTING MAIN TEST SUITE ==========\n")

# ---------- 1. Create Hacker and Default Inventory ----------
hacker = Hacker("ZeroCool")
print("Initial hacker state:")
print(hacker)

# ---------- 2. Acquire a rig (consume CryptoToken) ----------
print("\n--- Test 1: Acquire Rig ---")
hacker.acquire_rig()
print(hacker)

# ---------- 3. Check Rig’s status and display contents ----------
rig = hacker.get_rigs()
print("\n--- Test 2: Rig condition and storage ---")
print(rig.get_condition())
rig.display_storage()

# ---------- 4. Attack sequence ----------
print("\n--- Test 3: Attack another rig ---")
enemy_rig = Rig("Target Rig")
print("Before attack:", enemy_rig.get_condition())
hacker.attack(enemy_rig)
print("After attack:", enemy_rig.get_condition())
hacker.attack(enemy_rig)
print("Broke the enemy rig:", enemy_rig.get_condition())

# ---------- 5. Damage and repair ----------
print("\n--- Test 4: Rig takes enough damage and repair ---")
rig.take_damage()
rig.take_damage()  # Should break now
print(rig.get_condition())
hacker.add_asset(crypto_token,1)
hacker.repair_rig()          # Repair own rig if damaged
print(rig.get_condition())

# ---------- 6. Asset extraction from broken rig ----------
print("\n--- Test 5: Extract assets from a broken target ---")
hacker.add_asset(removable_drive,1)
hacker.extract_assets(enemy_rig)

# ---------- 7. Encrypt and decrypt all hacker assets ----------
print("\n--- Test 6: Encryption & Decryption ---")
print("Before encryption:")
hacker.display_inventory()
hacker.add_asset(security_chip,2)
hacker.encrypt_inventory()
print("\nAfter encryption:")
hacker.display_inventory()
hacker.decrypt_inventory()
print("\nAfter decryption:")
hacker.display_inventory()

# ---------- 8. Store and Retrieve items ----------
print("\n--- Test 7: Store and Retrieve ---")
hacker.add_asset(hardware_patch,1)
print("Hacker's storage")
hacker.display_inventory()
print("\nStore all items into rig:")

hacker.store()               # Store everything unencrypted
print("\nRig storage now:")
rig.display_storage()
print("\nRetrieve one 'Removable Drive':")
hacker.retrieve("Removable Drive")
print("\nRetrieve all remaining:")
hacker.retrieve()
print("\nRig storage")
rig.display_storage()


# ---------- 9. Upgrade rig ----------
print("\n--- Test 8: Upgrade Rig ---")
# Add a patch manually to inventory first
hacker.get_inventory().append(hardware_patch)
hacker.upgrade_rig()
print(rig.get_condition())

# ---------- 10. Generate new asset in rig ----------
print("\n--- Test 9: Rig generates asset ---")
rig.generate_assets()
rig.display_storage()

# ---------- 11. Encrypt/Decrypt rig storage ----------
print("\n--- Test 10: Encrypt/Decrypt Rig Storage ---")
rig.add_asset(security_chip,2)
rig.encrypt_storage()
rig.display_storage()
rig.decrypt_assets()
rig.display_storage()

# ---------- 12. Edge Case: Try to attack without rig ----------
print("\n--- Edge Case 1: Attack without rig ---")
temp_hacker = Hacker("NoRigMan")
temp_hacker.attack(enemy_rig)

# ---------- 13. Edge Case: Try to acquire rig with no CryptoToken ----------
print("\n--- Edge Case 2: Acquire rig without tokens ---")
temp_hacker.get_inventory().clear()   # Remove everything
temp_hacker.acquire_rig()

# ---------- 14. Edge Case: Try to extract from intact rig ----------
print("\n--- Edge Case 3: Extract from intact rig ---")
intact_rig = Rig("Healthy Rig")
hacker.extract_assets(intact_rig)

# ---------- 15. Edge Case: Encrypt/Decrypt without Security Chip ----------
print("\n--- Edge Case 4: Encrypt without chips ---")
# Clear chips from inventory
inv = hacker.get_inventory()
inv[:] = [a for a in inv if a.get_name() != "Security Chip"]
hacker.encrypt_inventory()

# ---------- 16. Edge Case: Repair undamaged rig ----------
print("\n--- Edge Case 5: Repair undamaged rig ---")
rig.repaired()

# ---------- 17. Edge Case: Rig launching spikes while broken ----------
print("\n--- Edge Case 6: Launch from broken rig ---")
rig.take_damage()
rig.take_damage()  # Force break
rig.take_damage()
rig.add_asset(data_spike,1)
hacker.attack(enemy_rig)

# ---------- 18. Edge Case: Moving encrypted asset ----------
print("\n--- Edge Case 7: store encrypted assets ---")
print("\nHacker's storage")
hacker.add_asset(security_chip,2)
hacker.encrypt_inventory()
hacker.store()
hacker.decrypt_inventory()

# ---------- 19. Edge Case: Attack with high trace ----------
print("\n--- Edge Case 8: Attack while exposed ---")
hacker.set_trace_level(6)
print(hacker)
hacker.attack(enemy_rig)
hacker.set_trace_level(0)

# ---------- 20. Edge Case: Store more assets than storage's limit ----------
print("\n--- Edge Case 9: Exceed storage limit ---")
hacker.display_inventory()
hacker.add_asset(removable_drive,3)
print('\n Transferring Assets....')
hacker.store()
print("\n Rig storage")
rig.display_storage() #Storage limit 7 assets for Level 1 rig
rig.generate_assets()
hacker.display_inventory()
print("\n========== TEST SUITE COMPLETE ==========")



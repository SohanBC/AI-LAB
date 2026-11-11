# 1. Environment Setup
# 'A' and 'B' represent two rooms. 
# 1 = Dirty, 0 = Clean
environment = {"A": 1, "B": 1} 

vacuum_location = "A" 

print(f"Starting Simulation...")
print(f"Initially :- {environment}")


while environment["A"] == 1 or environment["B"] == 1:
    print(f"--- Vacuum is currently in Room {vacuum_location} ---")
    
    # Condition 1: If the current room is dirty, clean it
    if environment[vacuum_location] == 1:
        print(f"Room {vacuum_location} is DIRTY. Cleaning...")
        environment[vacuum_location] = 0  # Change status to Clean
        print(f"Room {vacuum_location} is now CLEAN.")
    else:
        print(f" Room {vacuum_location} is already CLEAN.")
        
    # Condition 2: Movement logic between Room A and Room B
    if vacuum_location == "A":
        print("Moving right to Room B.")
        vacuum_location = "B"
    else:
        print("⬅Moving left to Room A.")
        vacuum_location = "A"
    
    print(f"Current Environment State: {environment}\n")

print("All rooms are clean.")
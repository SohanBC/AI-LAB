rooms = ["A", "B", "C"]
environment = {"A": "Dirty", "B": "Dirty", "C": "Dirty"}
memory = {"A": "Unknown", "B": "Unknown", "C": "Unknown"}

battery = 100 

current_location = "A"


while memory != {"A": "Clean", "B": "Clean", "C": "Clean"}:
    
    status = environment[current_location]
    memory[current_location] = status
    print(f"Room {current_location} is {status}. Memory: {memory} , battery : {battery}")


    if status == "Dirty":
        environment[current_location] = "Clean"
        memory[current_location] = "Clean"
        battery -=20
        print("-> Action: Suck")
    else:
        current_index = rooms.index(current_location)
        next_index = (current_index + 1) % len(rooms)
        current_location = rooms[next_index]
        print(f"-> Action: Move to Room {current_location}")
    print("-" * 45)

print("\nGoal achieved! All rooms are clean.")
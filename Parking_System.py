import heapq
import sys

file = open(sys.argv[1], 'r+')

slots_pq = []   # Priority queue for giving nearest slot
age_map = {}
slot_map = {}
vehicle_map = {}
parking_created = False     # Parking creation allowed only once

for line in file.readlines():
    line = line.strip()
    tup = line.split(" ")   # Splitting the commands and other information
    command = tup[0]

    if command == "Create_parking_lot" and not parking_created:
        # Adding all the slots to the Min Heap
        for i in range(int(tup[1])):
            slots_pq.append(i+1)
        heapq.heapify(slots_pq)
        print("Created parking of {} slots".format(tup[1]))

    elif command == "Park":
        if len(slots_pq) == 0:
            print("Parking full")
            continue
        slot = heapq.heappop(slots_pq)  # It will always return nearest slot
        vehicle_number = tup[1]
        age = tup[3]

        if age not in age_map:
            age_map[age] = set()
        age_map[age].add(slot)
        slot_map[slot] = (age, vehicle_number)
        vehicle_map[vehicle_number] = slot
        print("Car with vehicle registration number \"{0}\" has been parked at slot number {1}".format(vehicle_number, slot))
    
    elif command == "Slot_numbers_for_driver_of_age":
        age = tup[1]
        slot_set = age_map.get(age, "")
        slots = ",".join(list(map(str, slot_set)))
        print(slots)
    
    elif command == "Leave":
        slot = int(tup[1])
        if slot not in slot_map:
            print("Slot already empty")
            continue
        age, vehicle_number = slot_map[slot]
        age_map[age].remove(slot)
        del slot_map[slot]
        del vehicle_map[vehicle_number]
        heapq.heappush(slots_pq, slot)  # When slot is vacated, we will push it back to Heap
        print("Slot number {0} vacated, the car with vehicle registration number \"{1}\" left the space, the driver of the car was of age {2}".format(slot, vehicle_number, age))
    
    elif command == "Vehicle_registration_number_for_driver_of_age":
        age = tup[1]
        if age not in age_map:
            print("No driver is of age: "+age)
            continue
        slots = slot_map[age]
        vehicle_numbers = []
        for slot in slots:
            vehicle_numbers.append(slot_map[slot][1])
        print(",".join(vehicle_numbers))

    elif command == "Slot_number_for_car_with_number":
        vehicle_number = tup[1]
        if vehicle_number in vehicle_map:
            print(vehicle_map[vehicle_number])
        else:
            print(vehicle_number+" is not parked in the parking lot")

    else:
        print("Wrong command")
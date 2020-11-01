# Parking

All the sets and maps used are unordered, to give O(1) access time

## Variable Description

### We will store all the information in one container and all the other information can be gathered as an intersection of two

slots_pq: Priority Heap for slot: n  
age_map = map<age, set(slot)> : It will have age as key and a set of all slots to that age as value  
slot_map = vector<slot, set(age, car_number)>: It will have information on car as value and slot number as key  
vehicle_map = map<vehicle, slot>: It will have vehicle number as key and its slot number as value  

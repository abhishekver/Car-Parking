# Parking

All the sets and maps used are unordered, to give O(1) access time

## Variable Description

### We will store all the information in one container and all the other information can be gathered as an intersection of two

slots_pq: Priority Heap for slot: n  
age_map = map<age, set(slot)> : It will have age as key and a set of all slots to that age as value  
slot_map = vector<slot, set(age, car_number)>: It will have information on car as value and slot number as key  
vehicle_map = map<vehicle, slot>: It will have vehicle number as key and its slot number as value  


## How to Run

1. Clone the application on local system
2. Make sure, you’ve python installed on your system
3. It’ll be there in Linux and Mac, for Windows, visit: https://www.python.org/downloads/ . You can choose any version
4. Open terminal
5. Type command: cd <Download_location>/CarParking
6. Next type:  python Parking_System.py <name_of_the_testcase_file>
7. Output will be displayed on the console itself


contacts = {
    "dilan": "9783657282",
    "rajesh": "9947846370",
    "vinay": "7478643934"
}


contacts["ragav"] = "9947499383"  
contacts["karthik"] = "9947556434"  



get_number1 = contacts.get("dilan", "Contact not found")

get_number2 = contacts.get("vijay", "Contact not found")

print("--- Digital Rolodex ---")
for name, phone in contacts.items():
    print(f"Contact: {name} , Phone: {phone}")

print(f"Searching for number1: {get_number1}")
print(f"Searching for number2: {get_number2}")


#task2

raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]
u_users = set(raw_logs)    
is_present = "ID05" in u_users
print(f"Is 'ID05' present in unique_users? {is_present}")


print(f"Original list length: {len(raw_logs)}")
print(f"Unique set length: {len(u_users)}")
print(f"Unique User IDs: {u_users}")


#task3
friend_a = {"Python", "Cooking", "Hiking", "Movies"}
friend_b = {"Hiking", "Gaming", "Photography", "Python"}


shared_interests = friend_a & friend_b

all_interests = friend_a | friend_b

only_friend_a = friend_a - friend_b


print(f"Same  interests: {shared_interests}")
print(f"Unique Interests (Union):    {all_interests}")
print(f"Only Friend A :      {only_friend_a}")




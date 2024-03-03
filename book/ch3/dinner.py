#3-4
guests = ["Donald Duck", "Micky Mouse", "Daisy Duck"]
print(f"Dear {guests[0]}, you are invited to a dinner at me today at 7 o'clock.")
print(f"Dear {guests[1]}, you are invited to a dinner at me today at 7 o'clock.")
print(f"Dear {guests[2]}, you are invited to a dinner at me today at 7 o'clock.")
print(len(guests))
#3-5
print()
print(f"{guests[2]} can't come. ")
guests[2] = "Minnie Mouse"

print()
print(f"Dear {guests[0]}, you are invited to a dinner at me today at 7 o'clock.")
print(f"Dear {guests[1]}, you are invited to a dinner at me today at 7 o'clock.")
print(f"Dear {guests[2]}, you are invited to a dinner at me today at 7 o'clock.")
print(len(guests))
#3-6
print()
print("We've got a bigger table")
guests.insert(0, "a")
guests.insert(2, "b")
guests.append("c")

print()
print(f"Dear {guests[0]}, you are invited to a dinner at me today at 7 o'clock.")
print(f"Dear {guests[1]}, you are invited to a dinner at me today at 7 o'clock.")
print(f"Dear {guests[2]}, you are invited to a dinner at me today at 7 o'clock.")
print(f"Dear {guests[3]}, you are invited to a dinner at me today at 7 o'clock.")
print(f"Dear {guests[4]}, you are invited to a dinner at me today at 7 o'clock.")
print(f"Dear {guests[5]}, you are invited to a dinner at me today at 7 o'clock.")
print(len(guests))
#3-7
print()
print("Only two people can be invited")
popped_person_1 = guests.pop(0)
popped_person_2 = guests.pop(1)
popped_person_3 = guests.pop(2)
popped_person_4 = guests.pop(2)

print()
print(f"Dear {popped_person_1}, ")
print("I'm sorry to tell you that you can't be invited, because the new table can't be delivered early enough.")
print(f"Dear {popped_person_2}, ")
print("I'm sorry to tell you that you can't be invited, because the new table can't be delivered early enough.")
print(f"Dear {popped_person_3}, ")
print("I'm sorry to tell you that you can't be invited, because the new table can't be delivered early enough.")
print(f"Dear {popped_person_4}, ")
print("I'm sorry to tell you that you can't be invited, because the new table can't be delivered early enough.")
print(len(guests))

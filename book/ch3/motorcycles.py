motorcycles = []
motorcycles.append("honda")
motorcycles.append("yamaha")
motorcycles.append("suzuki") #adds initial values for list "motorcycles"
print(motorcycles)

motorcycles[0] = "ducati" #swaps honda with ducati at index 0
print (motorcycles)

motorcycles.append("honda") #adds honda at the end of the list
print(motorcycles)

motorcycles.insert(2, "vespa") #adds vespa at index 2
print(motorcycles)

del motorcycles[1] #deletes yamaha at index 1 
print(motorcycles)

popped_motorcycle = motorcycles.pop()
#deletes honda at the end of the list and saves it at a variable
print(motorcycles)
print(popped_motorcycle)

too_expensive = "ducati" #saves ducati at "too_expensive"
motorcycles.remove(too_expensive) #removes ducati by "too_expensive"
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
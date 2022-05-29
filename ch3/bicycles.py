bicycles = ["trek","cannondale","redline","specialized"]

print(bicycles[0].title()) # prints the element of the list "bicycles" at index 0 titeled

print(bicycles[1]) # note that the index is zero-based
print(bicycles[3])
print(bicycles[-1]) # prints the first element from back

message = f"My first bicycle was a {bicycles[0].title()}"
print(message)
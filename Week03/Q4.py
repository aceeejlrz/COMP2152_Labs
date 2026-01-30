monday_class = {"Alice", "Bob", "Charlie", "Diana"}
wednesday_class = {"Charlie", "Diana", "Eve", "Frank"}
monday_class.add("Eve")
print(f"Monday class: {monday_class}")
print(f"Wednesday class: {wednesday_class}")
print(f"Both classes: {monday_class & wednesday_class}")                     # & = Ampersand, shft + 7
print(f"Attended either class: {monday_class | wednesday_class}")            # | = Pipe symbol, shft + \
print(f"Only attended Monday class: {monday_class - wednesday_class}")       # - = Minus sign
print(f"Only attended one class: {monday_class ^ wednesday_class}")          # ^ = Caret, shft + 6
all_students = monday_class | wednesday_class
print(f"Is Monday subset of all Students: ", monday_class <= all_students)

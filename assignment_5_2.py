largest = None
smallest = None
while True :
    string_val = input("Enter a number: ")
    if string_val == "done" :
        break
    try:
        int_val = int(string_val)
    except:
        print("Invalid input")
        continue
    if smallest is None :
        smallest = int_val
    elif smallest > int_val :
        smallest = int_val
    if largest is None :
        largest = int_val
    elif largest < int_val :
        largest = int_val
print("Maximum", largest)
print("Minimum", smallest)
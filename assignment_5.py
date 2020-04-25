num = 0
total = 0.0
while True :
    string_val = input("Enter a number: ")
    if string_val == 'done' :
        break
    try:
        float_value = float(string_val)
    except:
        print("Invalid input")
        continue
    num += 1
    total = total + float_value
print(total,num,total/num)
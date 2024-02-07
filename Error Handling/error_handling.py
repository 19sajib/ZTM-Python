
while True:
    try:
        age = int(input("Enter your age: "))
        age_in_dogs_year = 10/age
        
    except ZeroDivisionError:
        print("enter age greater than 0")
        continue
        
    except ValueError:
        print("Please enter a no.")
        break
    
    except ValueError:
        print("!!!!")
        
    else:
        print(f"thank you, and your age is {age}")
        break
        
    finally:
        print("I will always get printed no matter what :)")
    
    print("can you hear me??????")
    
# printing error 
def division_fn(num1, num2):
    try: 
        return num1/num2
    except (ZeroDivisionError, TypeError) as err:
        print(f'error: {err}')

print(division_fn(1,'0'))
print(division_fn(1,0))
print(division_fn(1,4))
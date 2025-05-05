data = {"a": 10, "b": 20, "c": 30, "d": 40, "e": 50, "f": 60}
value = int(input("Enter a value to check its frequency:"))
count = list(data.values()).count(value)
print(f"The value '{value}' appears {count} time(s) in the dictionary.")

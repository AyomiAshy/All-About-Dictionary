codes = {'Kenya': '00254', 'Nigeria': '00234', 'Ghana': '00233'}
country = input("Enter country name: ")
if country in codes:
    print(f"The code for {country} is {codes[country]}")
else:
    print("Country not found in the dictionary.")
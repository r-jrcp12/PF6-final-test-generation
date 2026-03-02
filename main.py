import requests

def dish_fetch(num):
    response = requests.get("https://api-colombia.com/api/v1/TypicalDish")
    
    if response.status_code != 200:
        return {"error": "Failed to connect to API"}
    
    data = response.json()

    if num < 1 or num > len(data):
        return {"error": "Dish not found"}
    
    dish = data[num - 1]

    return {
        "id": dish.get("id"),
        "name": dish.get("name"),
        "description": dish.get("description")
         }


def main():
    print("Hello learners!")
    print("Colombian Typical Dishes 🇨🇴")
    
    result = dish_fetch(1)
    print(result)

if __name__=="__main__":
   main()



















  



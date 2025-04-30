import json
import requests

def get_all_buildings():
    url = "https://api.pdc.arizona.edu/buildings/simple"
    response = requests.get(url)

    if response.status_code ==  200:
        data = response.json() # get JSON
        with open("buildings.json", "w") as file:
            json.dump(data, file, indent=4)
        return data
    else:
        return []

def get_all_rooms():
    url = "https://api.pdc.arizona.edu/rooms/240"
    response = requests.get(url)

    if response.status_code ==  200:
        data = response.json() # get JSON
        with open("rooms.json", "w") as file:
            json.dump(data, file, indent=4)
        return data

    else:
        return []
    

def get_buildings_by_zip(zip_code):
    data = get_all_buildings()
    result = []
    for item in data:
        if item["zip"] == zip_code:
            result.append(item)

    return result


def get_buildings_by_city(city):
    data = get_all_buildings()
    result = []
    for item in data:
        if item["city"] == city:
            result.append(item)

    return result

def main():
    # To test any task, just delete the comment.
    # Task 1 is running by default.

    # TASK 1
    get_all_buildings()

    # TASK 2
    # zip_code = input("Enter the ZIP code: ")
    # buildings_by_zip = get_buildings_by_zip(zip_code)
    # if buildings_by_zip:
    #     print(json.dumps(buildings_by_zip, indent=4))
    # else:
    #     print("Something went wrong!")

    # TASK 3
    # city = input("Enter the city: ")
    # buildings_by_city = get_buildings_by_city(city)
    # if buildings_by_city:
    #     print(json.dumps(buildings_by_city, indent=4))
    # else:
    #     print("[]")

    # TASK 4
    # get_all_rooms()

    

if __name__ == "__main__":
    main()
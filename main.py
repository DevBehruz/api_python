import requests
from dataclasses import dataclass
from collections import namedtuple
import json

Room = namedtuple("Room", ["key", "name", "city", "number", "bldgName"])

@dataclass
class Building:
    uid: str
    building: str
    bldgNumber: str
    bldgAlpha: str
    name: str
    address: str
    city: str
    state: str
    zip: str
    sortAddress: str
    abbrev: str
    commonName: str
    shortName: str
    status: str
    rooms: list

def get_building_240():
    buildings_url = "https://api.pdc.arizona.edu/buildings/simple"
    response = requests.get(buildings_url)
    if response.status_code != 200:
        print("Failed to get buildings")
        return None

    buildings = response.json()
    for b in buildings:
        if b["bldgAlpha"] == "240":
            return b

    print("Building with bldgAlpha = 240 not found")
    return None

def get_rooms_for_building_240():
    rooms_url = "https://api.pdc.arizona.edu/rooms/240"
    response = requests.get(rooms_url)
    if response.status_code != 200:
        print("Failed to get rooms")
        return []

    room_data = response.json()
    rooms = [Room(
        key=room.get("key"),
        name=room.get("name"),
        city=room.get("city"),
        number=room.get("number"),
        bldgName=room.get("bldgName")
    ) for room in room_data]

    return rooms

import json

def main():

    # Task 5
    building_data = get_building_240()
    if not building_data:
        return

    rooms = get_rooms_for_building_240()

    building = Building(
        uid=building_data["bldgAlpha"],
        building=building_data["building"],
        bldgNumber=building_data["bldgNumber"],
        bldgAlpha=building_data["bldgAlpha"],
        name=building_data["name"],
        address=building_data["address"],
        city=building_data["city"],
        state=building_data["state"],
        zip=building_data["zip"],
        sortAddress=building_data["sortAddress"],
        abbrev=building_data["abbrev"],
        commonName=building_data["commonName"],
        shortName=building_data["shortName"],
        status=building_data["status"],
        rooms=rooms
    )

    # Store in a dictionary by UID
    building_dict = {building.uid: building}

    output_dict = {
        uid: {
            **vars(bldg),
            "rooms": [room._asdict() for room in bldg.rooms]
        }
        for uid, bldg in building_dict.items()
    }

    # Write to JSON file
    with open("building_240.json", "w") as f:
        json.dump(output_dict, f, indent=4)


if __name__ == "__main__":
    main()

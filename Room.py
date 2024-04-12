from enum import Enum

class RoomType(Enum):
    INDIVIDUAL = "Individual"
    DOBLE = "Doble"
    SUITE = "Suite"

class Room:
    def __init__(self, room_type, room_number, room_state, room_price):
        self.set_room_type(room_type)
        self.set_room_number(room_number)
        self.set_room_state(room_state)
        self.set_room_price(room_price)

    def get_room_type(self):
        return self._room_type.value

    def set_room_type(self, room_type):
        if isinstance(room_type, RoomType):
            self._room_type = room_type
        else:
            raise ValueError("Invalid room type.")

    def get_room_number(self):
        return self._room_number

    def set_room_number(self, room_number):
        if isinstance(room_number, int):
            self._room_number = room_number
        else:
            raise ValueError("Room number must be an integer.")

    def get_room_state(self):
        return self._room_state

    def set_room_state(self, room_state):
        if room_state in ["Ocupada", "Desocupada"]:
            self._room_state = room_state
        else:
            raise ValueError("Invalid room state. Must be 'Ocupada' or 'Desocupada'.")

    def get_room_price(self):
        return self._room_price

    def set_room_price(self, room_price):
        if isinstance(room_price, (int, float)) and room_price > 0:
            self._room_price = room_price
        else:
            raise ValueError("Room price must be a positive number.")

    def is_occupied(self):
        return self._room_state == "Ocupada"

    def check_in(self):
        if self.is_occupied():
            return "La habitación ya está ocupada."
        else:
            self.set_room_state("Ocupada")
            return "Check-in realizado con éxito."

    def check_out(self):
        if not self.is_occupied():
            return "La habitación ya está desocupada."
        else:
            self.set_room_state("Desocupada")
            return "Check-out realizado con éxito."


def main():
    #TESTING
    print("=================================================================")
    print("Test Case 1: Create a Room.")
    print("=================================================================")
    room1 = Room(RoomType.DOBLE, 101, "Desocupada" , 150)

    if room1.get_room_type() == "Doble":
        print("Test PASS. The parameter room_type has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if room1.get_room_number() == 101:
        print("Test PASS. The parameter room_number has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if room1.get_room_state() == "Desocupada":
        print("Test PASS. The parameter room_state has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if room1.get_room_price() == 150:
        print("Test PASS. The parameter room_price has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    print("=================================================================")
    print("Test Case 2: Check-in a Room.")
    print("=================================================================")
    room2 = Room(RoomType.DOBLE, 102, "Desocupada", 300)
    check_in_result = room2.check_in()

    if check_in_result == "Check-in realizado con éxito." and room2.is_occupied():
        print("Test PASS. Check-in functionality has been implemented correctly.")
    else:
        print("Test FAIL. Check the method check_in().")


    print("=================================================================")
    print("Test Case 3: Check-out a Room.")
    print("=================================================================")
    # Assuming room2 was checked in from the previous test
    check_out_result = room2.check_out()

    if check_out_result == "Check-out realizado con éxito." and not room2.is_occupied():
        print("Test PASS. Check-out functionality has been implemented correctly.")
    else:
        print("Test FAIL. Check the method check_out().")


    print("=================================================================")
    print("Test Case 4: Attempt Check-in on an Occupied Room.")
    print("=================================================================")
    room3 = Room(RoomType.INDIVIDUAL, 103, "Ocupada", 100)
    check_in_result = room3.check_in()

    if check_in_result == "La habitación ya está ocupada.":
        print("Test PASS. Attempted check-in on an occupied room handled correctly.")
    else:
        print("Test FAIL. Check the method check_in() for occupied rooms.")


    print("=================================================================")
    print("Test Case 5: Attempt Check-out on a Vacant Room.")
    print("=================================================================")
    # Assuming room3 was made vacant from the previous operation or is initially vacant
    room4 = Room(RoomType.DOBLE, 104, "Desocupada", 200)
    check_out_result = room4.check_out()

    if check_out_result == "La habitación ya está desocupada.":
        print("Test PASS. Attempted check-out on a vacant room handled correctly.")
    else:
        print("Test FAIL. Check the method check_out() for vacant rooms.")

if __name__ == "__main__":
    main()
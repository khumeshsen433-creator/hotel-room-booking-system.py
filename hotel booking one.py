# ============================================================
# Project Title : Hotel Room Booking System
# PS Number     : [67]
# Student Name  : Khumesh kumar sen
# Email ID      : khumesh.kimar.sen@rungta.org
# Course        : BCA (AI & ML)
# Section       : [BCA 1A]
# ============================================================


# ------------------------------------------------------------
# 1. CONSTANTS AND ROOM DETAILS
# ------------------------------------------------------------

FILE_NAME = "bookings.txt"
GST_RATE = 0.12

# Room details stored in a dictionary
ROOMS = {
    101: {"type": "Single", "rate": 2000},
    102: {"type": "Double", "rate": 3500},
    201: {"type": "Suite", "rate": 6000},
}

# Current bookings stored as a list of dictionaries
bookings = []


# ------------------------------------------------------------
# 2. FORMAT BILL AMOUNT
# ------------------------------------------------------------

def fmt(amount):
    """Show whole numbers without decimals, else 2 decimals."""
    return str(int(amount)) if amount == int(amount) else f"{amount:.2f}"


# ------------------------------------------------------------
# 3. LOAD BOOKING DATA FROM FILE
# ------------------------------------------------------------

def load_bookings():
    """Load bookings from file at program start."""
    try:
        with open(FILE_NAME, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3 and parts[0].isdigit() and parts[2].isdigit():
                    bookings.append(
                        {"room": int(parts[0]), "guest": parts[1], "nights": int(parts[2])}
                    )
    except FileNotFoundError:
        pass  # first run: no file yet


# ------------------------------------------------------------
# 4. SAVE BOOKING DATA TO FILE
# ------------------------------------------------------------

def save_bookings():
    """Save all bookings to file after every change."""
    with open(FILE_NAME, "w") as f:
        for b in bookings:
            f.write(f"{b['room']},{b['guest']},{b['nights']}\n")


# ------------------------------------------------------------
# 5. FIND BOOKING BY ROOM NUMBER
# ------------------------------------------------------------

def find_booking(room):
    for b in bookings:
        if b["room"] == room:
            return b
    return None


# ------------------------------------------------------------
# 6. DISPLAY AVAILABLE ROOMS
# ------------------------------------------------------------

def view_available():
    available = [
        f"{no} {info['type']} Rs. {info['rate']}"
        for no, info in ROOMS.items()
        if find_booking(no) is None
    ]
    if available:
        print(" | ".join(available))
    else:
        print("No rooms are available.")


# ------------------------------------------------------------
# 7. CALCULATE ROOM BILL AND GST
# ------------------------------------------------------------

def calculate_bill(room, nights):
    base = ROOMS[room]["rate"] * nights
    gst = base * GST_RATE
    return base, gst, base + gst


# ------------------------------------------------------------
# 8. PRINT FINAL BILL
# ------------------------------------------------------------

def print_bill(room, nights):
    base, gst, total = calculate_bill(room, nights)
    print(f"Bill: {fmt(base)} + GST {fmt(gst)} = Rs. {fmt(total)}")


# ------------------------------------------------------------
# 9. BOOK A HOTEL ROOM
# ------------------------------------------------------------

def book_room():
    guest = input("Guest: ").strip()
    if not guest or "," in guest:
        print("Invalid guest name.")
        return

    try:
        room = int(input("Room: "))
    except ValueError:
        print("Invalid room number.")
        return
    if room not in ROOMS:
        print("Invalid room number.")
        return
    if find_booking(room):
        print(f"Room {room} is already booked. Please choose another room.")
        return

    try:
        nights = int(input("Nights: "))
    except ValueError:
        print("Nights must be a number between 1 and 30.")
        return
    if not 1 <= nights <= 30:
        print("Nights must be between 1 and 30.")
        return

    bookings.append({"room": room, "guest": guest, "nights": nights})
    save_bookings()
    unit = "night" if nights == 1 else "nights"
    print(f"Room {room} booked for {guest} | {nights} {unit}")
    print_bill(room, nights)


# ------------------------------------------------------------
# 10. GENERATE BOOKING BILL
# ------------------------------------------------------------

def generate_bill():
    try:
        room = int(input("Room: "))
    except ValueError:
        print("Invalid room number.")
        return
    b = find_booking(room)
    if b is None:
        print(f"No booking found for room {room}.")
        return
    print(f"Guest: {b['guest']} | Room {room} | {b['nights']} night(s)")
    print_bill(room, b["nights"])


# ------------------------------------------------------------
# 11. CANCEL ROOM BOOKING
# ------------------------------------------------------------

def cancel_booking():
    try:
        room = int(input("Cancel: Room: "))
    except ValueError:
        print("Invalid room number.")
        return
    b = find_booking(room)
    if b is None:
        print(f"No booking found for room {room}.")
        return
    bookings.remove(b)
    save_bookings()
    print(f"Booking for room {room} cancelled. Room {room} is now available.")


# ------------------------------------------------------------
# 12. MAIN MENU AND PROGRAM CONTROL
# ------------------------------------------------------------

def main():
    load_bookings()
    while True:
        print("\n--- Hotel Room Booking System ---")
        print("1. Available rooms")
        print("2. Book a room")
        print("3. Generate bill")
        print("4. Cancel booking")
        print("5. Exit")
        choice = input("Choose option: ").strip()

        if choice == "1":
            view_available()
        elif choice == "2":
            book_room()
        elif choice == "3":
            generate_bill()
        elif choice == "4":
            cancel_booking()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-5.")


# ------------------------------------------------------------
# 13. PROGRAM EXECUTION
# ------------------------------------------------------------

if __name__ == "__main__":
    main()
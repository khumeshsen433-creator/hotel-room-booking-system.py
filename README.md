# hotel-room-booking-system.py

**PS No.:** 67
**Student:** Khumesh Kumar Sen
**ERP ID:** 00691
**Course:** Bachelor of Computer Application (BCA)
**University:** Rungta International Skills University, School of Information Technology

A console application written in Python 3 for a hotel. The user can view available rooms, book a room for a guest, cancel a booking and generate the bill. Bookings are saved in `bookings.txt` and loaded again when the program starts.

## Concepts Used

Dictionaries, Lists, Functions, File Handling

## Features

- View available rooms
- Book a room for a guest (1 to 30 nights)
- Generate the bill for a booked room
- Cancel a booking
- Input validation, including protection against double booking
- Bookings saved to `bookings.txt` after every change and loaded at program start

## Room Rates (per night)

| Room | Type   | Rate (Rs.) |
|------|--------|------------|
| 101  | Single | 2000       |
| 102  | Double | 3500       |
| 201  | Suite  | 6000       |

**Bill = (rate x nights) + 12% GST**

## How to Run

Requires Python 3 only (no extra libraries).

```bash
python hotel_booking.py
```

## Menu

```
1. Available rooms
2. Book a room
3. Generate bill
4. Cancel booking
5. Exit
```

## Sample Run

**Booking a room**

```
Choose option: 2
Guest: Amit
Room: 101
Nights: 2
Room 101 booked for Amit | 2 nights
Bill: 4000 + GST 480 = Rs. 4480
```

**Booking an already booked room**

```
Choose option: 2
Guest: Neha
Room: 101
Nights: 3
Room 101 is already booked. Please choose another room.
```

**Viewing rooms and cancelling**

```
Choose option: 1
102 Double Rs. 3500 | 201 Suite Rs. 6000
Choose option: 4
Cancel: Room: 101
Booking for room 101 cancelled. Room 101 is now available.
```

## Test Cases

| # | Scenario | Input | Expected Output | Result |
|---|----------|-------|-----------------|--------|
| 1 | Normal input | Book, Amit, 101, 2 nights | Room 101 booked for Amit \| 2 nights; Bill: 4000 + GST 480 = Rs. 4480 | Pass |
| 2 | Boundary (minimum) | Book, Neha, 102, 1 night | Room 102 booked for Neha \| 1 night; Bill: 3500 + GST 420 = Rs. 3920 | Pass |
| 3 | Invalid input | Book, Neha, 101, 3 nights (101 already booked) | Room 101 is already booked. Please choose another room. | Pass |
| 4 | Different valid scenario | `bookings.txt` has 101 (Amit, 2 nights); view rooms, then cancel 101 | 102 Double Rs. 3500 \| 201 Suite Rs. 6000; Booking for room 101 cancelled. Room 101 is now available. | Pass |

## File Format (`bookings.txt`)

One booking per line: `room,guest,nights`

```
101,Amit,2
102,Neha,1
```

## Project Structure

```
.
├── hotel_booking.py     # source code
├── bookings.txt         # created automatically when the first booking is made
├── README.md
└── Project_Report.docx
```

## Functions

| Function | Purpose |
|----------|---------|
| `load_bookings()` | Reads bookings from `bookings.txt` at start |
| `save_bookings()` | Writes all current bookings to `bookings.txt` |
| `find_booking(room)` | Returns the booking for a room, or `None` |
| `view_available()` | Prints rooms that are not booked |
| `book_room()` | Takes input, validates it, and books the room |
| `calculate_bill(room, nights)` | Returns base amount, GST and total |
| `print_bill(room, nights)` | Prints the bill in the required format |
| `generate_bill()` | Looks up a booking and prints its bill |
| `cancel_booking()` | Removes a booking and saves the file |
| `main()` | Shows the menu and runs the program loop |


class StarCinema:
    hall_list = []

    @classmethod
    def entry_hall(self, hall):
        self.hall_list.append(hall)

class Hall:
    def __init__(self, rows, cols, hall_no):
        self._seats = [['free' for i in range(cols)] for j in range(rows)]
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        StarCinema.entry_hall(self)

    def entry_show(self, show_id, movie_name, time):
        show_info = (show_id, movie_name, time)
        self._show_list.append(show_info)

    def book_seats(self, show_id, seat_list):
        if show_id not in [show[0] for show in self._show_list]:
            print("Invalid show ID")
            return

        for seat in seat_list:
            row, col = seat
            if not (0 <= row < self._rows) or not (0 <= col < self._cols):
                print("Invalid seat")
                return

            if self._seats[row][col] == 'booked':
                print("Seat already booked")
                return

            self._seats[row][col] = 'booked'
            print(f"Seat ({row}, {col}) booked successfully")

    def view_show_list(self):
        for show_info in self._show_list:
            print(f"Show ID: {show_info[0]}, Movie: {show_info[1]}, Time: {show_info[2]}")

    def view_available_seats(self, show_id):
        if show_id not in [show[0] for show in self._show_list]:
            print("Invalid show ID")
            return

        for row_idx, row in enumerate(self._seats):
            for col_idx, seat_status in enumerate(row):
                if seat_status == 'free':
                    print(f"Seat: ({row_idx}, {col_idx}) is available")

    def view_all_shows_today(self):
        print(f"All shows today in Hall {self._hall_no}:")
        self.view_show_list()

    def menu(self):
        while True:
            print("\n1. View all shows today")
            print("2. View available seats")
            print("3. Book ticket")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.view_all_shows_today()
            elif choice == '2':
                show_id = input("Enter show ID: ")
                self.view_available_seats(show_id)
            elif choice == '3':
                show_id = input("Enter show ID: ")
                num_seats = int(input("Enter the number of seats to book: "))
                seat_list = []
                for _ in range(num_seats):
                    row = int(input("Enter row: "))
                    col = int(input("Enter column: "))
                    seat_list.append((row, col))
                self.book_seats(show_id, seat_list)
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")


# Example usage:
hall1 = Hall(rows=5, cols=8, hall_no=1)
hall1.entry_show(show_id='1', movie_name='movie1', time='6:00 PM')
hall1.entry_show(show_id='2', movie_name='movie2', time='9:00 PM')

hall1.menu()
while True:
    print("\n1. View all shows today")
    print("2. View available seats")
    print("3. Book ticket")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        hall1.view_all_shows_today()
    elif choice == '2':
        show_id = input("Enter show ID: ")
        hall1.view_available_seats(show_id)
    elif choice == '3':
        show_id = input("Enter show ID: ")
        num_seats = int(input("Enter the number of seats to book: "))
        seat_list = []
        for i in range(num_seats):
            row = int(input("Enter row: "))
            col = int(input("Enter column: "))
            seat_list.append((row, col))

        hall1.book_seats(show_id, seat_list)
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")

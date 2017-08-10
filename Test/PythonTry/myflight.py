"""Model for Aircraft Flight """

class Flight:
    """ A flight with a particular passenger aircarft."""
    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError("No airline code in '{}'".format(number))

        if not number[:2].isupper():
            raise ValueError("Invalid airline code '{}'".format(number))

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("Invalid route number '{}'".format(number))

        self._number = number
        self._aircraft = aircraft
       
        # self._num_available_seats = num_available_seats
        
         
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter:None for letter in seats} for _ in rows]

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]


    
    def aircraft_model(self):
        return self._aircraft.model()
    
    # def seating_plan(self):
    #     return self._seating_plan()

    def num_available_seats(self):
        return sum( sum(1 for s in row.values() if s is None) for row in self._seating if row is not None)
    


    def _parse_seat(self, seat):
        """Parse a seat designator into a valid row and letter
        
        Args:
            seat: A seat designator such as '12F'.
        
        A tuple containing an integer and a letter string for a row and seat.

        """

        row_numbers, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {}".format(letter))

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid seat row {}".format(row))

        if row not in row_numbers:
            raise ValueError("Invalid row number {}".format(row))
        
        return row, letter

    


    def allocate_seat(self, seat, passenger):
        """Allocate a seat to a passenger
        
        Args:
            seat: A seat designator such as '12C' or '21F'
            passenger: The passenger name.

        Raises:
            ValueError: If the seat is unavailable.

        """
        row, letter = self._parse_seat(seat)

        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} is already occupied.".format(seat))

        self._seating[row][letter] = passenger
    


    def relocate_passenger(self, from_seat, to_seat):
        """Relocate a passenger to a different seat.
        
        Args:
            from_seat: The existing seat designator for a passenger to be moved.
            to_seat: The new seat designator.

        """
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError("No passenge to relocate in seat {}".format(from_seat))
            
        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError("Seat {} is already occupied.".format(to_seat))

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None
    


    def make_boarding_cards(self, card_printer):
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self.number(), self.aircraft_model())



    def _passenger_seats(self):
        """An Iteratable series of passenger seating allocation."""
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield (passenger, "{}{}".format(row, letter))
    


# Aircraft details and seating plan

class Aircraft:
    """."""

    def __init__(self, registration):
        self._registration = registration
    # def __init__(self, registration, model, num_rows, num_seats_per_row):
        # self._registration = registration
        # self._model = model
        # self._num_rows = num_rows
        # self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration


    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(rows)*len(row_seats) 

    def model(self):
        return self._model

 
        # return (range(1, self._num_rows + 1), "ABCDEFGHJKLMNOP"[:self._num_seats_per_row])

class Airbus(Aircraft):
    """."""
    # def __init__(self, registration, model, num_rows, num_seats_per_row):
    #     self._registration = registration
    #     # self._model = model
    #     # self._num_rows = num_rows
    #     # self._num_seats_per_row = num_seats_per_row

    # def registration(self):
    #     return self._registration

    def model(self):
        return "Airbus A319"
        #return self._model

    def seating_plan(self):
        return range(1,26), "ABCDEF"
        #return (range(1, self._num_rows + 1), "ABCDEFGHJKLMNOP"[:self._num_seats_per_row])

       

class Boeing(Aircraft):
    """."""
    # def __init__(self, registration, model, num_rows, num_seats_per_row):
    #     self._registration = registration
    #     # self._model = model
    #     # self._num_rows = num_rows
    #     # self._num_seats_per_row = num_seats_per_row

    # def registration(self):
    #     return self._registration

    def model(self):
        return "Boeing 777"
        #return self._model

    def seating_plan(self):
        return range(1,56), "ABCDEFGHJK"
        #return (range(1, self._num_rows + 1), "ABCDEFGHJKLMNOP"[:self._num_seats_per_row])
    
def make_flights():


    f = Flight("BA859", Airbus("G-RUPT"))
    f.allocate_seat('12A', 'Mark Antony')
    f.allocate_seat('18E', 'James Anderson')
    f.allocate_seat('1B', 'John Conahan')
    f.allocate_seat('15A', 'Jason Smith')
    f.allocate_seat('3F', 'Ron Olster')
    f.allocate_seat('20D', 'Bob Goldenberg')

    g = Flight("AR885", Boeing("M-JDJI"))
    g.allocate_seat('55A', 'Kark Antony')
    g.allocate_seat('37E', 'Mames Anderson')
    g.allocate_seat('29B', 'Hohn Conahan')
    g.allocate_seat('45A', 'Lason Smith')
    g.allocate_seat('36F', 'Won Olster')
    g.allocate_seat('5D', 'Gob Goldenberg')
    
    return f, g

def console_card_printer(passenger, seat, flight_number, aircraft):
    output = "| Name: {0}"      \
             "  Flight: {1}"    \
             "  Seat: {2}"      \
             "  Aircraft: {3}"  \
             "  |".format(passenger,flight_number,seat,aircraft)
    banner = '+' + '-' * (len(output) - 2) + '+'
    border = '|' + ' ' * (len(output) - 2) + '|'
    lines = [banner, border, output, border, banner]
    card = '\n'.join(lines)
    print(card)
    print()


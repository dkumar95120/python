from datetime import datetime, timedelta

def prRed(text): print("\033[91m {}\033[00m" .format(text))
def prGreen(text): print("\033[92m {}\033[00m" .format(text))

class Seat(object):
    def __init__(self, row, number, price):
        self.row=row
        self.number=number
        self.price =price
        self.taken = {}

    def reserve(self, date_time, patron):
        self.taken[str(date_time)] = patron

    def unreserve(self, time):
        self.taken[str(time)] = None

    def is_reserved (self, date_time):
        try:
            taken = self.taken[str(date_time)]
        except:
            taken = None
        return taken

class Show (object):
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration # in hours

class Theatre(object):
    def __init__(self, number):
        self.id = number
        self.show_times = []
        self.seats = []

    def add_seat(self, row, number, price):
        self.seats(Seat(row, number, price))

    def now_playing(self):
        return self.show_times[0]

    def display_show_times(self):
        _, show = self.show_times[0]
        print('\n\t\t\t\t\t',show.title,'Show Times\n')
        show_time = ''
        for date_time, show in self.show_times:
            show_time += '\t'+str(date_time)
            if (len(show_time) > 64):
                print (show_time)
                show_time=''

    def add_show_times (self, show, start_time):
        self.show_times.append((start_time, show))

    def remove_show (self, show):
        self.show = None
        for date_time, event in self.show_times:
            if event.title == show.title:
                self.show_times.remove((date_time, event))

    def seat_map (self, time):
        print('\n\t\t\t\t\tTheatre:',self.id,'Seat Map\n')
        s ='\t'
        for seat in self.seats:
            if (seat.is_reserved(time)):
                s += 'x'
            else:
                s += ' '

            s += seat.row + str(seat.number)
            if len(s) >= 80:
                print(s)
                s='\t'
        if len(s):
            print(s)

class Payment (object):
    def __init__(self, name, type, number, exp, cvv):
        self.name = name
        self.type = type
        self.number = number
        self.exp = exp
        self.cvv = cvv


class Patron (object):
    def __init__(self, name, address, payment_type, number, exp, cvv):
        self.name      = name
        self.address   = address
        self.payment   = Payment(name, payment_type, number, exp, cvv)
        self.show      = None
        self.date_time = None
        self.amount    = 0
        self.confirmation = 0
        self.theatreid = -1
        self.seat      = None

    def book (self, date_time, show, amount, theatreid, seat):
        global confirmation_code
        self.show      = show
        self.date_time = date_time
        self.amount    = amount
        self.theatreid = theatreid
        self.seat      = seat
        confirmation_code = 'Reserved {} {} Theatre:{:2} Seat:{}{:2} for {}'.format(show.title, date_time, theatreid, seat.row, seat.number, self.name)
        self.confirmation = confirmation_code
        return confirmation_code

class Address(object):
    def __init__(self, number, street, city, state, zip):
        self.number = number
        self.street = street
        self.city   = city
        self.state  = state
        self.zip    = zip

class Complex(object):
    def __init__ (self, brand, address):
        self.brand = brand
        self.location = address
        self.theatres=[]
        self.patrons = []

    def add_theatre (self):
        number = len(self.theatres) + 1
        theatre = Theatre(number)
        self.theatres.append(theatre)
        return theatre

    def add_patron (self, name, address, payment_type, number, exp, cvv):
        patron = Patron(name, address, payment_type, number, exp, cvv)
        self.patrons.append(patron)
        return patron

    def update_patron(patron):
        for p in self.patrons:
            if p.name == patron.name:
                self.patrons.remove(p)
                break
        self.patrons.append(patron)


    def show_times(self):
        for theatre in self.theatres:
            theatre.display_show_times()

    def find_seat(self, show, date_time):
        selected_seat = None
        theatreid = -1
        for theatre in self.theatres:
            _, s = theatre.now_playing()
            if show.title == s.title:
                for seat in theatre.seats:
                    if not seat.is_reserved(date_time):
                        theatreid = theatre.id
                        selected_seat = seat
                        break

        if not selected_seat:
            print('Sorry! The show {} at {} is completely sold out!!!'.format(show.title, date_time))

        return theatreid, selected_seat

    def book_my_show(self, patron, show, date_time, amount):            
        theatre_id, seat = self.find_seat(show, date_time)
        if seat:
            seat.reserve(date_time, patron)
            confirmation = patron.book(date_time, show, amount, theatre_id, seat)
            print(confirmation)

        return confirmation


    def show_bookings (self, time):
        for theatre in self.theatres:
            for seat in theatre.seats:
                patron = seat.is_reserved(time)
                if patron:
                    print ('{} {}{} {}'.format(theatre.id, seat.row, seat.number, patron.name))


### Driver for bookmyshow 
amc_address = Address(3111, 'Mission College Blvd', 'Santa Clara', 'CA', 95054)
amc         = Complex('AMC Mercado', amc_address)
movies      = ['Devdas', 'Veer Zaara','Bajirao Mastani', 'Three Idiots', 'Ashiqi 2']
duration    = [3,3,3,2,2]

now = datetime.now()
two_weeks = timedelta(days=14)
for i in range(5):
    # start shows at 12 noon onwards
    start_time = datetime(now.year, now.month, now.day, 12)
    # show first available show from now
    while start_time < now and start_time.hour + duration[i] < 24:
       start_time = datetime(start_time.year, start_time.month, start_time.day, start_time.hour+duration[i])

    first_show = start_time
    theatre=amc.add_theatre()
    show = Show(movies[i], duration[i])

    while start_time - now < two_weeks:
        if start_time.hour+duration[i] > 23: # last show starts at 10pm
            start_time = datetime(start_time.year, start_time.month, start_time.day+1, 12)
        else:
            start_time = datetime(start_time.year, start_time.month, start_time.day, start_time.hour+duration[i])

        theatre.add_show_times(show, start_time)

    for row in list(map(chr, range(65, 91))):
        if row < 'X':
            price = 10
        else:
            price = 20
        for number in range(11,31):
            seat = Seat(row, number, price)
            theatre.seats.append(seat)


home_address = Address(3270,'Sawtooth Court','Westlake Village','CA',91362)
show = Show(movies[0], duration[0])

amc.add_patron('Dharmendra Kumar', home_address, 'Visa', '4100 3100 2100 6768', '0120', '789')
amc.add_patron('Rachana Kumar',    home_address, 'Visa', '4100 3100 2100 6768', '0120', '789')
amc.add_patron('Neha Kumar',       home_address, 'Visa', '4100 3100 2100 6768', '0120', '789')
amc.add_patron('Aayush Kumar',     home_address, 'Visa', '4100 3100 2100 6768', '0120', '789')
home_address = Address(2220,'Laurel Drive','Santa Clara','CA',95050)
amc.add_patron('Gazal Sahai',      home_address, 'Visa', '4100 3100 2100 2220', '0220', '123')
amc.add_patron('Shard Saha',       home_address, 'Visa', '4100 3100 2100 2220', '0220', '123')
home_address = Address(444,'Arboleda Drive','Los Altos','CA',94024)
amc.add_patron('Garima Sahai',     home_address, 'Visa', '4100 3100 2100 4440', '0320', '456')
amc.add_patron('Navneet Aron',     home_address, 'Visa', '4100 3100 2100 4440', '0320', '456')

amc.show_times()

for i,p in enumerate(amc.patrons):
    i = i % 5
    show = Show(movies[i], duration[i])
    amc.book_my_show(p, show, first_show, 10)

for theatre in amc.theatres:
    theatre.seat_map(first_show)

amc.show_bookings(first_show)
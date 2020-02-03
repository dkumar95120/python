from datetime import datetime, timedelta

class Resource(object):
    def __init__ (self, name, floor, bldg, city, country, capacity, vc=False):
        self.name = name
        self.floor = floor
        self.bldg = bldg
        self.city = city
        self.country = country
        self.available = True
        self.capacity = capacity
        self.vc = vc

    def __str__ (self):
        return '{:20} Bldg {:4} Floor {:2} {:10} {:5} VC {:1} Capacity {:3}'.format(self.name, self.bldg, self.floor, self.city, self.country, self.vc, self.capacity)

    def __eq__(self, other):
        return (self.name == other.name and self.floor == other.floor and self.bldg == other.bldg and self.country == other.country)

    def hide (self):
        self.available = False

    def show (self):
        self.available = True

class Facility(object):
    def __init__ (self):
        self.resources = []

    def __contains__(self, resource):
        for res in self.resources:
            if res == resource:
                return True
        return False

    def add_resource (self, name, floor, bldg, city, country, capacity, vc=False):
        exists = False
        new_res = Resource (name, floor, bldg, city, country, capacity, vc)
        if new_res not in self.resources:
            self.resources.append(new_res)
        else:
            print(new_res, 'already exists')

        return new_res

    def remove_resource (self, res):
        if res in self.resources:
            self.resources.remove(res)
            print(resource, 'deleted.')

    def show_resources(self):
        for res in self.resources:
            print(res)

class Reservation (object):
    def __init__(self, resource, fm, to, by_email):
        self.resource = resource
        self.fm       = fm
        self.to       = to
        self.by_email = by_email

    def __eq__ (self, other):
        if self.by_email == other.by_email and self.resource == other.resource:
            if self.fm == other.fm and self.to == other.to:
                return True
        return False

    # prepare print string for this booking
    def __str__ (self):
        return '{:20} reservation From:{} To:{} for {}'.format(self.resource.name, self.fm, self.to, self.by_email)

class Reservation_log (object):
    def __init__(self):
        self.res_list = []

    def __contains__(self, reservation):
        for booking in self.res_list:
            if booking == reservation:
                return True
        return False

    def is_available (self, resource, fm, to):

        available = True

        for booking in self.res_list:
            if (booking.resource == resource) and ((fm < booking.to and to > booking.fm) or (booking.fm < to  and booking.to > fm)):
               available = False
               print('{:20} already booked for {} from {} to {}'.format(resource.name, booking.by_email, booking.fm, booking.to))

        return available

    def make_reservation (self, resource, fm, to, by_email):
        if self.is_available(resource, fm, to):
            new_reservation = Reservation(resource, fm, to, by_email)
            self.res_list.append(new_reservation)
            print(new_reservation)

    def cancel_reservation (self, resource, fm, to, by_email):
        booking = Reservation(resource, fm, to, by_email)
        if booking in self.res_list:
            self.res_list.remove(booking)
            print('cancelled', booking)

    # prune obsolete reservations
    def prune(self):
        now = datetime.now()
        for booking in self.res_list:
            if booking.to < now:
                self.res_list.remove(booking)
                print('Pruned', booking)

    def show_reservations(self):
        for booking in self.res_list:
            print(booking)

### Driver for conference room booking
co = Facility()
c1 = co.add_resource(name='Titanic',          floor=1, bldg=250, city='San Jose', country='USA', capacity=20, vc=True)
c2 = co.add_resource(name='Home Alone',       floor=1, bldg=250, city='San Jose', country='USA', capacity=4)
c3 = co.add_resource(name='Bambi',            floor=1, bldg=250, city='San Jose', country='USA', capacity=4)
c4 = co.add_resource(name='Deep Impact',      floor=2, bldg=250, city='San Jose', country='USA', capacity=16)
c5 = co.add_resource(name='Midnight Express', floor=2, bldg=250, city='San Jose', country='USA', capacity=12)
c6 = co.add_resource(name='Everest',          floor=3, bldg=300, city='San Jose', country='USA', capacity=40, vc=True)
co.show_resources()
print()
now = datetime.now()
fm  = datetime(now.year, now.month, now.day, now.hour+1)
duration = timedelta(minutes=60)
to  = fm + duration

rl = Reservation_log()

rl.make_reservation(c1, fm, to, 'dhakumar@hotmail.com')
rl.make_reservation(c2, fm, to, 'dhakumar@hotmail.com')
rl.make_reservation(c3, fm, to, 'dhakumar@hotmail.com')
rl.make_reservation(c4, fm, to, 'dhakumar@hotmail.com')
rl.make_reservation(c5, fm, to, 'dhakumar@hotmail.com')
rl.make_reservation(c6, fm, to, 'dhakumar@hotmail.com')
print()
#case 1: when requested time start before booked time and ends after the start of booked time but less then booked to time
fm = fm-timedelta(minutes=30)
to  = fm + duration
rl.make_reservation(c1, fm, to, 'dkumar@gmail.com')
#case 2: when requested time start and to time is within booked time 
fm = fm + timedelta(minutes=15)
to = fm + timedelta(minutes=30)
rl.make_reservation(c2, fm, to, 'dkumar@gmail.com')
#case 3: when requested start and end time is more than booked time 
fm = fm-timedelta(minutes=30)
to  = fm + timedelta(hours=2)
rl.make_reservation(c3, fm, to, 'dkumar@gmail.com')
# case 4: when requested time starts after booked start but before booked end time
fm = fm +timedelta(minutes=30)
to  = fm + timedelta(hours=1)
rl.make_reservation(c4, fm, to, 'dkumar@gmail.com')
# These should be allowed
print()
fm  = datetime(now.year, now.month, now.day, now.hour+1) + duration
to  = fm + duration
rl.make_reservation(c1, fm, to, 'dkumar@gmail.com')
rl.make_reservation(c2, fm, to, 'dkumar@gmail.com')

fm  = datetime(now.year, now.month, now.day, now.hour+1)- duration
to  = fm + duration
rl.make_reservation(c3, fm, to, 'dkumar@gmail.com')
rl.make_reservation(c4, fm, to, 'dkumar@gmail.com')

print()
fm  = datetime(now.year, now.month, now.day, now.hour+1)
duration = timedelta(minutes=60)
to  = fm + duration
rl.cancel_reservation(c1, fm, to, 'dhakumar@hotmail.com')
class ParkingSpot (object):
    def __init__(self, number, stype, size, location, valet=False):
        self.stype    = stype # e.g. [H]andicapped, [C]ompact, [R]egular
        self.size     = size  # e.g. [S]mall, [M]edium, [L]arge
        self.vehicle  = None # e.g.[Bus], [Car], Two-Wheeler [TW]
        self.number   = number
        self.valet    = valet   # True, False
        self.location = location # e.g. [F]ront, [B]ack, or [A]ny

    def park (self, vehicle):
        self.vehicle = vehicle

    def unpark (self):
        vehicle = self.vehicle
        self.vehicle = None
        return vehicle

    def can_park(self, vehicle='Car', stype='R', valet=False):
        if valet != self.valet: # cannot park in a valet spot if not valet or vice versa
            return False

        if self.vehicle != None: # spot is already filled
            return False

        if self.stype == 'H' and stype != 'H': # Regular or Compact vehicle cannot part in a handicapped spot
            return False

        if self.stype == 'C' and stype == 'R': # cannot park a regular vehicle in a compact spot
            return False

        # check if the vehicle can fit in the spot
        if (vehicle == 'Car' and self.size == 'S') or (vehicle == 'Bus' and self.size != 'L'):
            return False

        return True

class ParkingLot(object):
    def __init__(self):
        self.lot = []
        self.max_spot = 0

    def add_spot (self, stype, size, location, valet=False):
        self.max_spot += 1
        spot = ParkingSpot(self.max_spot, stype, size, location, valet)
        self.lot.append(spot)

    def available_spots(self):
        nspot = {}
        nspot['S'] = []
        nspot['M'] = []
        nspot['L'] = []
        for spot in self.lot:
            if spot.vehicle == None:
                nspot[spot.size].append(spot.number)
        return nspot

    def park(self, vehicle, stype, location, valet=False): # assuming vehicle can be parked in Any location
        parked = False
        area={}
        area['F'] = 'Front'
        area['B'] = 'Back'
        for spot in self.lot:
            if spot.can_park(vehicle, stype, valet):
                if location == spot.location:
                    spot.park(vehicle)
                    print(vehicle, " parked in spot", spot.number, 'in ', area[spot.location])
                    parked = True
                    break
        if not parked: # try any location if cannot park in preferred location
            for spot in self.lot:
                if spot.can_park(vehicle, stype, valet):
                    spot.park(vehicle)
                    print(vehicle, " parked in spot", spot.number, 'in ', area[spot.location])
                    parked = True
                    break

        if not parked:
            print('\nSorry, no space available for', vehicle,'\n')

        return parked

    def unpark(self, number):
        vehicle = None
        for spot in self.lot:
            if spot.number == number:
                vehicle = spot.unpark()
                break
        return vehicle

    def status(self):
        nspot = self.available_spots()
        total_spots = len(nspot['S']) + len(nspot['M']) + len(nspot['L'])
        if total_spots == 0:
            print("\nParking lot is full!\n")
        else:
            print("\nAvailable Spots:\n Small: {}\n Medium: {}\n Large: {}\n".format(nspot['S'], nspot['M'], nspot['L']))

# driver for parking lot class dry run
parking_lot = ParkingLot()
# add 5 large spaces and 5 handicapped spaces in Front
big = 5
for i in range(big):
    parking_lot.add_spot(stype='R', size='L', location='F', valet=False)
    parking_lot.add_spot(stype='H', size='L', location='F', valet=False)

# add 20 small spaces (10 in front and 10 in back) for two wheelers and compact cars
sml = 20
for i in range(sml):
    if i < sml//2:
        parking_lot.add_spot(stype='C', size='S', location='F', valet=False)
    else:
        parking_lot.add_spot(stype='C', size='S', location='B', valet=False)

# add 40 spaces 20 in front 20 in back for Regular Mid size cars
mid = 40
for i in range(mid):
    if i < mid//2:
        parking_lot.add_spot(stype='R', size='M', location='F', valet=False)
    else:
        parking_lot.add_spot(stype='R', size='M', location='B', valet=False)

parking_lot.status()
# park six buses 
for i in range(big+1):
    parking_lot.park(vehicle='Bus', stype='R', location='F', valet=False)

for i in range(mid+1):
    parking_lot.park(vehicle='Car', stype='R', location='F', valet=False)

for i in range(sml+1):
    parking_lot.park(vehicle='TW', stype='C', location='F', valet=False)

parking_lot.status()

for number in range(9,70,10):
    vehicle = parking_lot.unpark(number)
    print('Spot {} is now available with a {} moving out'.format(number, vehicle))
    parking_lot.status()

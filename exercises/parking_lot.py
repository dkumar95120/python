from collections import defaultdict
class Vehicle:
    def __init__(self, id, type, stype):
        self.id = id  # license plate
        self.type = type # [Bus], [Car], Two-Wheeler [TW]
        self.stype = stype # [H]andicapped, [C]ompact, [R]egular

class ParkingSpot:
    def __init__(self, number, stype, size, location, valet=False):
        self.stype    = stype # e.g. [H]andicapped, [C]ompact, [R]egular
        self.size     = size  # e.g. [S]mall, [M]edium, [L]arge
        self.vehicle  = None 
        self.number   = number
        self.valet    = valet   # True, False
        self.location = location # e.g. [F]ront, [B]ack, or [A]ny

    def park (self, vehicle):
        self.vehicle = vehicle

    def unpark (self):
        vehicle = self.vehicle
        self.vehicle = None
        return vehicle

    def can_park(self, vehicle, valet=False):
        if valet != self.valet: # cannot park in a valet spot if not valet or vice versa
            return False

        if self.stype == 'H' and vehicle.stype != 'H': # Regular or Compact vehicle cannot part in a handicapped spot
            return False

        if self.stype == 'C' and vehicle.stype != 'C': # cannot park a regular vehicle in a compact spot
            return False

        # check if the vehicle can fit in the spot
        if (vehicle.type == 'Car' and self.size == 'S') or (vehicle.type == 'Bus' and self.size != 'L'):
            return False

        return True

class ParkingLot(object):
    def __init__(self):
        self.lot = defaultdict(list)
        self.max_spot = 0

    def add_spot (self, stype, size, location, valet=False):
        self.max_spot += 1
        spot = ParkingSpot(self.max_spot, stype, size, location, valet)
        self.lot[None].append(spot)

    def available_spots(self):
        nspot = {}
        nspot['S'] = []
        nspot['M'] = []
        nspot['L'] = []
        for spot in self.lot[None]:
            nspot[spot.size].append(spot.number)
        return nspot

    def park(self, vehicle, location, valet=False): # assuming vehicle can be parked in Any location
        parked = False
        area={}
        area['F'] = 'Front'
        area['B'] = 'Back'
        for spot in self.lot[None]:
            if spot.can_park(vehicle, valet):
                if location == spot.location:
                    spot.park(vehicle)
                    print(vehicle.id, " parked in spot", spot.number, 'in ', area[spot.location])
                    parked = True
                    break
        if not parked: # try any location if cannot park in preferred location
            for spot in self.lot[None]:
                if spot.can_park(vehicle, valet):
                    spot.park(vehicle)
                    print(vehicle.id, " parked in spot", spot.number, 'in ', area[spot.location])
                    parked = True
                    break

        if not parked:
            print('\nSorry, no space available for', vehicle.id,'\n')
        else:
            self.lot[vehicle.id] = self.lot[None].pop(self.lot[None].index(spot))

        return parked

    def unpark(self, vehicle_id):
        spot = None
        if vehicle_id in self.lot:
            spot = self.lot[vehicle_id]
            spot.unpark()
            # add this spot to available spots
            self.lot[None].append(spot)
            # delete reference to this vehicle in this parking lot
            del self.lot[vehicle_id]
        else:
            print(f"{vehicle_id} is not parked in this parking lot")

        return spot

    def status(self):
        nspot = self.available_spots()
        total_spots = len(nspot['S']) + len(nspot['M']) + len(nspot['L'])
        if total_spots == 0:
            print("\nParking lot is full!\n")
        else:
            print("\nAvailable Spots:\n Small: {}\n Medium: {}\n Large: {}\n".format(nspot['S'], nspot['M'], nspot['L']))

# driver for parking lot class dry run
parking_lot = ParkingLot()
# add large spaces for buses and for handicapped vehicles in Front
big = 5
for i in range(big):
    parking_lot.add_spot(stype='R', size='L', location='F', valet=False)
    parking_lot.add_spot(stype='H', size='L', location='F', valet=False)

# add spaces for two wheelers and compact cars (half in front and the other half in back)
sml = 20
for i in range(sml):
    if i < sml//2:
        parking_lot.add_spot(stype='C', size='S', location='F', valet=False)
    else:
        parking_lot.add_spot(stype='C', size='S', location='B', valet=False)

# add spaces for Regular Mid size cars half in front and the other half in back 
mid = 30
for i in range(mid):
    if i < mid//2:
        parking_lot.add_spot(stype='R', size='M', location='F', valet=False)
    else:
        parking_lot.add_spot(stype='R', size='M', location='B', valet=False)

parking_lot.status()
# park six buses 
for i in range(big+1):
    vehicle = Vehicle(f'4WRK45{i}', 'Bus', 'R')
    parking_lot.park(vehicle, location='F', valet=False)

for i in range(mid+1):
    if i < 5:
        stype = 'H'
    elif i < 20:
        stype = 'C'
    else:
        stype = 'R'
    vehicle = Vehicle(f'5XHT8{i:02}', 'Car', stype)
    parking_lot.park(vehicle, location='F', valet=False)

for i in range(sml+1):
    vehicle = Vehicle(f'7SFM9{i:02}', 'TW', 'C')
    parking_lot.park(vehicle, location='F', valet=False)

parking_lot.status()

for vehicle_id in ['4WRK450','4WRK451', '5XHT800', '5XHT801', '7SFM905' '7SFM917']:
    spot = parking_lot.unpark(vehicle_id)
    if spot:
        print(f'Spot {spot.number} is now available with a {vehicle_id} moving out')
    parking_lot.status()

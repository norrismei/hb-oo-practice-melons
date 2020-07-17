############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

        self.pairings = []

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    muskmelon = MelonType('musk', '1998', 'green', True, True, 'muskmelon')
    all_melon_types.append(muskmelon)
    muskmelon.add_pairing('mint')

    casaba = MelonType('cas', '2003', 'orange', False, False, 'casaba')
    all_melon_types.append(casaba)
    casaba.add_pairing('strawberries')
    casaba.add_pairing('mint')

    crenshaw = MelonType('cren', '1996', 'green', False, False, 'crenshaw')
    all_melon_types.append(crenshaw)
    crenshaw.add_pairing('proscuitto')

    yellow_watermelon = MelonType('yw', '2013', 'yellow', False, True, \
                                'yellow watermelon')
    all_melon_types.append(yellow_watermelon)
    yellow_watermelon.add_pairing('ice cream')


    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon_type in melon_types:
        print(f"{melon_type.name.capitalize()} pairs well with:")
        
        for pairing in melon_type.pairings:
            print(f"- {pairing}")

        print()


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_type_lookup = {}

    for melon_type in melon_types:
        melon_type_lookup[melon_type.code] = melon_type

    return melon_type_lookup

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape_rating, color_rating, \
                    from_field, harvested_by):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.from_field = from_field
        self.harvested_by = harvested_by


    def is_sellable(self):
        """Returns True if melon is sellable; False otherwise"""
        if self.shape_rating > 5 and \
            self.color_rating > 5 and \
            self.from_field != 3:
            return True
        else:
            return False


    # Needs __init__ and is_sellable methods

def make_melons(melon_types, melon_data=[]):
    """Takes in list of MelonType objects, eturns a list of Melon objects."""

    melon_type_by_code = make_melon_type_lookup(melon_types)

    melons = []

    melon_1 = Melon(melon_type_by_code['yw'], 8, 7, 2, 'Sheila')
    melons.append(melon_1)

    melon_2 = Melon(melon_type_by_code['yw'], 3, 4, 2, 'Sheila')
    melons.append(melon_2)

    melon_3 = Melon(melon_type_by_code['yw'], 9, 8, 3, 'Sheila')
    melons.append(melon_3)

    melon_4 = Melon(melon_type_by_code['cas'], 10, 6, 35, 'Sheila')
    melons.append(melon_4)

    melon_5 = Melon(melon_type_by_code['cren'], 8, 9, 35, 'Michael')
    melons.append(melon_5)

    melon_6 = Melon(melon_type_by_code['cren'], 8, 2, 35, 'Michael')
    melons.append(melon_6)

    melon_7 = Melon(melon_type_by_code['cren'], 2, 3, 4, 'Michael')
    melons.append(melon_7)

    melon_8 = Melon(melon_type_by_code['musk'], 6, 7, 4, 'Michael')
    melons.append(melon_8)

    melon_9 = Melon(melon_type_by_code['yw'], 7, 10, 3, 'Sheila')
    melons.append(melon_9)

    for melon in melon_data:
        code = melon[5]
        shape_rating = int(melon[1])
        color_rating = int(melon[3])
        from_field = int(melon[11])
        harvested_by = melon[8]
        melon_object = Melon(melon_type_by_code[code], shape_rating, color_rating, \
                    from_field, harvested_by)
        melons.append(melon_object)

    return melons


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        if melon.is_sellable():
            is_sellable_msg = '(CAN BE SOLD)'
        else:
            is_sellable_msg = '(NOT SELLABLE)'
        print("Harvested by " + melon.harvested_by + " from Field " + \
            str(melon.from_field) + " " + is_sellable_msg)


def open_and_close_file(filepath):
    """Opens file and returns list of harvests"""

    file = open('harvest_log.txt')

    harvests = []

    for line in file:
        line = line.rstrip()
        tokens = line.split()
        harvests.append(tokens)

    return harvests


# Functions to test script
file = 'harvest_log.txt'
melon_types = make_melon_types()
melons = make_melons(melon_types, open_and_close_file(file))
get_sellability_report(melons)


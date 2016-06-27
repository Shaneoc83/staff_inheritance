class Bird(object):
    def __init__(self, kind, call):
        self.kind = kind
        self.call = call

    def get_description(self):
        return "A %s goes %s." % (self.kind, self.call)


class Seabird(Bird):
    def __init__(self, kind, call, diving_depth):
        super(Seabird, self).__init__(kind, call)
        self.diving_depth = diving_depth

    def get_description(self):
        return super(Seabird, self).get_description() + '\nand dives to a depth of %s metres.' % self.diving_depth


class Fowl(Bird):
    def __init__(self, kind, call, fowl_type):
        self.fowl_types = {'landfowl': 'Landfowl is an order of heavy-bodied ground-feeding birds',
                           'waterfowl': 'Waterfowl is an order of birds that comprises three families: \nAnhimidae (the screamers)\n'
                                        'Anseranatidae (the magpie goose), \nAnatidae'}
        self.fowl_type = fowl_type
        super(Fowl, self).__init__(kind, call)

    def get_description(self):
        return super(Fowl, self).get_description() + "\nSome interesting facts about the %s : A %s is of type %s. %s " \
                                                     % (self.kind, self.kind, self.fowl_type,
                                                        self.fowl_types[self.fowl_type.lower()])

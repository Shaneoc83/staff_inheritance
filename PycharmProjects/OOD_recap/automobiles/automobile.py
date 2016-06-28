class Auto:
    def __init__(self, auto_type, engine_type, capacity, composition, is_soft_top=False, is_articulated=False):

        self.auto_type = auto_type.lower()
        self.engine_type = engine_type.lower()
        self.capacity = capacity
        self.composition = composition.lower()
        self.is_soft_top = is_soft_top
        self.is_articulated = is_articulated
        self.operation_type = "manual"

        #  add the engine
        self.my_engine = Engine(engine_type, capacity)

        # add the body
        self.my_body = Body(self.composition, self.is_soft_top, self.is_articulated)

        # add the wheels and doors
        self.my_wheels = []
        self.my_doors = []

        if self.auto_type == "car":
            for wheel in range(4):
                self.my_wheels.append(Wheel(17, "Radial"))
            if self.composition == "carbon fibre":
                self.operation_type = "automatic"
            for door in range(4):
                self.my_doors.append(Door(self.operation_type))

        elif self.auto_type == "bike":
            for wheel in range(2):
                self.my_wheels.append(Wheel(18, "Slick"))

        elif self.auto_type == "truck":
            if self.is_articulated:
                for wheel in range(18):
                    self.my_wheels.append(Wheel(26, "Asymmetric"))
            else:
                for wheel in range(10):
                    self.my_wheels.append(Wheel(26, "Asymmetric"))

            for door in range(2):
                self.my_doors.append(Door(self.operation_type))

    def drive(self):
        if len(self.my_doors) > 0:
            print self.my_doors[0].open()
            print self.my_doors[0].close()

        print self.my_engine.start()

        for wheel in self.my_wheels:
            print wheel.rotate()

        if self.is_soft_top:
            print self.my_body.open_roof()

        print "Driving!"

        print "----------------------------"

    def stop(self):
        for wheel in self.my_wheels:
            print wheel.stop()

        print "Stopping!!"
        print self.my_engine.stop()

        if self.is_soft_top:
            print self.my_body.close_roof()

        if len(self.my_doors) > 0:
            print self.my_doors[0].open()
            print self.my_doors[0].close()

        print "----------------------------"

    def description(self):
        print "Description:"
        print self.auto_type
        print self.engine_type
        print self.capacity
        print self.composition
        print self.is_soft_top
        print self.is_articulated
        print self.operation_type
        print "----------------------------"


class Engine:
    def __init__(self, engine_type, capacity=0):
        self.engine_type = engine_type
        self.capacity = capacity

    def start(self):
        return "Engine started"

    def stop(self):
        return "Engine Stopped"


class Wheel:
    def __init__(self, size, tyre_type):
        self.size = size
        self.tyre_type = tyre_type

    def rotate(self):
        return "Turning!"

    def stop(self):
        return "Braking!"


class Door:
    def __init__(self, operation_type):
        self.operation_type = operation_type.lower()

    def open(self):
        if self.operation_type == 'automatic':
            return "Click Swish!"
        else:
            return "Click!"

    def close(self):
        if self.operation_type == 'automatic':
            return "Swish Clunk"
        else:
            return "Creak Clunk!!"


class Body:
    def __init__(self, composition, is_soft_top=False, is_articulated=False):
        self.composition = composition
        self.is_soft_top = is_soft_top
        self.is_articulated = is_articulated

    def open_roof(self):
        return "whirr... fold...clunk"

    def close_roof(self):
        return "unfold..whirr...clunk"

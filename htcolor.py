from ev3dev2.sensor import Sensor

class HTColor:
    # red value 0-1
    r=0

    # green value 0-1
    g=0

    # blue value 0-1
    b=0

    # white value 0-1
    w=0

    def __init__(self, port_number=1):
        self.sensor = Sensor(name_pattern="sensor" + str(port_number-1), name_exact=True)
        self.sensor.mode = "RGB"

        pass

    def read(self):
        self.r = self.sensor.value(0) / 255.0
        self.g = self.sensor.value(1) / 255.0
        self.b = self.sensor.value(2) / 255.0
        self.w = self.sensor.value(3) / 255.0


        # convert colors to HSB
        r,g,b = self.r, self.g, self.b
        mx = max(r, g, b)
        mn = min(r, g, b)
        df = mx-mn
        if mx == mn:
            h = 0
        elif mx == r:
            h = (60 * ((g-b)/df) + 360) % 360
        elif mx == g:
            h = (60 * ((b-r)/df) + 120) % 360
        elif mx == b:
            h = (60 * ((r-g)/df) + 240) % 360
        if mx == 0:
            s = 0
        else:
            s = (df/mx)*100
        v = mx*100

        self.hue = h
        self.saturation = s
        self.brightness = v

    def sees_red(self, auto_read=True):
        if auto_read: self.read()
        return self.saturation > 50 and (self.hue < 30 or self.hue > 330)

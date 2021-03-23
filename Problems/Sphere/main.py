class Sphere:
    # finish class Sphere here
    P = 3.1415

    def __init__(self, radius):
        self.radius = radius
        self.volume = 4 / 3 * (Sphere.P * radius ** 3)



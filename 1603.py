class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.spaces = [0, big, medium, small]

    def addCar(self, carType: int) -> bool:
        self.spaces[carType] -= 1
        return self.spaces[carType] >= 0


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)

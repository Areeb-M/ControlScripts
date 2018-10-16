import MotorController


class Controller:
    def __init__(self):
        MotorController.set_velocity(0)
        MotorController.set_turn(0)
        MotorController.update_car()

    def update(self, data):
        raise NotImplementedError()

    def HALT(self):
        raise NotImplementedError()

    def update_car(self):
        MotorController.update_car()

    def set_velocity(self, v):
        MotorController.set_velocity(v)

    def set_turn(self, t):
        MotorController.set_turn(t)

    #def

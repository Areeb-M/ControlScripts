import MotorController


class Controller:
    def __init__(self):
        MotorController.set_velocity(0)
        MotorController.set_turn(0)
        MotorController.update_car()

    def update(self):
        raise NotImplementedError()

    def HALT(self):
        raise NotImplementedError()

    def update_car(self):
        MotorController.update_car()

    #def

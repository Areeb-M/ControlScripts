import MotorController


class Controller:
    halt = False

    def __init__(self):
        MotorController.set_velocity(0)
        MotorController.set_turn(0)
        MotorController.update_car()

    def update(self, data):
        raise NotImplementedError()

    def HALT(self):
        self.set_velocity(0)
        self.set_turn(0)
        Controller.halt = True

    def UNHALT(self):
        Controller.halt = False

    def update_car(self):
        if not Controller.halt:
            MotorController.update_car()

    def set_velocity(self, v):
        if not Controller.halt:
            MotorController.set_velocity(v)

    def set_turn(self, t):
        if not Controller.halt:
            MotorController.set_turn(t)

    def get_velocity(self):
        return MotorController.get_velocity()

    def get_turn(self):
        return MotorController.get_turn()

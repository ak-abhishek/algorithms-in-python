#!/usr/bin/python


class Model(object):

    def __init__(self, name, roll_no):
        self.set_name(name)
        self.set_roll_no(roll_no)

    def get_roll_no(self):
        return self.roll_no

    def set_roll_no(self, roll_no):
        self.roll_no = roll_no

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


class View(object):

    def print_student_details(self, student_name, student_rollno):
        print "Student:", student_name, " Roll No:", student_rollno


class Controller(object):

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def set_student_name(self, name):
        self.model.set_name(name)

    def get_student_name(self):
        return self.model.get_name()

    def set_roll_no(self, roll_no):
        self.model.set_roll_no(roll_no)

    def get_roll_no(self):
        return self.model.get_roll_no()

    def update_view(self):
        self.view.print_student_details(self.model.get_name(), self.model.get_roll_no())


if __name__ == '__main__':
    model = Model('Robert', '10')
    view = View()
    ctrl = Controller(model, view)

    ctrl.update_view()

    ctrl.set_student_name('John')

    ctrl.update_view()

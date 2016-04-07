#!/usr/bin/python


class Observer(object):

    def update(self):
        return NotImplementedError


class Subject(Observer):

    def __init__(self):
        self.observers = []
        self.state = 0

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state
        self.notify_all_observers()

    def attach(self, observer):
        self.observers.append(observer)

    def notify_all_observers(self):
        for observer in self.observers:
            observer.update()


class BinaryObserver(Observer):

    def __init__(self, subject):
        self.subject = subject
        self.subject.attach(self)

    def update(self):
        print "Binary String", bin(self.subject.get_state())


class OctalObserver(Observer):

    def __init__(self, subject):
        self.subject = subject
        self.subject.attach(self)

    def update(self):
        print "Octal String", oct(self.subject.get_state())


class HexaObserver(Observer):

    def __init__(self, subject):
        self.subject = subject
        self.subject.attach(self)

    def update(self):
        print "Hexadecimal String", hex(self.subject.get_state())


if __name__ == '__main__':
    subject = Subject()

    BinaryObserver(subject)
    OctalObserver(subject)
    HexaObserver(subject)

    print "First State: 15"
    subject.set_state(15)

    print "Second State: 20"
    subject.set_state(20)

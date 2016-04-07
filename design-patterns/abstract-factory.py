#!/usr/bin/env python


class Shape(object):

    def draw(self):
        raise NotImplementedError


class Rectangle(Shape):

    def draw(self):
        print "Inside Rect.draw()"


class Square(Shape):

    def draw(self):
        print "Inside Sq.draw()"


class Circle(Shape):

    def draw(self):
        print "Inside Circle.draw()"


class Color(object):

    def fill(self):
        raise NotImplementedError


class Red(Color):

    def fill(self):
        print "Inside Red.fill()"


class Green(Color):

    def fill(self):
        print "Inside Green.fill()"


class Blue(Color):

    def fill(self):
        print "Inside Blue.fill()"


class AbstractFactory(object):

    def get_color(self, color):
        raise NotImplementedError

    def get_shape(self, shape):
        raise NotImplementedError


class ShapeFactory(AbstractFactory):

    def get_color(self, color):
        raise NotImplementedError

    def get_shape(self, shape):
        if shape.upper() == 'CIRCLE':
            return Circle()
        elif shape.upper() == 'RECTANGLE':
            return Rectangle()
        elif shape.upper() == 'SQUARE':
            return Square()
        else:
            raise ValueError("Invalid Shape")


class ColorFactory(AbstractFactory):

    def get_color(self, color):
        if color.upper() == 'RED':
            return Red()
        elif color.upper() == 'GREEN':
            return Green()
        elif color.upper() == 'BLUE':
            return Blue()
        else:
            raise ValueError("Invalid Color")


class FactoryProducer(object):

    @classmethod
    def get_factory(cls, factory_type):
        if factory_type.upper() == 'SHAPE':
            return ShapeFactory()
        elif factory_type.upper() == 'COLOR':
            return ColorFactory()
        else:
            raise ValueError("Invalid Factory Type")


if __name__ == '__main__':
    shapefactory = FactoryProducer.get_factory('Shape')

    shape1 = shapefactory.get_shape('Circle')
    shape1.draw()

    shape2 = shapefactory.get_shape('Rectangle')
    shape2.draw()

    shape3 = shapefactory.get_shape('Square')
    shape3.draw()

    colorfactory = FactoryProducer.get_factory('Color')

    color1 = colorfactory.get_color('Red')
    color1.fill()

    color2 = colorfactory.get_color('Green')
    color2.fill()

    color3 = colorfactory.get_color('Blue')
    color3.fill()

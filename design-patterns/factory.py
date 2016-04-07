#!/usr/bin/env python


class Shape(object):

    def draw(self):
        return NotImplementedError


class Rectangle(Shape):

    def draw(self):
        print "Inside Rect.draw()"


class Square(Shape):

    def draw(self):
        print "Inside Sq.draw()"


class Circle(Shape):

    def draw(self):
        print "Inside Circle.draw()"


class ShapeFactory(Shape):

    def get_shape(self, shape):
        if not shape:
            return None

        if shape.upper() == 'CIRCLE':
            return Circle()
        elif shape.upper() == 'RECTANGLE':
            return Rectangle()
        elif shape.upper() == 'SQUARE':
            return Square()
        else:
            raise ValueError("Invalid type")

if __name__ == '__main__':
    shape_factory = ShapeFactory()

    circle = shape_factory.get_shape('Circle')
    circle.draw()

    sqaure = shape_factory.get_shape('Square')
    sqaure.draw()

    rect = shape_factory.get_shape('Rectangle')
    rect.draw()

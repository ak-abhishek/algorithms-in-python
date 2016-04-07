#!/usr/bin/python


class Singleton(object):

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance


if __name__ == '__main__':
    singleton = Singleton()

    print "object 1", singleton

    singleton2 = Singleton()

    print "object 2", singleton2

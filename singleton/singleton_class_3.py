"""
Pattern Name: SingleTon
Pattern Type: Creational
"""
# Solution 3


class SingleTon(object):
    def __init__(self, cls_name):
        self.cls_name = cls_name
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = self.cls_name(*args, **kwargs)
        return self.instance


@SingleTon
class Logger(object):
    def __init__(self):
        self.start = None

    def write(self, message):
        if self.start:
            print(self.start, message)
        else:
            print(message)


logger1 = Logger()
logger1.start = "# >"
print("logger 1 ", logger1)
logger1.write("object of logger 1 is created")

logger2 = Logger()
logger2.start = "$ >"
print("logger 2 ", logger2)
logger2.write("Logger 2 object created")

import time


class Loggable:
    def log(self, msg):
        print(str(time.time()) + ': ' + str(msg))


class LoggableList(list, Loggable):
    def append(self, obj):
        self.log(obj)
        list.append(self, obj)


x = LoggableList()
x.append('Hello')
x.append(213)

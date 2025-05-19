import rpyc
from constRPYC import *
from rpyc.utils.server import ThreadedServer

class DBList(rpyc.Service):
    value = []

    def exposed_append(self, data):
        self.value.append(data)
        return self.value

    def exposed_value(self):
        return self.value

    def exposed_remove(self, data):
        try:
            self.value.remove(data)
            return self.value
        except ValueError:
            return f"Value {data} not found."

    def exposed_update(self, index, data):
        try:
            self.value[index] = data
            return self.value
        except IndexError:
            return f"Index {index} out of range."

    def exposed_get(self, index):
        try:
            return self.value[index]
        except IndexError:
            return f"Index {index} out of range."

    def exposed_clear(self):
        self.value.clear()
        return self.value

    def exposed_length(self):
        return len(self.value)

if __name__ == "__main__":
    server = ThreadedServer(DBList(), port=PORT)
    server.start()
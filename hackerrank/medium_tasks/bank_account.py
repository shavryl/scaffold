import threading


def positive(func):
    def wrapper(conn, amount):
        if amount <= 0:
            raise ValueError('Dont use negative amount!')
        return func(conn, amount)
    return wrapper


class ConnectionState:

    """
    state machine design pattern
    """

    money = 0

    @staticmethod
    def get_balance(conn):
        raise NotImplementedError()

    @staticmethod
    def withdraw(conn, amount):
        raise NotImplementedError()

    @staticmethod
    def deposit(conn, amount):
        raise NotImplementedError()

    @staticmethod
    def open(conn):
        raise NotImplementedError()

    @staticmethod
    def close(conn):
        raise NotImplementedError()


class BankAccount(ConnectionState):

    def __init__(self):
        self.new_state(ClosedAccount)
        self._lock = threading.RLock()

    def new_state(self, newstate):
        self._state = newstate

    def get_balance(self):
        return self._state.get_balance(self)

    def deposit(self, amount):
        return self._state.deposit(self, amount)

    def withdraw(self, amount):
        return self._state.withdraw(self, amount)

    def open(self):
        return self._state.open(self)

    def close(self):
        return self._state.close(self)


class ClosedAccount(ConnectionState):

    @staticmethod
    def get_balance(self):
        raise ValueError('Not open')

    @staticmethod
    def withdraw(self, amount):
        raise ValueError('Not open')

    @staticmethod
    def deposit(self, amount):
        raise ValueError('Not open')

    @staticmethod
    def open(self):
        self.new_state(OpenedAccount)

    @staticmethod
    def close(self):
        raise ValueError('Already closed')


class OpenedAccount(ConnectionState):

    @staticmethod
    def get_balance(self):
        return self.money

    @staticmethod
    @positive
    def withdraw(self, amount):
        if (self.money - amount) >= 0:
            with self._lock:
                self.money -= amount
        else:
            raise ValueError('Not enough money on your account')

    @staticmethod
    @positive
    def deposit(self, amount):
        with self._lock:
            self.money += amount

    @staticmethod
    def open(self):
        raise ValueError('Already opened')

    @staticmethod
    def close(self):
        self.money = 0
        self.new_state(ClosedAccount)

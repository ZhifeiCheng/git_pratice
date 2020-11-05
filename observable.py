class Observable(object):
    def __init__(self):
        self.__observers = []
        self.__is_changed = False
        self.__observable_last_state = None

    def register_observer(self, observer):
        if observer not in self.__observers:
            self.__observers.append(observer)

    def remove_observer(self, observer):
        self.__observers.remove(observer)

    def notify_observers(self, *args, **kwargs):
        for observer in self.__observers:
            observer.notify(self, *args, **kwargs)

    @property
    def observable_last_state(self):
        return self.__observable_last_state

    @observable_last_state.setter
    def observable_last_state(self, *args):
        self.__observable_last_state = args

    def set_changed(self, *args):
        self.__is_changed = True

    def clear_changed(self):
        self.__is_changed = False

    def has_changed(self):
        return self.__is_changed


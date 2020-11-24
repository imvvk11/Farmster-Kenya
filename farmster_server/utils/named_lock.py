from threading import Lock


class NamedLockContainer:
    def __init__(self):
        self.lock_dict = dict()
        self.global_lock = Lock()

    def lock(self, name: str):
        return NamedLock(self, name)


class NamedLock:
    def __init__(self, container: NamedLockContainer, name: str):
        self.name = name
        self.parent = container

    def __enter__(self):
        if self.name not in self.parent.lock_dict:
            with self.parent.global_lock:
                if self.name not in self.parent.lock_dict:
                    self.parent.lock_dict[self.name] = Lock()

        self.parent.lock_dict[self.name].acquire()

    def __exit__(self, type, value, traceback):
        self.parent.lock_dict[self.name].release()

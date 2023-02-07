from abc import ABC, abstractmethod


class BaseClass(ABC):
    __id = 0
    object_list = None
    manager = None

    def __init__(self, *args, **kwargs):
        self.id = self.generate_id()
        self.store(self)
        self.set_manager()
        super().__init__(*args, **kwargs)

    @classmethod
    def generate_id(cls):
        cls.__id += 1
        return cls.__id

    @classmethod
    def store(cls, obj):
        if cls.object_list is None:
            cls.object_list = list()
        cls.object_list.append(obj)

    @classmethod
    def set_manager(cls):
        if cls.manager is None:
            cls.manager = Manager(cls)

    @abstractmethod
    def show_detail(self):
        print(f"{str(self)} id: {self.id}")


class Manager:
    def __init__(self, _class):
        self._class = _class

    def __str__(self):
        return f"Manager: {self._class}"

    def search(self, **kwargs):
        """

        :param kwargs: a=2, b=5, name="sirwan"
        :return: obj(a=2, b=5, name="sirwan")
        """
        results = list()
        for key, value in kwargs.items():
            if key.endswith("__min"):
                key = key[:-5]
                compare_key = "min"
            elif key.endswith("__max"):
                key = key[:-5]
                compare_key = "max"
            else:
                compare_key = "equal"

            results.append(list())
            length_result = len(results) - 1
            for obj in self._class.object_list:
                if hasattr(obj, key):
                    if compare_key == "min":
                        compare = bool(getattr(obj, key) >= value)
                    elif compare_key == "max":
                        compare = bool(getattr(obj, key) <= value)
                    else:
                        compare = bool(getattr(obj, key) == value)

                    if compare:
                        results[length_result].append(obj)

        if results:
            if len(results) == 1:
                return results

            result = results[0]
            for i in range(1, len(results)):
                result = list(set(result).intersection(results[i]))

            return result

        return None

    # def get(self, **kwargs):
    #     results = list()
    #     for key, value in kwargs.items():
    #         if key.endswith("__min"):
    #             key = key[:-5]
    #             compare_key = "min"
    #         elif key.endswith("__max"):
    #             key = key[:-5]
    #             compare_key = "max"
    #         else:
    #             compare_key = "equal"
    #
    #         results.append(list())
    #         length_result = len(results) - 1
    #         for obj in self._class.object_list:
    #             if hasattr(obj, key):
    #                 if compare_key == "min":
    #                     compare = bool(getattr(obj, key) >= value)
    #                 elif compare_key == "max":
    #                     compare = bool(getattr(obj, key) <= value)
    #                 else:
    #                     compare = bool(getattr(obj, key) == value)
    #
    #                 if compare:
    #                     return obj
    #
    #     return None
    #
    # def count(self):
    #     return len(self._class.object_list)

from abc import ABC, abstractmethod
from AbstractObj import AbstractObj


class AbstractObjManager(ABC):
    """
    Object Manager abstract base class

    Each ObjManager will have all Objects from each instance
    """
    manageable_objects = []
    manager_obj: AbstractObj = None

    def __init__(self, obj):
        self.manager_obj = obj(__ObjControllerInstance=True)
        self.manageable_objects = self.manager_obj.objects

    @abstractmethod
    def add_new_object(self, obj):
        """
        Do Configuration or whatever you want with obj and then call __add_new_object(obj) to add the obj
        :param obj: Object of which this class is the manager
        """
        pass

    def __add_new_object(self, obj):
        self.manageable_objects.append(obj)

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.manageable_objects = []

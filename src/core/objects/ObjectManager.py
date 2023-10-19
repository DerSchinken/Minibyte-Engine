class ObjectManager:
    object_list: list = []
    object_id_list: list[str] = []
    last_id: int = 0

    @staticmethod
    def generate_id():
        """
        Generates a Unique object id
        """
        _id = ObjectManager.last_id + 1
        object_id = "object-" + str(_id)
        while object_id in ObjectManager.object_id_list:
            _id += 1
            object_id = "object-" + str(_id)

        ObjectManager.last_id = _id
        return object_id

class ObjectBuilder:
    @staticmethod
    def build_object(object_list: list):
        """
        This method transform list of Content objects into dictionary and removes
        _ from names and remove _timestamp from result
        """
        parsed_objects = [vars(group) for group in object_list]
        return [
            {
                protected_key[1:]: value for protected_key, value in object_.items()
                if protected_key not in ['_timestamp', '_event_id']
            }
            for object_ in parsed_objects
        ]

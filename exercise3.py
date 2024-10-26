class instance_counter_metaclass(type):

    def __init__(cls, name, bases, dct):

        super().__init__(name, bases, dct)

        cls.instance_count = 0  # Count in 0

 

    def __call__(cls, *args, **kwargs):

        instance = super().__call__(*args, **kwargs)

        cls.instance_count += 1  # Increment instance count when an instance is created

        return instance
class VoltageSignal(object):
    __slots__ = ["_name", "_low", "_high", "_res", "_sets", "_volts", "_duration", "_rate", "_noise", "_data"]

    def __init__(self, voltage, duration, rate=1000, noise=0.0):
        self._volts = float(voltage)
        self._duration = float(duration)
        self._rate = float(rate)
        self._noise = float(noise)
        self._sets = {}  # This is used for fuzzy sets
        self._data = self._create_()  # Assuming this is a method that generates some data

    def __setattr__(self, name, value):
        """Define a set within a domain or assign a value to a domain attribute."""
        # It's a domain attribute (listed in __slots__)
        if name in self.__slots__:
            object.__setattr__(self, name, value)
        # Handle fuzzy sets
        else:
            assert str.isidentifier(name), f"{name} must be an identifier."
            # Store fuzzy sets in _sets dictionary
            self._sets[name] = value

    def _create_(self):
        """Example method for creating data."""
        return [self._volts, self._duration, self._rate, self._noise]  # Dummy data generation

# Example usage
signal = VoltageSignal(5.0, 10.0)
signal.noise = 0.2  # Sets noise using __setattr__
signal.some_fuzzy_set = "Low"  # Adds fuzzy set to _sets
print(signal)

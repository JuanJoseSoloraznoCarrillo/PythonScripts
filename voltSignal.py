#! /home/juanjose/py/bin/python

import numpy as np
import matplotlib.pyplot as plt

 

class VoltageSignal(object):
    __slots__ = ['_time_line_',"_name", "_low", "_high", "_res", "_sets", "_volts", "_duration", "_rate", "_noise", "_data"]

    def __init__(self, voltage, duration, rate=1000, noise=0.0):
        self._volts = float(voltage)
        self._duration = float(duration)
        self._rate = float(rate)
        self._noise = float(noise)
        self._sets = {}  # This is used for fuzzy sets
        self._data = self._create_()  # Assuming this is a method that generates some data

    def __getattr__(self, name):
        """Get the value of an attribute. Called after __getattribute__ is called with an AttributeError."""
        if name in self._sets:
            return self._sets[name]
        else:
            raise AttributeError(f"{name} is not a set or attribute")

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

    @property
    def Voltage(self):
        """The Voltage property."""
        return self._volts

    @Voltage.setter
    def Voltage(self, value):
        self._volts = value
        self._data = self._create_()

    @property
    def Duration(self):
        """The duration property."""
        return self._duration

    @Duration.setter
    def Duration(self, value):
        self._duration = value
        self._data = self._create_()
    
    @property
    def Noise(self):
        """The Noise property."""
        return self._noise

    @Noise.setter
    def Noise(self, value):
        self._noise = value
        self._data = self._create_()

    @property
    def Data(self):
        """The _data property."""
        return self._data

    @property
    def Rate(self):
        """The rate property."""
        return self._rate

    @Rate.setter
    def Rate(self, value):
        self._rate = value
        self._data = self._create_()

    def plot(self):
        plt.figure(figsize=(10, 4))
        plt.plot(self._time_line_, self._data, label="%sV DC Signal"%self._volts, color="b")
        plt.title("Simulated %fV DC Voltage Signal"%self._volts)
        plt.xlabel("Time [s]")
        plt.ylabel("Voltage [V]")
        uplim = self._volts+self._volts*0.1
        lowlim = self._volts-self._volts*0.1
        plt.ylim(lowlim,uplim)
        plt.grid(True)
        plt.legend()
        plt.show()
    
    def _create_(self):
        self._time_line_ = np.linspace(0,self._duration,int(self._rate*self._duration),endpoint=False)
        signal = np.full_like(self._time_line_,self._volts)
        noise = self._noise*np.random.normal(size=self._time_line_.shape)
        return signal+noise


if __name__ == '__main__':
    import sys
    def help():
        print('[*] Correct usage:')
        print('[?] python3 voltSignal.py [voltage] [duration] [rate<opt>] [noise<opt>]')
        print('\t>>> python3 voltSignal.py 12.5 10.0 1000 0.01')

    if len(sys.argv) < 1:
        exit(1)
    else:
        try:
            voltage = sys.argv[1]
            noise = sys.argv[2]
            duration = sys.argv[3]
            rate = sys.argv[4]
            print(voltage,noise,duration,rate)
            sig = VoltageSignal(voltage,duration,rate,noise)
            sig.plot()
        except:
            help()

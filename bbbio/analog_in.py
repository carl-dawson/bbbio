"""
This is a bastardization of the work done by the Adafruit_Blinka team.
https://github.com/adafruit/Adafruit_Blinka

>>> pin = AnalogIn("P9_39")
>>> pin.dac_value
>>> 2245
>>> pin.value
>>> 0.986572265625
"""
import os


class AnalogIn:
    """Analog Input Class"""

    # Sysfs paths
    _sysfs_path = "/sys/bus/iio/devices/"
    _device_path = "iio:device{}"

    # Channel paths
    _channel_path = "in_voltage{}_raw"

    _pins = {
        "P9_39": 0,
        "P9_40": 1,
        "P9_37": 2,
        "P9_38": 3,
        "P9_33": 4,
        "P9_36": 5,
        "P9_35": 6
    }

    def __init__(self, adc_id, device=0):
        self._device = device
        self._channel = adc_id if isinstance(adc_id, int) else self._pins[adc_id]

        self.device_path = os.path.join(
            self._sysfs_path, self._device_path.format(self._device)
        )

        if not os.path.isdir(self.device_path):
            raise ValueError(
                f"No AnalogIn device found for the given ID: '{adc_id}'."
            )

        self.path = os.path.join(self._sysfs_path,
                                 self._device_path.format(self._device),
                                 self._channel_path.format(self._channel))

    @property
    def dac_value(self):
        """Read the ADC and return the value as an integer"""
        with open(self.path, "r") as analog_in:
            return int(analog_in.read().strip())

    @property
    def value(self):
        """Read the ADC and return the value as a Voltage"""
        with open(self.path, "r") as analog_in:
            return 1.8 * int(analog_in.read().strip()) / 2**12

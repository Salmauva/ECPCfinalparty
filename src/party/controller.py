# Salma Abd Adin, script for controller

# Import the needed libraries

from nsp2visasim import sim_pyvisa as pyvisa



# open device
rm = pyvisa.ResourceManager("@py")


class ArduinoVISADevice:
    """class for controller corresponds to operation with the arduino"""

    def __init__(self, port):
        """function to open device and port
        Arg:
            port(str) opening available port
        Returns:
            none
        """
        self.device = rm.open_resource(
            port, read_termination="\r\n", write_termination="\n"
        )

    def get_identification(self):
        """gives back identitystring of the device

        Returns:
            str: returning the identification
        """
        return self.device.query("*IDN?")

    def set_output_value(self, value):
        """set out put voltage on channel 0 in ADC
        Args :
            Value (int): gives value in ADC to the output
        Returns:
            int: returning thr set out value
        """
        self.value = int(self.device.query(f"OUT:CH0 {value}"))
        return self.value

    def get_output_value(self):
        """get previously set output voltage in ACD

        Returns:
            int: ACD values of the set output
        """
        return int(self.device.query(f"OUT:CH0?"))

    def get_input_value(self, channel):
        """measure values in ACD on input channel
        Args:
            channel (str): reading ACD value in this channel
        Returns:
            int: returning values in ACD
        """
        self.channel = int(self.device.query(f"MEAS:CH{channel}?"))
        return self.channel

    def get_input_voltage(self, channel):
        """converting input value from ACD to voltage

        Args:
            channel (str): reading ACD value in this channel

        Returns:
            str: the converted ACD value to voltage
        """
        return (3.3 * int(self.device.query(f"MEAS:CH{channel}?"))) / 1023
    
    def close_device(self):
        """function to close the device
        """
        self.device.close()



def list_devices():
    """making lists of visible ports
    Args: none
    Returns:
        list: list of visible ports
    """
    port = rm.list_resources()
    return port
print(list_devices())
#('ASRL::SIMLED::INSTR', 'ASRL::SIMPV::INSTR', 'ASRL::SIMPV_BRIGHT::INSTR')
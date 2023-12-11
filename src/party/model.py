# Salma Abd Adin, script for model

# Import the needed libraries
import numpy as np
# import pyvisa

# open device
# rm = pyvisa.ResourceManager("@py")

# call controller from the other document
from party.controller import ArduinoVISADevice, list_devices


class DiodeExperiment:
    """class for model corresponding to mathematical calculations"""

    def __init__(self, port):
        """open device in init function
        Args:
            port(str): available ports
        Returns:
            str: it returns itself
        """
        self.device = ArduinoVISADevice(port=port)

    def find_identification(self):
        """giving identity of device with the corresponding given port from user

        Returns:
            str: identity of the device
        """
        identify = self.device.get_identification()
        return identify
    
    def close_arduino(self):
        """calling close arduino method from controller
        """      
        self.device.close_device()


    def scan(self, min, max, n):
        """Converting voltage value to ACD. Making lists for current, voltage. Calculating their errors per n measurment.

        Args:
            min (int): star value for voltage in ACD
            max (int): finish value for voltage in ACD
            n (int): number of experiments

        Returns:
            list: returning I,U, errors lists for the plot
        """
        u_list_plot = []
        i_list_plot = []
        u_list_error_plot = []
        i_list_error_plot = []
        p_list_plot = []
        r_list_plot = []
        p_list_error_plot = []
        r_list_error_plot = []
        # converting min,max value to ACD value
        voltage_min_acd = int((1023 * min) / 3.3)
        voltage_max_acd = int((1023 * max) / 3.3)

        # going per one point n-times
        for x in range(voltage_min_acd, voltage_max_acd):
            u_list_per_point = []
            i_list_per_point = []
            p_list_per_point = []
            r_list_per_point = []
            self.device.set_output_value(x)

            # calculate per point the std and mean per n measurments
            for i in range(0, n):
                u_chanel_1 = self.device.get_input_voltage(channel=1)
                u_chanel_2 = self.device.get_input_voltage(channel=2)
                # u_value = u_chanel_1 - u_chanel_2
                u_list_per_point.append(u_chanel_1*3)
                ampere = u_chanel_2 / 4.7
                i_list_per_point.append(ampere)
                if ampere != 0:
                    power = (u_chanel_1 * 3) * ampere
                    p_list_per_point.append(power)
                    resistance = (u_chanel_1 * 3) / ampere
                    r_list_per_point.append(resistance)

            # lists for the plot
            u_list_error_plot.append(np.std(u_list_per_point) / (n**0.5))
            i_list_error_plot.append(np.std(i_list_per_point) / (n**0.5))
            p_list_error_plot.append(np.std(p_list_per_point) / (n**0.5))
            r_list_error_plot.append(np.std(r_list_per_point) / (n**0.5))
            u_list_plot.append(np.mean(u_list_per_point))
            i_list_plot.append(np.mean(i_list_per_point))
            p_list_plot.append(np.mean(p_list_per_point))
            r_list_plot.append(np.mean(r_list_per_point))
            self.device.set_output_value(0)
        return u_list_plot, i_list_plot, u_list_error_plot, i_list_error_plot, p_list_plot, r_list_plot, p_list_error_plot,r_list_error_plot
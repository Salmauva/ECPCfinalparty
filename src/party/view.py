# Salma Abd Adin, script for view

# Import the needed libraries
import matplotlib.pyplot as plt
import csv

# call the controller and ports list
from party.controller import ArduinoVISADevice, list_devices

# call the model and ports list
from party.model import DiodeExperiment, list_devices


"""choose the port and plot the current as function of voltage and save the data with errors in csv document"""

port = "ASRL::SIMPV::INSTR"
diode = DiodeExperiment(port)
voltage, current, voltage_error, current_error = diode.scan(0, 3.3, 2)

# plot the graph plus errors
plt.errorbar(
    voltage,
    current,
    yerr=current_error,
    xerr=voltage_error,
    fmt=".",
    markersize=2.5,
)
plt.xlabel("Voltage [V]")
plt.ylabel("Current [A]")
# plt.xlim(0, 3)
# plt.ylim(0, 0.003)
# plt.savefig("plot.jpg")
plt.show()
# make a csv document, add the errors too
with open("measurments.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["U [V]", "I [A]", "U_error [V]", "I_error [A]"])
    for a, b, c, d in zip(voltage, current, voltage_error, current_error):
        writer.writerow([a, b, c, d])
# adding commando
# if __name__ == "__main__":
#     view()
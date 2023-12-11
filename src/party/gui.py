# Salma Abd Adin

# import needed libaries and files
import numpy as np
import csv
import sys
from PySide6 import QtWidgets
from party.ui_mainwindow import Ui_MainWindow
import pyqtgraph as pg
from party.model import DiodeExperiment, list_devices

# PyQtGraph global options
pg.setConfigOption("background", "w")
pg.setConfigOption("foreground", "k")

class UserInterface(QtWidgets.QMainWindow):
    """class for making graphical user interface as a window including graph from the experiment

    """
    def __init__(self):
        """
        initiats ui main window.Connecting signals with functions.
        """        
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # making x and y-axis labels

        self.show()

        # make signals
        self.ui.plotmenu.addItems(["IU", "PR"])
        self.ui.clear_button.clicked.connect(self.plot)
        self.ui.save_data.clicked.connect(self.save_data)
        self.ui.device_button.addItems(list_devices())
        print(list_devices())

    def plot(self):

        choose_plot = self.ui.plotmenu.currentText()

        if choose_plot == "IU":
            """making plot with errorbars based on the given min,max, number of measurments and which port.
            """ 
            # clearing data whenever 'start' clicked again
            self.ui.plot_widget.clear()

            # taking inserted values
            min = self.ui.add_min_button.value()
            max = self.ui.add_max_button.value()
            n = self.ui.add_numpoints_button.value()
            port = self.ui.device_button.currentText()

            # opening device 
            diode = DiodeExperiment(port)
            # getting lists from method scan from model file
            voltage, current, voltage_error, current_error, p_list_plot, r_list_plot, p_list_error_plot,r_list_error_plot = diode.scan(min, max, n)

            # Make a scatterplot with errorbars
            self.ui.plot_widget.plot(voltage, current, symbol="o", symbolSize=5, pen=None)
            error_bars = pg.ErrorBarItem(
                x=np.array(voltage), y=np.array(current), width=2 * np.array(voltage_error), height=2 * np.array(current_error)
            )
            self.ui.plot_widget.addItem(error_bars)
            self.ui.plot_widget.setLabel("left", "Current (A)")
            self.ui.plot_widget.setLabel("bottom", "Voltage (V)")

            # saving u,i,u-error and i-error in the class 
            self.u = voltage
            self.i = current
            self.u_error = voltage_error
            self.i_error = current_error

            # closing device after scan
            diode.close_arduino()

        if choose_plot == "PR":
            """making plot with errorbars based on the given min,max, number of measurments and which port.
            """ 
            # clearing data whenever 'start' clicked again
            self.ui.plot_widget.clear()

            # taking inserted values
            min = self.ui.add_min_button.value()
            max = self.ui.add_max_button.value()
            n = self.ui.add_numpoints_button.value()
            port = self.ui.device_button.currentText()

            # opening device 
            diode = DiodeExperiment(port)
            # getting lists from method scan from model file
            u_list_plot, i_list_plot, u_list_error_plot, i_list_error_plot, p_list_plot, r_list_plot, p_list_error_plot,r_list_error_plot= diode.scan(min, max, n)

            # Make a scatterplot with errorbars
            self.ui.plot_widget.plot(r_list_plot, p_list_plot, symbol="o", symbolSize=5, pen=None)
            error_bars = pg.ErrorBarItem(
                x=np.array(r_list_plot), y=np.array(p_list_plot), width=2 * np.array(r_list_error_plot), height=2 * np.array(p_list_error_plot)
            )
            self.ui.plot_widget.addItem(error_bars)
            self.ui.plot_widget.setLabel("left", "Power (W)")
            self.ui.plot_widget.setLabel("bottom", "Resistance (ohm)")
            # saving r,p,r-error and p-error in the class 
            self.r = r_list_plot
            self.p = p_list_plot
            self.r_error = r_list_error_plot
            self.p_error = p_list_error_plot

            # closing device after scan
            diode.close_arduino()

    def save_data (self):
        """saving data as csv-file with the insterted name whenever user clickes on 'save' and intering namefile
        """        
        choose_plot = self.ui.plotmenu.currentText()

        if choose_plot == "IU":
            filename, _ = QtWidgets.QFileDialog.getSaveFileName(filter="CSV files (*.csv)")
            with open(f"{filename}", "w", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["U [V]", "I [A]", "U_error [V]", "I_error [A]"])
                for a, b, c, d in zip(self.u, self.i, self.u_error, self.i_error):
                    writer.writerow([a, b, c, d])
        if choose_plot == "PR":
            filename, _ = QtWidgets.QFileDialog.getSaveFileName(filter="CSV files (*.csv)")
            with open(f"{filename}", "w", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["R [Ohm]", "P [W]", "R_error [Ohm]", "P_error [W]"])
                for a, b, c, d in zip(self.r, self.p, self.r_error, self.p_error):
                    writer.writerow([a, b, c, d])

def main():
    """showing the grafical user interface
    """      
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())

# making a command line
if __name__ == "__main__":
    main()
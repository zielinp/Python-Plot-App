__appname__ ="Plot ver02"

import sys
import numpy
import re

from math import *

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg as FigureCanvas,
                                                NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure

import ui_QT_Graph02

#----------------- Main-------------------------
class Main(QMainWindow, ui_QT_Graph02.Ui_MainWindow):


    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(__appname__)

        # Connections signals
        self.drawButton.clicked.connect(self.drawPlot)
        self.cleanButton.clicked.connect(self.clearPlot)

        # Pusty wykres i toolbar kiedy uruchomimy aplikacje
        self.fig = Figure()
        self.insidePlot = self.fig.add_subplot(111)
        self.insidePlot.grid(True)
        self.canvas = FigureCanvas(self.fig)
        self.verticalLayout.addWidget(self.canvas)
        self.canvas.draw()
        self.toolbar = NavigationToolbar(self.canvas, self.widget, coordinates=True)
        self.verticalLayout.addWidget(self.toolbar)

        # Komunikat początkowy dla użytkownika
        self.userCommunication.setText("Hello! Please enter your function, range and step.")
        self.userCommunication.setAlignment(Qt.AlignHCenter)


    def displayError(self, errorText):
        """Funkcja służąca do wyświetlania błędów w oknie komunikacji z użytkownikiem"""
        self.userCommunication.setText(errorText)
        self.userCommunication.setStyleSheet("color:red")
        self.userCommunication.setAlignment(Qt.AlignHCenter)

    def isDataValid(self):
        """Funkcja sprawdzająca poprawność wpisanych przez użytkownika danych i wyliczająca
            dziedzinę oraz zbiór wartości funkcji"""
        result = False

        # Sprawdzanie poprawności wpisanej funkcji
        try:
            if self.functionRange.text() == '' or self.functionPattern.text() == '':  # Sprawdzanie czy pola nie są puste
                raise Exception("Sorry, you have empty fields!")

            x = 8
            wzorFunkcji = self.functionPattern.text()
            eval(wzorFunkcji)
        except NameError as ne:
            #QMessageBox.critical(self, __appname__, "Error is:\r\n" + str(ne))
            errorText = "Remember to use 'x' as a function variable!"
            self.displayError(errorText)
            return

        except SyntaxError as se:
            # QMessageBox.critical(self, __appname__, "Error is:\r\n" + str(se))
            errorText = "Remember to use Python syntax while writing function pattern!"
            self.displayError(errorText)
            return

        except Exception as e:
            # QMessageBox.critical(self, __appname__, "Error is:\r\n" + str(e))
            self.displayError(str(e))
            return

        # Sprawdzanie poprawności wpisanej dziedziny
        try:
            dziedzina = self.functionRange.text()

            if re.findall(';', dziedzina).count(';') != 2:  # Czy użyto dwóch średników
                raise ValueError("Please use two semicolons while specifing range!")

            start, stop, step = dziedzina.split(';')
            a = float(start)
            b = float(stop)
            c = float(step)

            if a >= b:
                raise ValueError("Stop value must me bigger than start!")

            if c <= 0:
                raise ValueError("Step must be bigger than 0!")

        except TypeError as e1:
            # QMessageBox.critical(self, __appname__, "Error is:\r\n" + str(e1))
            self.displayError(str(e1))

        except ValueError as e2:
            # QMessageBox.critical(self, __appname__, "Error is:\r\n" + str(e2))
            self.displayError(str(e2))


        else:
            # Wyliczenie dziedziny i zbioru wartości funkcji
            self.X = numpy.arange(a, b + c, c)
            self.Y = []
            for x in self.X:
                self.Y.append(eval(wzorFunkcji))
            result = True
        return result

    def drawPlot(self):
        """Funkcja służąca do rysowania wpisanej funkcji"""
        self.insidePlot.cla()
        self.insidePlot.grid(True)
        if self.isDataValid() == True:
            self.userCommunication.setText("Success!")
            self.userCommunication.setStyleSheet("color:green")
            self.userCommunication.setAlignment(Qt.AlignHCenter)
            self.insidePlot.plot(self.X,self.Y)
            self.insidePlot.set(xlabel='x', ylabel ='F(x)')
            self.insidePlot.set_title("F(x)=" + self.functionPattern.text())
            self.fig.tight_layout()
            self.canvas.draw()

    def clearPlot(self):
        """Funkcja służąca do czyszczenia pola wykresu"""
        self.insidePlot.cla()
        self.insidePlot.grid(True)
        self.canvas.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv) #tworzenie aplikacji
    form = Main() #stworz i pokaz form
    form.show()
    sys.exit(app.exec_()) #uruchom petle glowna
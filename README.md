# GUI
Techniques used : XML parsing, GUI development.

This is a part of a software which is used to test various computer peripherals.(Still in development stage)
The raw data is generally available in the form of Excel sheets which is then converted to XML.
This project is a GUI which has an option of choosing the board number and the peripherals on the particular board which makes the testers job easy.
The data in the GUI is processed from the generated XML file.
The XML is parsed using ElementTree module of Python 3.x  which implements simple and efficient API for parsing XML data.
The GUI is made using tkinter module of Python 3.x which is the standard Python interface to the Tk GUI toolkit.
The tkinter widgets like RadioButton, CheckButton, Menu etc are used.
The next stage is executing command line programs within Python so that required log files are generated and test is completed.


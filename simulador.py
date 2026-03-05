import sys
from PyQt6.QtWidgets import QApplication
from interfaz_cabina import CabinaPerforador

def main():

    app = QApplication(sys.argv)

    ventana = CabinaPerforador()
    ventana.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()

import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import Cargar
import limpiar

class Ui_FP(object):
    def setupUi(self, FP):
        FP.setObjectName("FP")
        FP.resize(804, 569)
        FP.setFixedSize(804, 569)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        FP.setFont(font)
        self.centralwidget = QtWidgets.QWidget(FP)
        self.centralwidget.setObjectName("centralwidget")

        # Estilo general para los botones
        button_style = """
        QPushButton {
            background-color: #0077b6;
            color: white;
            border-radius: 15px;
            padding: 10px;
        }
        QPushButton:hover {
            background-color: #005f99;
        }
        QPushButton:pressed {
            background-color: #003f66;
        }
        """

        # Botón Cargar Archivo
        self.Cargar_Archivo = QtWidgets.QPushButton(self.centralwidget)
        self.Cargar_Archivo.setGeometry(QtCore.QRect(30, 17, 181, 38))
        font.setBold(True)
        font.setWeight(75)
        self.Cargar_Archivo.setFont(font)
        self.Cargar_Archivo.setStyleSheet(button_style)
        self.Cargar_Archivo.setObjectName("Cargar_Archivo")

        # Botón Visualizar Archivo
        self.Visualizar_Archivo = QtWidgets.QPushButton(self.centralwidget)
        self.Visualizar_Archivo.setGeometry(QtCore.QRect(540, 20, 161, 31))
        self.Visualizar_Archivo.setFont(font)
        self.Visualizar_Archivo.setStyleSheet(button_style)
        self.Visualizar_Archivo.setObjectName("Visualizar_Archivo")

        # Botón de Ayuda
        self.Help = QtWidgets.QPushButton(self.centralwidget)
        self.Help.setGeometry(QtCore.QRect(720, 20, 31, 31))
        font.setFamily("Nirmala UI")
        font.setPointSize(14)
        self.Help.setFont(font)
        self.Help.setStyleSheet(button_style)
        self.Help.setObjectName("Help")

        # Etiqueta del Logo
        directorio_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_logo = os.path.join(directorio_actual, "Logo.png")

        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(65, 70, 109, 95))
        self.Logo.setAutoFillBackground(False)
        self.Logo.setText("")

        pixmap = QtGui.QPixmap(ruta_logo)
        if not pixmap.isNull():
            image = pixmap.toImage()
            image = image.convertToFormat(QtGui.QImage.Format_ARGB32)
            transparency = 255
            for y in range(image.height()):
                for x in range(image.width()):
                    pixel = image.pixel(x, y)
                    alpha = QtGui.qAlpha(pixel)
                    image.setPixel(x, y, QtGui.qRgba(QtGui.qRed(pixel), QtGui.qGreen(pixel), QtGui.qBlue(pixel), min(alpha, transparency)))
            pixmap = QtGui.QPixmap.fromImage(image)
            self.Logo.setPixmap(pixmap)

        self.Logo.setScaledContents(True)
        self.Logo.setObjectName("Logo")

        # Consola
        self.Consola = QtWidgets.QTextEdit(self.centralwidget)
        self.Consola.setGeometry(QtCore.QRect(200, 80, 531, 81))
        self.Consola.setReadOnly(True)
        self.Consola.setObjectName("Consola")

        # Etiquetas
        self.Etiqueta_preparar = QtWidgets.QLabel(self.centralwidget)
        self.Etiqueta_preparar.setGeometry(QtCore.QRect(150, 190, 121, 31))
        self.Etiqueta_preparar.setObjectName("Etiqueta_preparar")

        self.Etiqueta_modelar = QtWidgets.QLabel(self.centralwidget)
        self.Etiqueta_modelar.setGeometry(QtCore.QRect(470, 190, 121, 31))
        self.Etiqueta_modelar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Etiqueta_modelar.setObjectName("Etiqueta_modelar")

        # Botón Limpiar Base de Datos
        self.Limpiar_Base = QtWidgets.QPushButton(self.centralwidget)
        self.Limpiar_Base.setGeometry(QtCore.QRect(80, 230, 251, 71))
        self.Limpiar_Base.setFont(font)
        self.Limpiar_Base.setStyleSheet(button_style)
        self.Limpiar_Base.setObjectName("Limpiar_Base")

        # Botón Entrenar Modelo
        self.entrenar_modelo = QtWidgets.QPushButton(self.centralwidget)
        self.entrenar_modelo.setGeometry(QtCore.QRect(410, 230, 251, 71))
        self.entrenar_modelo.setFont(font)
        self.entrenar_modelo.setStyleSheet(button_style)
        self.entrenar_modelo.setObjectName("entrenar_modelo")

        # Botón Generar Pronósticos
        self.pronosticos = QtWidgets.QPushButton(self.centralwidget)
        self.pronosticos.setGeometry(QtCore.QRect(410, 310, 251, 71))
        self.pronosticos.setFont(font)
        self.pronosticos.setStyleSheet(button_style)
        self.pronosticos.setObjectName("pronosticos")

        # Botón Guardar Archivo
        self.Guardar_Archivo = QtWidgets.QPushButton(self.centralwidget)
        self.Guardar_Archivo.setGeometry(QtCore.QRect(250, 440, 241, 71))
        self.Guardar_Archivo.setFont(font)
        self.Guardar_Archivo.setStyleSheet(button_style)
        self.Guardar_Archivo.setObjectName("Guardar_Archivo")

        # ScrollBar para Consola
        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(730, 80, 20, 81))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.Consola.setVerticalScrollBar(self.verticalScrollBar)

        # Líneas decorativas
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(270, 200, 181, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(50, 200, 91, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(360, 230, 16, 151))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(40, 230, 16, 151))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(120, 400, 521, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(590, 200, 91, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")

        # Caja de Texto para Periodos Estacionales
        self.label_periodos = QtWidgets.QLabel(self.centralwidget)
        self.label_periodos.setGeometry(QtCore.QRect(80, 320, 120, 20))
        self.label_periodos.setText("Periodos:")
        self.label_periodos.setFont(font)
        self.label_periodos.setObjectName("label_periodos")

        self.input_periodos = QtWidgets.QLineEdit(self.centralwidget)
        self.input_periodos.setGeometry(QtCore.QRect(210, 320, 50, 20))
        self.input_periodos.setText("3")
        self.input_periodos.setObjectName("input_periodos")

        # Caja de Texto para Desviaciones Estándar
        self.label_desviaciones = QtWidgets.QLabel(self.centralwidget)
        self.label_desviaciones.setGeometry(QtCore.QRect(80, 350, 120, 20))
        self.label_desviaciones.setText("D. Estándar:")
        self.label_desviaciones.setFont(font)
        self.label_desviaciones.setObjectName("label_desviaciones")

        self.input_desviaciones = QtWidgets.QLineEdit(self.centralwidget)
        self.input_desviaciones.setGeometry(QtCore.QRect(210, 350, 50, 20))
        self.input_desviaciones.setText("2")
        self.input_desviaciones.setObjectName("input_desviaciones")

        # Barra de Progreso
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(200, 170, 531, 16))
        self.progressBar.setValue(0)
        self.progressBar.setVisible(False)
        self.progressBar.setObjectName("progressBar")

        # Añadir centralwidget al FP
        FP.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FP)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 804, 27))
        self.menubar.setObjectName("menubar")
        FP.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FP)
        self.statusbar.setObjectName("statusbar")
        FP.setStatusBar(self.statusbar)

        self.retranslateUi(FP)
        QtCore.QMetaObject.connectSlotsByName(FP)

        # Conectar botones con sus funciones
        self.Cargar_Archivo.clicked.connect(self.cargar_archivo)
        self.Visualizar_Archivo.clicked.connect(self.visualizar_archivo)
        self.Help.clicked.connect(self.mostrar_ayuda)
        self.Limpiar_Base.clicked.connect(self.limpiar_base_datos)
        self.entrenar_modelo.clicked.connect(self.calcular_entrenar_modelo)
        self.pronosticos.clicked.connect(self.calcular_pronosticos)
        self.Guardar_Archivo.clicked.connect(self.guardar_archivos)

        self.dataset_listo = None

    def retranslateUi(self, FP):
        _translate = QtCore.QCoreApplication.translate
        FP.setWindowTitle(_translate("FP", "Reacsa Forecast Assistant"))
        self.Cargar_Archivo.setText(_translate("FP", "Cargar Archivo Excel"))
        self.Visualizar_Archivo.setText(_translate("FP", "Visualizar Archivo"))
        self.Help.setText(_translate("FP", "?"))
        self.Etiqueta_preparar.setText(_translate("FP", "Preparar Datos"))
        self.Etiqueta_modelar.setText(_translate("FP", "Modelar Datos"))
        self.Limpiar_Base.setText(_translate("FP", "Limpiar Base de Datos"))
        self.entrenar_modelo.setText(_translate("FP", "Hiperparámetros: 1"))
        self.pronosticos.setText(_translate("FP", "Hiperparámetros: 2"))
        self.Guardar_Archivo.setText(_translate("FP", "Guardar Archivos"))

    # Funciones para los botones
    
    def cargar_archivo(self):
        ruta = QFileDialog.getOpenFileName(None, None, "Seleccionar archivo", "", "Excel Files (*.xlsx);;CSV Files (*.csv)")

        if ruta[0]: 
            dataset, logs = Cargar.cargar(ruta[0])

            for mensaje in logs:
                self.Consola.append(mensaje)

            if dataset is not None:
                self.dataset_listo = dataset
                self.Consola.append(f"Filas procesadas: {dataset.shape[0]}")

            

    def visualizar_archivo(self):
        if self.dataset_limpio is not None:
            temp_file = "temp_visualizacion.xlsx"
            self.dataset_limpio.to_excel(temp_file, index=False)
            os.startfile(temp_file)
        elif self.dataset_listo is not None:
            # Guardar el DataFrame temporalmente para abrirlo
            temp_file = "temp_visualizacion.xlsx"
            self.dataset_listo.to_excel(temp_file, index=False)
            os.startfile(temp_file)
        else:
            self.Consola.append("❌ No hay datos cargados para visualizar.")

    def mostrar_ayuda(self):
        self.Consola.append("Función de ayuda no implementada")

    def limpiar_base_datos(self):
            if self.dataset_listo is not None:
                try:
                    dataset_limpio, logs = limpiar.limpiar_dataset(self.dataset_listo)
                    for mensaje in logs:
                        self.Consola.append(mensaje)
                    if dataset_limpio is not None:
                        self.dataset_limpio = dataset_limpio
                except ValueError as e:
                    self.Consola.append(f"❌ Hubo un error en el proceso de limpieza: {str(e)}")        
            else:
                self.Consola.append("❌ Primero debes cargar un archivo válido.")

    def entrenar_modelo(self):
        self.Consola.append("Función de hiperparámetros 1 no implementada")

    def pronosticos(self):
        self.Consola.append("Función de hiperparámetros 2 no implementada")

    def guardar_archivos(self):
        self.Consola.append("Función de guardar archivos no implementada")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    FP = QtWidgets.QMainWindow()
    ui = Ui_FP()
    ui.setupUi(FP)
    FP.show()
    sys.exit(app.exec_())

from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel,QGridLayout
from PyQt5.QtWidgets import QLineEdit,QPushButton,QHBoxLayout
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
class Kalkulator(QWidget):
	def __init__(self,parent=None):
		super().__init__(parent)
		self.interfejs()
	def interfejs(self):
		self.resize(300,100)
		self.setWindowTitle("Super Kalkulator")
		self.show()
		etykieta1=QLabel("Liczba 1:",self)
		etykieta2=QLabel("Liczba 2:",self)
		etykieta3=QLabel("Wynik:",self)
		uklad=QGridLayout()
		uklad.addWidget(etykieta1,0,0)
		uklad.addWidget(etykieta2,0,1)
		uklad.addWidget(etykieta3,0,2)
		self.setLayout(uklad)
		self.setGeometry(20,20,300,100)
		#self.setWindowIcon(QIcon('kalkulator.png'))
		self.setWindowTitle("Prosty Kalkulator")
		self.liczba1Edt=QLineEdit()
		self.liczba2Edt=QLineEdit()
		self.wynikEdt=QLineEdit()
		self.wynikEdt.readonly = True
		self.wynikEdt.setToolTip('Wpisz <b>liczby</b> i wybierz dzialanie...')
		uklad.addWidget(self.liczba1Edt,1,0)
		uklad.addWidget(self.liczba2Edt,1,1)
		uklad.addWidget(self.wynikEdt,1,2)
		dodajBtn=QPushButton("&Dodaj",self)
		odejmijBtn=QPushButton("&Odejmij",self)
		dzielBtn=QPushButton("&Mnoz",self)
		mnozBtn=QPushButton("&Dziel",self)
		pierwBtn=QPushButton("&Pierwiastek",self)
		koniecBtn=QPushButton("&Koniec",self)
		koniecBtn.resize(koniecBtn.sizeHint())
		ukladH=QHBoxLayout()
		ukladH.addWidget(dodajBtn)
		ukladH.addWidget(odejmijBtn)
		ukladH.addWidget(dzielBtn)
		ukladH.addWidget(mnozBtn)
		ukladH.addWidget(pierwBtn)
		uklad.addLayout(ukladH,2,0,1,3)
		uklad.addWidget(koniecBtn,3,0,1,3)
		dodajBtn.clicked.connect(self.dzialanie)
		odejmijBtn.clicked.connect(self.dzialanie)
		mnozBtn.clicked.connect(self.dzialanie)
		dzielBtn.clicked.connect(self.dzialanie)
		pierwBtn.clicked.connect(self.dzialanie)
		koniecBtn.clicked.connect(self.koniec)
	def closeEvent(self,event):
		odp=QMessageBox.question(self,'Komunikat',"Czy na pewno koniec?",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		if odp==QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()
	def dzialanie(self):
		nadawca=self.sender()
		try:
			liczba1=float(self.liczba1Edt.text())
			liczba2=float(self.liczba2Edt.text())
			wynik=""
		
			if nadawca.text()=="&Dodaj":
				wynik=liczba1+liczba2
			elif nadawca.text()=="&Odejmij":
				wynik=liczba1-liczba2
			elif nadawca.text()=="&Mnoz":
				wynik=liczba1*liczba2
			elif nadawca.text()=="&Pierwiastek":
				wynik=liczba1**0.5
			else:
				try:
					wynik=round(liczba1/liczba2,9)
				except ZeroDivisionError:
					QMessageBox.critical(self,"Blad","Nie można dzielic przez zero!")
					return
			self.wynikEdt.setText(str(wynik))
		except ValueError:
			QMessageBox.warning(self,"Blad","Bledne dane",QMessageBox.Ok)
	def koniec(self):
		self.close()
	def keyPressEvent(self,e):
		if e.key()==Qt.Key_Escape:
			self.close()
if __name__=='__main__':
	import sys
	app=QApplication(sys.argv)
	okno=Kalkulator()
	sys.exit(app.exec_())



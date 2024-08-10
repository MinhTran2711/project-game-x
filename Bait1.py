import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel, QPushButton, QVBoxLayout, QWidget

class TextDisplayApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        #Chinh thong so cua so
        self.setWindowTitle("Text Display Application")
        self.setGeometry(100, 100, 400, 200) #(x, y, width, height)
        
        #Tao 1 widget trung tam cho cua so chinh
        central_Widget = QWidget()
        self.setCentralWidget(central_Widget)
        
        #Tao widget (QLineEdit, QpushButton, QLabel)
        self.text_edit = QLineEdit()
        self.display_button = QPushButton("Hiển thị")
        self.result_label = QLabel("")
        
        #Tao 1 layout doc
        layout = QVBoxLayout()
        
        #Them Widget vao layout
        layout.addWidget(self.text_edit)
        layout.addWidget(self.display_button)
        layout.addWidget(self.result_label)
        
        #Set layout cho widget doc
        central_Widget.setLayout(layout)
        
        #Ket noi su kien nut bam toi chuc nang display_text
        self.display_button.cliked.connect(self.display_text)
        
    def display_text(self):
        #Lay text tu QLineEdit va hien thi no trong QLabel
        entered_text = self.text_edit.text()
        self.result_label.setText(f"Input Text: {entered_text}")
        
    def main():
        #Tao 1 ung dung PyQt 
        app = QApplication(sys.argv)
        
        #Tao trinh the hien cua TextDisplayApp
        window = TextDisplayApp()
        
        #Show the window
        window.show()
        
        #Chay vong lap su kien cua ung dung
        sys.exit(app.exec_())
        
    if __name__ == "__main__":
        main()
        
        
        
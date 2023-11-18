from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QListWidget, QPushButton, QLineEdit,  QVBoxLayout, QHBoxLayout

app  = QApplication([])
window = QWidget()


text = QTextEdit()
lineText = QLineEdit()
notes_list = QListWidget()
tegs_list = QListWidget()


note_Create_btn = QPushButton("Створити нотатку")
note_Deleate_btn = QPushButton("Видалити нотатку")
note_Save_btn = QPushButton("Зберегти нотатку")
add_Tex_ToNote_btn = QPushButton("додати нотатку до тегу")
an_Pin_btn = QPushButton("відкріпити нотатку")
siorch_Note_btn = QPushButton("пошук по тегех")

main_line = QHBoxLayout()
line1 = QVBoxLayout()
line2 = QVBoxLayout()

line1.addWidget(text)

line2.addWidget(notes_list)
line2.addWidget(note_Create_btn)
line2.addWidget(note_Deleate_btn)
line2.addWidget(note_Save_btn)

line2.addWidget(tegs_list)

line2.addWidget(lineText)

line2.addWidget(add_Tex_ToNote_btn)
line2.addWidget(an_Pin_btn)
line2.addWidget(siorch_Note_btn)










main_line.addLayout(line1)
main_line.addLayout(line2)
window.setLayout(main_line)



window.show()
app.exec_()
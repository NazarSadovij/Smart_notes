from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QListWidget, QPushButton, QLineEdit,  QVBoxLayout, QHBoxLayout, QInputDialog
import json
app  = QApplication([])
window = QWidget()


text = QTextEdit()
lineText = QLineEdit()
notes_list = QListWidget()
tegs_list = QListWidget()


note_Create_btn = QPushButton("Створити нотатку")
note_Deleate_btn = QPushButton("Видалити нотатку")
note_Save_btn = QPushButton("Зберегти нотатку")
add_Tex_ToNote_btn = QPushButton("Додати нотатку до тегу")
an_Pin_btn = QPushButton("Відкріпити нотатку")
siorch_Note_btn = QPushButton("Пошук по тегех")

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

def writeFile():
    with open ("notes.json","w", encoding = "utf-8") as file:
        json.dump(notes, file, ensure_ascii=True, sort_keys=True, indent=4)



def save_note():
    note_text=text.toPlainText()
    note_name = notes_list.currentItem().text()
    notes [note_name]["text"] = note_text
    writeFile()


note_Save_btn.clicked.connect(save_note)

notes  = {}


def show_note():
    note_name = notes_list.currentItem().text()
    text.setText(notes[note_name]["text"])

notes_list.itemClicked.connect(show_note)

def add_note():
    note_name, ok = QInputDialog.getText(window, "Нова замітка", "new_note")
    if ok and note_name != "":
        notes [note_name] = {
            "text": "note_name",
            "tags":[],
        }
        notes_list.addItem(note_name)

with open ("notes.json", "r", encoding="utf-8") as file:
    notes = json.load(file)

notes_list.addItems(notes)

note_Create_btn.clicked.connect(add_note)



window.show()
app.exec_()
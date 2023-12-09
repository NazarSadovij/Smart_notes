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


note_Create_btn.setStyleSheet(""" 
background-color: #fadb11
""")

note_Deleate_btn.setStyleSheet(""" 
background-color: #fadb11
""")

note_Save_btn.setStyleSheet(""" 
background-color: #fadb11
""")

add_Tex_ToNote_btn.setStyleSheet(""" 
background-color: #0eaeed
""")

an_Pin_btn.setStyleSheet(""" 
background-color: #0eaeed
""")

siorch_Note_btn.setStyleSheet(""" 
background-color: #0eaeed
""")

text.setStyleSheet(""" 
background-color: #0bdb1c
""")

notes_list.setStyleSheet(""" 
background-color: #ca0bdb
""")

tegs_list.setStyleSheet(""" 
background-color: #ed160e
""")

lineText.setStyleSheet(""" 
background-color: #ed8c0e
""")




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



def add_tag():
    note_name = notes_list.currentItem().text()
    tag = lineText.text()

    notes[note_name]["tags"].append(tag)
    tegs_list.addItem(tag)
    writeFile()

add_Tex_ToNote_btn.clicked.connect(add_tag)

def del_tag():
    note_name = notes_list.currentItem().text()
    tag_name = tegs_list.currentItem().text()

    notes[note_name]["tags"].remove(tag_name)

    tegs_list.clear()
    tegs_list.addItems(notes[note_name]["tags"])
    writeFile()
an_Pin_btn.clicked.connect(del_tag)

def siorch_by_tag():
    tag = lineText.text()
    if(siorch_Note_btn.text()=="Siorch"):
        filtered = {}                                                        
        for key in notes:
            if tag in notes[key]["tags"]:
                print(notes[key])
                filtered[key] = notes[key]
        siorch_Note_btn.setText("Відмінити пошук")
        notes_list.clear()
        notes_list.addItems(filtered)
        tegs_list.clear()
        lineText.clear()
    else:
        siorch_Note_btn.setText("Siorch")
        notes_list.clear()
        notes_list.addItems(notes)
        tegs_list.clear()
        
siorch_Note_btn.clicked.connect(siorch_by_tag)
            
        
    


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
    tegs_list.clear()
    tegs_list.addItems(notes[note_name]["tags"])

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
import json
import requests

class NotesApp:
    def __init__(self):
        self.url = 'http://localhost:5000'

    def read_all(self):
        res =  requests.get(f'{self.url}/notes')
        return res.json()
    #end def
#end class
app = NotesApp()
choice = int(input('1-all, 2-read_by_id, 3-create, 4-update, 5-delete, 6-search\n choice: '))
if choice==1:
    notes = app.read_all()
    print(notes)

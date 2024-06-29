import os
import firebase_admin
from firebase_admin import credentials, firestore

class Dao:
    def __init__(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, '..', 'dragons_private_key.json')
        
        cred = credentials.Certificate(file_path)
        firebase_admin.initialize_app(cred)
        
        self.db = firestore.client()
    
    def getDados(self, dragon, food):
        doc = self.db.collection('jogo').document('dados').get()

        if doc.exists:
            data = doc.to_dict()

            food.position = data['food']['position']

            dragon.direction = data['dragon']['direction']
            dragon.direction_blocks = data['dragon']['direction_blocks']
            dragon.eatState = data['dragon']['eatState']
            dragon.last_direction = data['dragon']['last_direction']
            dragon.position = data['dragon']['position']
            dragon.body = [[coord['x'], coord['y']] for coord in data['dragon']['body']]
            dragon.color = 'blue'

        else:
            print('Documento não encontrado...')

    def saveDados(self, dragon, food):
        data = {
            'dragon': dragon.to_dict(),
            'food': food.to_dict()
        }

        #print("Dados a serem salvos no Firestore:")
        #print(data)

        self.db.collection('jogo').document('dados').set(data)




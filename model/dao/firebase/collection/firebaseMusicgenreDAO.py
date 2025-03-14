from ....dao.interfaceMusicgenreDAO import InterfaceMusicgenreDAO
from ....dto.musicgenreDTO import MusicgenreDTO
from ..firebaseConnector import FirebaseConnector

class FirebaseMusicgenreDAO(InterfaceMusicgenreDAO):

    def __init__(self):
        self.firebaseConnector = FirebaseConnector()
    
    def get_musicgenres(self):
        musicgenres = []
        try:
            musicgenres_ref = self.firebaseConnector.get_musicgenre_collection()
            query = musicgenres_ref.stream()  # Obtiene todos los documentos

            for doc in query:
                musicgenre_data = doc.to_dict()  # Convierte el documento a un diccionario
                
                # Crear un objeto SongDTO con los datos de la canción
                musicgenre_dto = MusicgenreDTO()
                musicgenre_dto.set_id(musicgenre_data.get("id",""))  # ID del documento en Firestore
                musicgenre_dto.set_description(musicgenre_data.get("description",""))
                # Missing : Obtencion musicgenre JSON
                musicgenres.append(musicgenre_dto)  # Agregar la canción a la lista
        except Exception as e:
            print(e)

        return musicgenres
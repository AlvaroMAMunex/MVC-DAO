# model/dao/firebase/firebaseDAOFactory.py
from ...factory.interfaceDAOFactory import InterfaceDAOFactory
from .collection.firebaseUserDAO import FirebaseUserDAO
from .collection.firebaseSongsDAO import FirebaseSongDAO
from .collection.firebaseMusicgenreDAO import FirebaseMusicgenreDAO

class FirebaseDAOFactory (InterfaceDAOFactory):
    def __init__(self):
        pass
    
    def getUserDao(self):
        return FirebaseUserDAO()
    
    def getSongsDAO(self):
        return FirebaseSongDAO()
    
    def getMusicgenreDAO(self):
        return FirebaseMusicgenreDAO()
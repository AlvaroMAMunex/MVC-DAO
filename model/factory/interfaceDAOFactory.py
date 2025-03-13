from abc import abstractmethod, ABC


class InterfaceDAOFactory(ABC):

    @abstractmethod
    def getUserDao(self):
        pass
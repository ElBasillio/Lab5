from abc import ABC, abstractmethod

class Shape3D(ABC):
    @abstractmethod
    def volume(self) -> float:
        pass

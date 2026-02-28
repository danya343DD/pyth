from abc import ABC, abstractmethod



class Transport(ABC):
    "Абстрактный продукт"
    
    @abstractmethod
    def load_cargo(self):
        pass

    @abstractmethod
    def calculate_cost(self):
        pass

    @abstractmethod
    def track_location(self):
        pass

class Truck(Transport):
    def load_cargo(self):
        return "Груз загружен в грузовик."
    
    def calculate_cost(self):
        return "Стоимость рассчитана для наземной перевозки."
    
    def track_location(self):
        return "Грузовик отслеживается via GPS."
    
    def check_road_condition(self):
        return "Состояние дороги проверено: ОК."

class Ship(Transport):
    def load_cargo(self):
        return "Груз загружен на корабль."
    
    def calculate_cost(self):
        return "Стоимость рассчитана для морской перевозки."
    
    def track_location(self):
        return "Корабль отслеживается via AIS."
    
    def check_weather(self):
        return "Погодные условия проверены: Штормов нет."

class Airplane(Transport):
    def load_cargo(self):
        return "Груз загружен в самолет."
    
    def calculate_cost(self):
        return "Стоимость рассчитана для авиаперевозки."
    
    def track_location(self):
        return "Самолет отслеживается via Radar."
    
    def check_flight_permission(self):
        return "Разрешение на полет получено."



class Logistics(ABC):
    "Абстрактный создатель"
    
    @abstractmethod
    def create_transport(self) -> Transport:
        pass
    
    def plan_delivery(self):
        "Бизнес-логика, использующая фабричный метод"
        transport = self.create_transport()
        
        # Общие операции
        print(transport.load_cargo())
        print(transport.calculate_cost())
        print(transport.track_location())
        
        # Уникальные операции (полиморфизм через isinstance или доп. методы)
        if isinstance(transport, Truck):
            print(transport.check_road_condition())
        elif isinstance(transport, Ship):
            print(transport.check_weather())
        elif isinstance(transport, Airplane):
            print(transport.check_flight_permission())
            
        return transport

class RoadLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Truck()

class SeaLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Ship()

class AirLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Airplane()

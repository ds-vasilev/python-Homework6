from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///project.db')
Base = declarative_base()


class Driver(Base):
    __tablename__ = 'Driver'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(25), nullable=False)
    car = Column(String(25), nullable=False)
    def __repr__(self):
        return f"id: {self.id}, name: {self.name}, car: {self.car}"


class Client(Base):
    __tablename__ = 'Client'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    is_vip = Column(Boolean, nullable=False)
    def __repr__(self):
        return f"id: {self.id}, name: {self.name}, is_vip: {self.is_vip}"


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, autoincrement=True, comment="Идентификатор")
    address_from = Column(String(50), comment="Откуда")
    address_to = Column(String(50), comment="Куда")
    client_id = Column(Integer, ForeignKey('Client.id'), comment="Клиент")
    driver_id = Column(Integer, ForeignKey('Driver.id'), comment="Водитель")
    date_created = Column(String(25), comment="Дата создания")                                  # ЗАГЛУШКА
    status = Column(String(25), comment="Статус")
    clients = relationship("Client", foreign_keys=[client_id])
    drivers = relationship("Driver", foreign_keys=[driver_id])
    def __repr__(self):
        return f"id: {self.id}, address_from: {self.address_from}, address_to: {self.address_to}, " \
               f"client_id: {self.client_id}, driver_id: {self.driver_id}, date_created: {self.date_created}," \
               f" status: {self.status}"

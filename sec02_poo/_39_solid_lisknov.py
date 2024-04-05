"""PRINCIPIO DE SUSTITUCIÓN DE LISKOV

El principio de sustitución de Liskov establece que una clase hija 
debe ser sustituible por su clase padre. El principio de sustitución de 
Liskov tiene como objetivo garantizar que la clase hija pueda asumir 
el lugar de su clase padre sin causar ningún error.

Básicamente consiste en poder replazar cualquier clase hija en lugar
de un respectivo padre.
"""
from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def notify(self, message: str):
        pass


class Email(Notification):
    def __init__(self, email: str) -> None:
        self.email = email

    def notify(self, message: str):
        print(f'Send "{message}" to {self.email}')


class SMS(Notification):
    def __init__(self, phone: str) -> None:
        self.phone = phone

    def notify(self, message: str):
        print(f'Send "{message}" to {self.phone}')


class Contact:
    def __init__(self, name: str, email: str, phone: str) -> None:
        self.name = name
        self.email = email
        self.phone = phone


class NotificationManager:
    def __init__(self, notification: Notification) -> None:
        self.notification = notification

    def send(self, message: str):
        self.notification.notify(message)


def showExample01():
    contact = Contact('John Wick', 'johnwick@killer.com', '+525632140588')
    notificationSMS = SMS(contact.phone)
    notificationEMAIL = Email(contact.email)

    # manager de notificacion
    notificationManager = NotificationManager(notificationSMS)
    notificationManager.send('Hello John')

    # asignamos otro tipo de notificacion
    notificationManager.notification = notificationEMAIL
    notificationManager.send('Hi John')


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')

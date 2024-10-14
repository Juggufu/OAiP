class SecuritySystemFacade:
    def __init__(self):
        self.security_system = SecuritySystem()
        self.camera_control = CCTV()
        self.access_control = AccessControl()
        self.signaling = Signaling()

    def active_full_securitysystem(self):
        self.security_system.activation()
        self.camera_control.cctvactive()
        self.access_control.accesscontrolactive()
        print('Система полной безопасности активированна.')

    def deactive_full_securitysystem(self):
        self.security_system.deactivation()
        self.camera_control.cctvdeactive()
        self.access_control.accesscontroldeactive()
        self.signaling.signalingdeactive()
        print('Система полной безопасности выключена.')

    def authorization(self, user):
        self.access_control.access_granted(user)

    def unauthorization(self, user):
        self.access_control.access_denied(user)
        self.signaling.signalingactive()


class SecuritySystem:
    def activation(self):
        print('Система Безопасности активирована.')

    def deactivation(self):
        print('Система Безопасности выключнеа.')


class CCTV:
    def cctvactive(self):
        print('Видеонаблюдение активировано. Запись начата.')

    def cctvdeactive(self):
        print('Видеонаблюдение выключено. Запись остановлена.')


class AccessControl:
    def access_vvod(self):
        self.user = input()

    def accesscontrolactive(self):
        print('Контроль доступа активирован.')

    def access_granted(self, user):
        print(f"Доступ предоставлен пользователю: {user}")

    def access_denied(self, user):
        print(f"Отказ в доступе пользователю: {user}")

    def accesscontroldeactive(self):
        print('Контроль доступа выключнен.')


class Signaling:
    def signalingactive(self):
        print('Сигнализация была активирована.')

    def signalingdeactive(self):
        print('Сигнализация была выключнеа.')


security_facad = SecuritySystemFacade()
security_facad.active_full_securitysystem()
security_facad.authorization('Бакрсук')
security_facad.deactive_full_securitysystem()

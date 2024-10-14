from abc import ABC, abstractmethod

class RemoteControl(ABC):
    @abstractmethod
    def tern_on(self):
        pass

    @abstractmethod
    def tern_off(self):
        pass

    @abstractmethod
    def volume_increase(self):
        pass

    @abstractmethod
    def decrease_volume(self):
        pass


class Television(RemoteControl):
    def tern_on(self):
        print('включение теливизора')

    def tern_off(self):
        print('выключение теливизора')

    def volume_increase(self):
        print('увеличение громкости')

    def decrease_volume(self):
        print('уменьшенмие громкости')


class Radio(RemoteControl):
    def tern_on(self):
        print('включение радио')

    def tern_off(self):
        print('выключение радио')

    def volume_increase(self):
        print('увеличение громкости')

    def decrease_volume(self):
        print('уменьшенмие громкости')


class IRRemoteControl:
    def __init__(self, devise:RemoteControl):
        self.devise = devise

    def off_on(self, state: bool):
        if state:
            self.devise.tern_on()
        else:
            self.devise.tern_off()

    def inclusion_volume(self):
        self.devise.volume_increase()

    def shutdown_volume(self):
        self.devise.decrease_volume()


if __name__ == '__main__':
    tv = Television()
    radio = Radio()

    tv_remote = IRRemoteControl(tv)
    tv_remote.off_on(True)
    tv_remote.inclusion_volume()
    tv_remote.off_on(False)
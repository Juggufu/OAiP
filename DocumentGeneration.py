from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def save(self):
        raise NotImplementedError()

    @abstractmethod
    def create(self):
        raise NotImplementedError()


class PDFdocument(Document):
    def create(self):
        print('файл формата PDF создан')

    def save(self):
        print('файл формата PDF сохранен')


class Worddocument(Document):
    def create(self):
        print('файл формата Word создан')

    def save(self):
        print('файл формата Word сохранен')


class ExcelDocument(Document):
    def create(self):
        print('файл формата Excel создан')

    def save(self):
        print('файл формата Excel сохранен')


class Applocation(ABC):
    def create_document(self, type_):
        raise NotImplementedError()

    def save_document(self, type_):
        raise NotImplementedError()


class MyApplocation(Applocation):
    def create_document(self, type_):
        if type_ == 'PDF':
            return PDFdocument()
        elif type_ == 'Word':
            return Worddocument()
        elif type_ == 'Excel':
            return ExcelDocument()

    def save_document(self, type_):
        if type_ == 'PDF':
            return PDFdocument()
        elif type_ == 'Word':
            return Worddocument()
        elif type_ == 'Excel':
            return ExcelDocument()


if __name__ == '__main__':
    app = MyApplocation()
    app.create_document('PDF').create()
    app.create_document('Word').create()
    # app.create_document('Exel').create()
    app.save_document('PDF').save()
    app.save_document('Word').save()
    # app.save_document('Excel').save()

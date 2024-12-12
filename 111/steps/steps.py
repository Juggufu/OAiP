from behave import given, when, then
from bdd.db import Database
from bdd.gui import GUI
from PyQt6.QtWidgets import QApplication


@given("база данных инициализирована")
def step_init_database(context):
    context.db = Database()


@when('я добавляю запись с именем и возрастом ')
def step_add_record(context, name, age):
    context.db.add_record(name, int(age))


@then('запись с именем должна быть в базе данных')
def step_check_record(context, name):
    records = context.db.get_all_records()
    assert any(record[1] == name for record in records)


@given("приложение запущено")
def step_start_gui(context):
    context.app = QApplication([])
    context.window = GUI()


@when('я нажимаю на кнопку "Открыть окно"')
def step_press_button(context):
    context.window.button.click()


@then("окно должно быть открыто")
def step_check_window(context):
    assert context.window.isVisible()

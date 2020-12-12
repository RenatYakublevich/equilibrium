"""
Файл typess
Все типы данных
"""
import exceptions


def choose_type(value, variables, types):
    if types == 'string':
        return String(value, variables).return_value()
    elif types == 'int':
        return Int(value, variables).return_value()
    elif types == 'array':
        return Array(value, variables).return_value()
    elif types == 'float':
        return Float(value, variables).return_value()
    elif types == 'char':
        return Char(value, variables).return_value()
    else:
        return value


class Int:
    def __init__(self, value, variables):
        try:
            self.value = int(eval(value, variables))
        except TypeError as e:
            exceptions.Type_Error('Объект не является числом')

    def return_value(self):
        return int(self.value)


class String:
    def __init__(self, value, variables):
        try:
            self.value = str(eval(value, variables))
        except TypeError as e:
            exceptions.Type_Error('Объект не является строкой')

    def return_value(self):
        return self.value


class Array:
    def __init__(self, value, variables):
        try:
            self.value = eval(str(value), variables)

        except TypeError as e:
            exceptions.Type_Error('Объект не является массивом')

    def return_value(self):
        return self.value


class Float:
    def __init__(self, value, variables):
        try:
            self.value = float(eval(value, variables))

        except TypeError as e:
            exceptions.Type_Error('Объект не является дробью')

    def return_value(self):
        return self.value


class Char:
    def __init__(self, value, variables):
        try:
            if len(value.replace("'", "")) > 1:
                exceptions.Type_Error('Объект не является символом')
            else:
                self.value = eval(str(value), variables)
        except TypeError:
            exceptions.Type_Error('Объект не является символом')

    def return_value(self):
        return self.value
class CustomException1(BaseException):
    pass

class CustomException2(BaseException):
    pass

class CustomException3(BaseException):
    pass

class MyClass:
    def method1(self):
        #Пример метода, который выбрасывает исключение
        raise CustomException1("Ошибка в методе method1")

    def method2(self):
        #Пример метода, который выбрасывает другое исключение
        raise CustomException2("Ошибка в методе method2")

    def method3(self):
        #Пример метода, который выбрасывает третье исключение
        raise CustomException3("Ошибка в методе method3")

class ExceptionHandler:
    def handle_exceptions(self, obj):
        try:
            #Вызов методов объекта obj
            obj.method1()
            obj.method2()
            obj.method3()
        except CustomException1 as e:
            print("Обработка исключения CustomException1:", str(e))
        except CustomException2 as e:
            print("Обработка исключения CustomException2:", str(e))
        except CustomException3 as e:
            print("Обработка исключения CustomException3:", str(e))
        except BaseException as e:
            print("Обработка других исключений:", str(e))

#Пример использования
my_obj = MyClass()
exception_handler = ExceptionHandler()
exception_handler.handle_exceptions(my_obj)

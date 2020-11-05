from datetime import datetime
from decor_path import decor_path


def logger(function):

    def old_function(*args, **kwargs):

        result = function(*args, **kwargs)
        with open('log_file_name.log', 'a') as file:
            file.write(f'Функцию {function.__name__} вызвали в {datetime.now()} со следующими аргументами '
                       f'{[arg for arg in args]}, и {[(key, val) for key, val in kwargs]}. В результате получили '
                       f'{result}\n')

        return result

    return old_function


@decor_path
@logger
def foo(a, b, c):
    return a + b + c


foo(8, 5, 2)



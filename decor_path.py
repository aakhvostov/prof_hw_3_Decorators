from os import path


def decor_path(function):

    def old_function(*args, **kwargs):

        result = function(*args, **kwargs)
        print(f'Логи хранятся в файле с адресом {path.abspath("log_file_name.log")}')
        return result

    return old_function

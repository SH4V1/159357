from datetime import datetime

log_list = []

def logger(func):
    def wrapper(*args, **kwargs):
        current_datetime = datetime.now()
        function_name = func.__name__
        try:
            result = func(*args, **kwargs)
            status = 'success'
        except Exception as error:
            result = f'failed: {error}'
            status = 'failed'
        
        log_data = f'{current_datetime}, {function_name}, {args}, {result}, {status}'
        log_list.append(log_data)
        return log_data

    return wrapper

@logger
def some_function(input_text):
    return input_text

some_function('nastya')
some_function('senchyk')

def get_logs():
    with open('l6.txt', 'a') as log_file:
        for log_data in log_list:
            log_file.write(log_data + '\n')
            yield log_data

log = get_logs()
print(next(log))
print(next(log))

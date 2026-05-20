### დეკორატორები

###task1

def number_check(func):
    def wrapper(*args, **kwargs):
        for num in args:
            if num < 0:
                return "შედეგი აუცილებლად უნდა იყოს დადებითი"
        return func(*args, **kwargs)
    return wrapper
@number_check
def sum_of_digits(a, b):
    return a + b
@number_check
def multy_of_digits(a, b):
    return a * b
print(multy_of_digits(2, 3))
print(sum_of_digits(2, 3))
print(sum_of_digits(-5, 3))




### task 2

def loggin(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'გამოვიძახეთ ფუნქცია {func.__name__}, მას გადაეწოდა ატრიბუტები {args} -ის სახით, რამაც დაგვიბრუნა შედეგი {result}')

        return result
    return wrapper
@loggin
def sum_of_digits(a, b):
    return a + b
print(sum_of_digits(2, 3))
print(sum_of_digits(-5, 3))




### task 3

import time

def repeat_action(times, delay):

    def decorator(func):


        def wrapper(*args, **kwargs):
            last_result = None


            for i in range(times):

                last_result = func(*args, **kwargs)


                if i < times - 1:
                    print(f"[Delaying for {delay} seconds...]")
                    time.sleep(delay)

            return last_result

        return wrapper

    return decorator

@repeat_action(times=3, delay=1)
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alex")        ### gavakete ai daxmarebit. vecdebi xelaxla gaviaro es decoratoris factory




### ავტორიზაცია, უსაფრთხოება task 4

current_user = {
    'username': 'Irakli',
    'role':'admin'
}

def role_required(allowed_role):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if current_user['role'] == allowed_role:
                return func(*args, **kwargs)
            else:
                print('permission denied')
                return None
        return wrapper
    return decorator
@role_required('admin')
def delate_user(user_id):
    print(f'Delated user {user_id} successfully')
@role_required('editor')
def edit_user(user_id):
    print(f'Edited user {user_id} successfully')
@role_required('user')
def create_user(user_id):
    print(f'Created user {user_id} successfully')



### აქვე დავწერ რომ არ დავამავიწყდეს.
######## გამიჭირდა გაკეთბა, თუ შეიძლება decorate factories და ეს მაგალითი განვიხილოთ ლექციაზე, როცა დრო იქნება.

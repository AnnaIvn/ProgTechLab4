from flask import Flask

app = Flask(__name__)


def some_output():
    return "My dockerised app using flask"

# @app.route('/')
# def check_format(arg):
#     if arg[0] == '6' or arg[0] == '7' or arg[0] == '8' and len(arg) >= 4:
#         return True
#     raise ValueError("Incorrect input format")

# def two_dot_formating(arg):
#     if arg[1] != ':':
#         return str(arg[:1] + ':' + arg[1:])
#     return arg

# def space_formating(arg):
#     if arg[2] != ' ':

#         return str(arg[:2] + ' ' + arg[2:])
#     return arg

# def distrib_by_age(arg):
#     if int(arg[0]) == 6:
#         return str(arg + ' -> 1st grade')
#     elif int(arg[0]) == 7:
#         return str(arg + ' -> 2nd grade')
#     elif int(arg[0]) == 8:
#         return str(arg + ' -> 3rd grade')
#     else:
#         raise ValueError("Incorrect age")

# def exception(arg):
#     if int(arg[0]) == 5:
#         raise Exception("Age exception | 5 years -> 1st grade")
#     return arg

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)

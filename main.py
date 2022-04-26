from bd import *

def Users():
    list = ['Gabriel', 'Emerson', 'Vitor']
    return list


# Criar login
def SignIn():
    user = input("Usuário: ")
    if user != "" and user.title() in Users():
        password = input("Password: ")
        if password != "":
            validation(user, password)
            print("ok")
    else:
        print("Erro")

# Criar Cadastro
def SignUp():
    new_user = input('New User: ').title()
    if new_user != "" and len(new_user) >= 6:
        password = input("Password: ")
        if password != "" and len(password) >= 5:
            pw_repeat = input("Repeat Password: ")
            if password == pw_repeat:
                insert(new_user, password)
                interface()
            else:
                print("Usuario ou senha incorretos")
        else:
            print("Usuario ou senha incorretos")
    else:
        print("Usuario inválido (Mais que 6 caracteres)")

# Criar sistema de escolha
def choice(c):
    if c == 1:
        SignUp()
    elif c == 2:
        SignIn()
    elif c == 3:
        print('About')
    elif c == 0:
        print('Exit')
    else:
        print("Erro")

# Criar interface inicial
def interface():
    print("==== WELCOME ====")
    print("User Options:")
    print("1 - Sign Up")
    print("2 - Sign In")
    print("3 - About")
    print("0 - Exit")
    c = int(input("> "))
    choice(c)


interface()

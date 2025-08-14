# Nada de hacking aqui, só demosntração de como usa uma lib que aceita argumentos;
import sys
import getopt

def main():
    user = ''
    password = ''
    try:
        opts, args = getopt.getopt(sys.argv[1:], "u:p:", ["user=", "password="])
    except getopt.GetoptError:
        print("Uso: script.py -u <usuario> -p <senha>")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-u", "--user"):
            user = arg
        elif opt in ("-p", "--password"):
            password = arg

    print(f"Usuário: {user}")
    print(f"Senha: {password}")

if __name__ == "__main__":
    main()

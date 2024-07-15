import sys

def get_args(num_args, mensaje_uso="Número incorrecto de argumentos"):
    if(len(sys.argv)) != num_args+1:
        print("Error en el numero de argumentos:", mensaje_uso)
        sys.exit(1)
    return sys.argv[1:]

#usalo con

# if __name__ == "__main__":
#     argumento1, argumento2, argumento3 = get_args(3)
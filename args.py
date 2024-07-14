import sys

if __name__ == "__main__":
    # Verifica que se proporcionen suficientes argumentos
    if len(sys.argv) != 3:
        print("Uso: python args.py <a> <b>")
        print(len(sys.argv))
        sys.exit(1)

    # Obtén los nombres de archivo de los argumentos de línea de comandos
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    
    print(f"arg1: {arg1}")
    print(f"arg2: {arg2}")
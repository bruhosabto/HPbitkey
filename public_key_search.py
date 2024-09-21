import random
import multiprocessing
import sys
import termios
import tty
from ecdsa import SECP256k1, SigningKey, VerifyingKey
import math
import time
from Stock import Stocked

def get_cursor_position():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        sys.stdout.write("\033[6n")
        sys.stdout.flush()

        response = ""
        while True:
            ch = sys.stdin.read(1)
            response += ch
            if ch == "R":
                break
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    response = response.lstrip("\033[")
    rows, cols = map(int, response[:-1].split(";"))
    return rows, cols

def process_key_search_public(provided_public_key, comeco,comeco_curto,linha,start,end):
    contador = 0
    
    start_time = time.time()
    roda = True
    
    while roda:
        
        #print(f"\33[{linha+3}HNovo range:{hex(start_range)} até {hex(end_range)} total:{contador}")
        private_key = random.randint(start, end)
        private_key_hex = format(private_key, '064x')  # Formatar para hexadecimal com 64 caracteres
        #private_key_hex = generate_private_key()
        
        # Converter a chave privada hexadecimal para bytes
        private_key_bytes = bytes.fromhex(private_key_hex)
        
        # Gerar a chave privada usando a curva SECP256k1
        private_key = SigningKey.from_string(private_key_bytes, curve=SECP256k1)
        
        # Aplicar 
        public_key = private_key.get_verifying_key()
        
        # Converter a chave pública para o formato hexadecimal comprimido
        contador += 1
        public_key_hex =  public_key.to_string().hex()[:64]

        
        # Converter a chave pública para o formato hexadecimal comprimido
        contador+=1
        #public_key_hex = "03afd" + public_key.to_string().hex()[:64]
        #print(f"\33[{linha+4}Hpublic key:{public_key_hex} private key:{private_key_hex} Total:{contador}")
        if not public_key_hex.startswith(comeco_curto):
            continue
        print(f"\33[{linha+5}Hpublic key:{public_key_hex}\nprivate key:{private_key_hex}")
            
        
        
        if not public_key_hex.startswith(comeco) :
            continue
        print(f"\33[{linha+6}Hpublic key:{public_key_hex}\nprivate key:{private_key_hex} Total:{contador}")
        
        # Comparar a chave pública gerada com a fornecida
        if public_key_hex == provided_public_key:
            print("CHAVE PRIVADA ENCONTRADA!\n Parabéns Bruno S. Santos seu puto!")
            print(f"Chave Privada: {private_key_hex}")
            print(f"Chave Pública Gerada: {public_key_hex}")
            abrir = open('privatekeyfound.txt','a')
            abrir.write(f"private key:{private_key_hex}\n")
            abrir.close()
            roda = False
            break

num_processes = multiprocessing.cpu_count()
linha, c = get_cursor_position()

try:
    print("Opções: [130,135,140,145,150,155,160]")
    opt = int(input(":>"))
except ValueError as erro:
    print(erro)
    sys.exit()
stocked = Stocked()
chave_publica_alvo = stocked.getPublic_key(opt)
if chave_publica_alvo is None:
    print("[!] Chave pública não encontrada!")
    sys.exit()
start, end = stocked.getRanger(opt)
comeco = chave_publica_alvo[:4]
comeco_curto = chave_publica_alvo[:2]
processes = []
for _ in range(num_processes):
    p = multiprocessing.Process(target=process_key_search_public, args=(chave_publica_alvo, comeco,comeco_curto,linha,start,end))
    processes.append(p)
    p.start()   



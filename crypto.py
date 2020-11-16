from cryptography.fernet import Fernet


def gerar_chave():
    key = Fernet.generate_key()
    with open("./key/secret.key", "wb") as key_file:
        key_file.write(key)


def carregar_chave():
    return open("./key/secret.key", "rb").read()


def renovar_chave():
    old_key = open("./key/secret.key", "rb").read()
    gerar_chave()
    return f'Chave antiga: {old_key.decode()}'


def enviar_chave(new_key):
    old_key = open("./key/secret.key", "rb").read()
    open("./key/secret.key", "wb").write(new_key.encode())
    return f'Chave antiga: {old_key.decode()}'


def encrypt(text):
    text = text.encode()
    key = carregar_chave()
    encrypted_text = Fernet(key).encrypt(text)
    return encrypted_text


def decrypt(text):
    key = carregar_chave()
    decrypted_text = Fernet(key).decrypt(text.encode())
    return decrypted_text

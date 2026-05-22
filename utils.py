from usuario import Usuario
def verificar_login(usuario, senha, lista_usuarios):
    for u in lista_usuarios:
        if usuario == u.nome and senha == u.senha:
            return u
    return None
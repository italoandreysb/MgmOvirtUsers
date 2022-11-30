"""
Nome: Ovirt_mgm_user.
Versão: 1.5.
Função: Automatizar o gerenciamento de usuários e grupos do Ovirt.
"""
import os
import time

print('Bem-vindo ao Ovirt MGM user')
try:
    decisao = '0'
    decisao = int(input(
        'Digite o número correspondente: \n'
        '1. Criar usuário; \n'
        '2. Alterar senha de usuário; \n'
        '3. Criar grupo; \n'
        '4. Remover usuario; \n'
        ))

except (ValueError, TypeError, NameError):
    print('Houve um erro, favor digitar um número entre de 1 e 4')

try:
    """Criação de usuário"""
    if decisao == 1:
        nome_usu = str(input('Primeiro nome do usuário: \nEx: Petter \n'))
        sobrenome_usu = str(input('Último sobrenome do usuário: \nEx: Parker \n'))
        cria_user = ('ovirt-aaa-jdbc-tool user add ' + nome_usu.lower() + '.' + sobrenome_usu.lower() + ' --attribute=firstName=' + nome_usu.title() + ' --attribute=lastName=' + sobrenome_usu.title())
        desbloqueia_user = ('ovirt-aaa-jdbc-tool user unlock ' + nome_usu.lower() + '.' + sobrenome_usu.lower())
        grupo_pertencente = str(input('A qual grupo o usuário pertencerá? \n'))
        grupo_pertencente = ('ovirt-aaa-jdbc-tool group-manage useradd ' + grupo_pertencente.title() + ' --user=' + nome_usu.lower() + '.' + sobrenome_usu.lower())

        # Comando a ser executado:
        os.system(cria_user + '\n' + desbloqueia_user + '\n' + grupo_pertencente)

        """Inserindo senha"""
        print(
            'Insira a senha do usuario: \n'
            'Igual ou maior que 8 digitos \n'
        )
        insere_senha = ('ovirt-aaa-jdbc-tool user password-reset ' + nome_usu.lower() + '.' + sobrenome_usu.lower() + ' --password-valid-to="2070-01-01 08:00:00-0300"')

        # Comando a ser executado:
        os.system(insere_senha)
        time.sleep(3)

        print(
            'Para finalizar o cadastro, execute os procedimentos abaixo via portal web do Ovirt \n'
            '1 - Acesse o Portal de Administração; \n'
            '2 - Vá ao Menu Administração > Usuários; \n'
            '3 - Escolha a opção Adicionar - Usuário e informe o usuário (nome.sobrenome) criado - Iniciar; \n'
            '4 - Selecione o usuário - Adicionar e fechar; \n'
            )

    """Alteracao de senha de usuario"""
    if decisao == 2:
        nome_usu = str(input(
            'Qual o nome do usuário? \n'
            'Ex: petter.parker \n'
        ))
        altera_senha = ('ovirt-aaa-jdbc-tool user password-reset ' + nome_usu.lower() + ' --password-valid-to="2070-01-01 08:00:00-0300"')

        # Comando a ser executado:
        os.system(altera_senha)
        

    """Criacao de grupo"""
    if decisao == 3:
        nome_grupo = str(input('Digite o nome do grupo: \n'))
        nome_grupo = ('ovirt-aaa-jdbc-tool group add ' + nome_grupo.title())

        # Comando a ser executado
        os.system(nome_grupo.title())


    """Remocao de usuario"""
    if decisao == 4:
        remove_usu = str(input(
            'Qual o usuário que deseja remover? \n'
            'Ex: petter.parker \n'
            ))
        confirma_remocao = str(input(
            'Tem certeza que deseja remover o usuario ' + remove_usu.lower() + '? \n'
            'S para SIM | N para NAO \n'
        ))
        if confirma_remocao.lower() == 's':

            # Comando a ser executado
            os.system('ovirt-aaa-jdbc-tool user delete ' + remove_usu.lower())
        else:
            print('Remocao cancelada')
except (ValueError, TypeError, NameError):
    print('Houve um erro, favor digitar um valor válido')

"""Fontes:
 https://rhv.bradmin.org/ovirt-engine/docs/Administration_Guide/sect-Administering_User_Tasks_From_the_commandline.html
 https://intranet.bktele.com.br/index.php/How_To_-_Criar_usu%C3%A1rio_na_plataforma_Ovirt
 By: Ítalo Andrey
"""
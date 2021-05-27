import selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import os
import flask
from flask import request,jsonify
from flask_cors import CORS, cross_origin

app = flask.Flask(__name__)
app.config["DEBUG"] = True
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'



option = Options()
option.headless = True
driver = webdriver.Chrome()

url = "https://produtos.synchro.com.br/pages/view/"
driver.get(url)

def logar():
    driver.find_element_by_xpath('//*[@id="login-button"]').click()
    driver.find_element_by_xpath('//*[@id="j_username"]').send_keys("abreu@gesif.com.br")
    driver.find_element_by_xpath('//*[@id="j_password"]').send_keys("12345")
    driver.find_element_by_xpath('//*[@id="entrar"]').click()

def listar(ano,coluna):
    vetor_coluna = coluna.splitlines()
    vetor_traduzido = []
    for x in vetor_coluna:
        if x[len(x) - 4:len(x)] == ano:
            vetor_traduzido.append(x)
    return jsonify(vetor_traduzido)

logar()



def percorre_tabela(url):
    driver.get(url)
    data_release_atual = driver.find_element_by_xpath(
        '//*[@id="principal-body"]/div[1]/div[6]/div/div/div[2]/div/div/div/div/table/tbody/tr[1]/td[2]').text[0:8]
    xpath = '//*[@id="principal-body"]/div[1]/div[6]/div/div/div[2]/div/div/div/div/table/tbody/tr['

    print(data_release_atual)
    lista_releases_atuais = []
    elemento_mais_recente = driver.find_element_by_xpath(xpath + '1]/td[1]/span/a').text
    final = 1
    i = 1
    while (final):
        try:
            elemento = driver.find_element_by_xpath(xpath + str(i) + ']/td[1]/span/a').text
            data_elemento = driver.find_element_by_xpath(xpath + str(i) + ']/td[2]').text[0:8]
        except:
            break
        if data_elemento == data_release_atual:
            lista_releases_atuais.append(elemento)
            i += 1
        else:
            break
    return jsonify(lista_releases_atuais)


@app.route('/teste', methods=['GET'])
@cross_origin()
def teste():
    return 'a'

# print("bem vindo ao robô bizonho")
# while(1+1==2):
#     print("escolha sua opção:")
#     print("1)DFe")
#     print("2)Conector")
#     print("3)CTe")
#     print("4)Solfis")
#     print("5)SFW")
#     print("6)NFE")
#     print("7)Certificado da SEFAZ")
#     menu_principal = input("R: ")

#     # ------------------DFE------------------
#
# @app.route('/
# dfe', methods=['GET'])
@app.route('/dfe', methods=['GET'])
@cross_origin()
def dfe():
    url = 'http://produtos.synchro.com.br/pages/view/content/dfe/releases'
    driver.get(url)
    data_liberacao = driver.find_element_by_xpath(
        '//*[@id="principal-body"]/div[1]/div[4]/div/div[1]/div[2]/div/p').text
    versao_dfe = driver.find_element_by_xpath(
        '//*[@id="principal-body"]/div[1]/div[4]/div/div[1]/div[1]/div/h2/small').text
    coluna = driver.find_element_by_xpath('//*[@id="principal-body"]/div[1]/div[4]/div/div[2]').text
    menu_versao = request.args['versao']
    if menu_versao == '1':
        ano = request.args['ano']
        return listar(ano, coluna)
    if menu_versao == '2':
        return 'Versão atual do DFe: ' + versao_dfe + ' ' + data_liberacao


# ------------------CONECTOR DFE------------------
# @app.route('/
# conector', methods=['GET'])
# @cr@app.route('/dfe', methods=['GET'])

# def conector():
# url = 'https://produtos.synchro.com.br/downloads/dfe/Conector_DFe'
# driver.get(url)
# table = driver.find_element_by_xpath(
#     '//*[@id="principal-body"]/div[1]/div[6]/div/div/div[2]/div/div/div/div/table').text
# texto_inicial = table.splitlines()[0]
# indice = (texto_inicial.find('NT'))
# versao_conector = texto_inicial[indice:indice + 18]
# data = table.splitlines()[0][len(table.splitlines()[0]) - 8:len(table.splitlines()[0]) - 6]
# data_texto = table.splitlines()[0][len(table.splitlines()[0]) - 14:len(table.splitlines()[0]) - 6]
# if data == re
# quest.args['ano']: print('Versão atual do Conector: ' + versao_conector + "liberado em " + data_texto)
@app.route('/conector-dfe', methods=['GET'])
@cross_origin()
def conector_dfe():
    url = 'https://produtos.synchro.com.br/downloads/dfe/Conector_DFe'
    return percorre_tabela(url)


# # ------------------CTE------------------
# @app.route('/
# cte', methods=['GET'])
# @cr@app.route('/dfe', methods=['GET'])

# def cte():
#     url = 'http://produtos.synchro.com.br/downloads/dfe/CTe'
#     driver.get(url)
#     table = driver.find_element_by_xpath(
#         '//*[@id="principal-body"]/div[1]/div[6]/div/div/div[2]/div/div/div/div/table').text
#     emissao = table.splitlines()[1].split('-')[0]
#     emissao_recepcao = table.splitlines()[0].split('-')[0]
#     data = table.splitlines()[0][len(table.splitlines()[0]) - 8:len(table.splitlines()[0]) - 6]
#     data_texto = table.splitlines()[0][len(table.splitlines()[0]) - 14:len(table.splitlines()[0]) - 6]
#     if data =
#     = request.args['ano']: return("Versões do CT-e: 1. Emissão: " + emissao + " 2. Recepção: " + emissao_recepcao + "liberados em " + data_texto)
@app.route('/cte', methods=['GET'])
@cross_origin()
def cte():
    try:
        url = 'http://produtos.synchro.com.br/downloads/dfe/CTe'
        percorre_tabela(url)
    except selenium.common.exceptions.NoSuchElementException:
        return


# # ------------------SOLFIS------------------

@app.route('/solfis', methods=['GET'])
@cross_origin()
def solfis():
    url = "http://produtos.synchro.com.br/pages/view/content/solfis/releases"
    driver.get(url)
    versao_solfis = driver.find_element_by_xpath('//*[@id="principal-body"]/div[1]/div[4]/div/div[1]/div[1]/div/h2/small').text
    data_liberacao = driver.find_element_by_xpath('//*[@id="principal-body"]/div[1]/div[4]/div/div[1]/div[2]/div/p').text
    versao = request.args['versao']
    if versao == '1' :return("Versão atual da SOLFIS: " + versao_solfis + ' ' + data_liberacao)
    coluna = driver.find_element_by_xpath('//*[@id="principal-body"]/div[1]/div[4]/div/div[2]').text
    ano = request.args['ano']
    if versao == '2':return listar(ano, coluna)

# # ------------------SFW------------------
# @app.route('/
# sfw', methods=['GET'])
@app.route('/sfw', methods=['GET'])
@cross_origin()
def sfw():
    url = "http://produtos.synchro.com.br/pages/view/content/sfw/releases"
    driver.get(url)
    versao_sfw = driver.find_element_by_xpath(
        '//*[@id="principal-body"]/div[1]/div[4]/div/div[1]/div[1]/div/h2/small').text
    data_liberacao = driver.find_element_by_xpath(
        '//*[@id="principal-body"]/div[1]/div[4]/div/div[1]/div[2]/div/p').text
    versao = request.args['versao']
    if versao == '1' :return("Versão atual da SFW: " + versao_sfw + ' ' + data_liberacao)
    coluna = driver.find_element_by_xpath('//*[@id="principal-body"]/div[1]/div[4]/div/div[2]').text
    ano = request.args['ano']
    if versao == '2': return listar(ano, coluna)

# # ------------------NFE------------------
# @app.route('/
# nfe', methods=['GET'])
# @cr@app.route('/dfe', methods=['GET'])

# def nfe():
#     url = "https://produtos.synchro.com.br/downloads/dfe/NFe"
#     driver.get(url)
#     table = driver.find_element_by_xpath(
#         '//*[@id="principal-body"]/div[1]/div[6]/div/div/div[2]/div/div/div/div/table').text
#     texto_inicial = table.splitlines()[0]
#     indice = (texto_inicial.find('NT'))
#     versao_nfe = texto_inicial[indice:indice + 18]
#     data = table.splitlines()[0][len(table.splitlines()[0]) - 8:len(table.splitlines()[0]) - 6]
#     data_texto = table.splitlines()[0][len(table.splitlines()[0]) - 14:len(table.splitlines()[0]) - 6]
#     objeto = {"versao_nfe":versao_nfe,"data":data_texto}
#     if data =
#     = request.args['ano']: return jsonify(objeto)
@app.route('/nfe', methods=['GET'])
@cross_origin()
def nfe():
    try:
        url = 'https://produtos.synchro.com.br/downloads/dfe/NFe'
        percorre_tabela(url)
    except selenium.common.exceptions.NoSuchElementException:
        return

# # ------------------CERTIFICADO SEFAZ------------------
# @app.route('/
# certificado', methods=['GET'])
# @cr@app.route('/dfe', methods=['GET'])

# def certificado():
#     url = "http://produtos.synchro.com.br/downloads/dfe/Certificados_Sefaz"
#     driver.get(url)
#     table = driver.find_element_by_xpath(
#         '//*[@id="principal-body"]/div[1]/div[6]/div/div/div[2]/div/div/div/div/table').text
#     data_texto_hml = driver.find_element_by_xpath(
#         '//*[@id="principal-body"]/div[1]/div[6]/div/div/div[2]/div/div/div/div/table/tbody/tr[1]/td[2]').text
#     data_texto_prod = driver.find_element_by_xpath(
#         '//*[@id="principal-body"]/div[1]/div[6]/div/div/div[2]/div/div/div/div/table/tbody/tr[2]/td[2]').text
#     data_texto_hml_filtrada = data_texto_hml[len(data_texto_hml[0]) - 15:len(data_texto_hml[0]) - 6]
#     data_texto_prod_filtrada = data_texto_prod[len(data_texto_prod[1]) - 15:len(data_texto_prod[1]) - 6]
#     return("O
#     certificado da SEFAZ teve sua última atualização em " + data_texto_hml_filtrada + "(hml) e " + data_texto_prod_filtrada + "(prod)")
@app.route('/certificado-sefaz', methods=['GET'])
@cross_origin()
def certificado_sefaz():
    try:
        url =  "http://produtos.synchro.com.br/downloads/dfe/Certificados_Sefaz"
        percorre_tabela(url)
    except selenium.common.exceptions.NoSuchElementException:
        return


@app.route('/mdfe', methods=['GET'])
@cross_origin()
def mdfe():
    try:
        url = "http://produtos.synchro.com.br/downloads/dfe/MDF-e"
        percorre_tabela(url)
    except selenium.common.exceptions.NoSuchElementException:
        return

# # ------------------REINF------------------

@app.route('/reinf', methods=['GET'])
@cross_origin()
def reinf():
    try:
        url = "http://produtos.synchro.com.br/downloads/solfis/Retidos/REINF"
        percorre_tabela(url)
    except selenium.common.exceptions.NoSuchElementException:
        return


@app.route('/ativo-imobilizado-e-ciap', methods=['GET'])
@cross_origin()
def ativo_imobilizado_e_ciap():
    try:
        url = 'http://produtos.synchro.com.br/downloads/solfis/Ativo_Imobilizado_e_CIAP'
        percorre_tabela(url)
    except selenium.common.exceptions.NoSuchElementException:
        return

@app.route('/emif', methods=['GET'])
@cross_origin()
def emif():
    try:
        url = 'http://produtos.synchro.com.br/downloads/solfis/EMIF'
        percorre_tabela(url)
    except selenium.common.exceptions.NoSuchElementException:
        return


@app.route('/expert-fiscal', methods=['GET'])
@cross_origin()
def expert_fiscal():
    try:
        url = 'http://produtos.synchro.com.br/downloads/solfis/Expert_Fiscal'
        percorre_tabela(url)
    except selenium.common.exceptions.NoSuchElementException:
        return


@app.route('/in', methods=['GET'])
@cross_origin()
def IN():
    try:
        url = 'http://produtos.synchro.com.br/downloads/solfis/IN'
        percorre_tabela(url)
    except selenium.common.exceptions.NoSuchElementException:
        return


@app.route('/obrigacoes', methods=['GET'])
@cross_origin()
def obrigacoes():
    try:
        url = 'http://produtos.synchro.com.br/downloads/solfis/Obrigacoes'
        percorre_tabela(url)
    except selenium.common.exceptions.NoSuchElementException:
        return


@app.route('/obrigacoes-estaduais-gerais', methods=['GET'])
@cross_origin()
def obrigacoes_estaduais_gerais():
    try:
        url = 'http://produtos.synchro.com.br/downloads/solfis/Obrigacoes/Estadual'
        percorre_tabela(url)
    except selenium.common.exceptions.NoSuchElementException:
        return


uf = ['AC','AL','AM','AP','BA','CE','DF','ES','GO',
      'MA','MG','MS','MT','PA','PB','PE','PI','PR',
      'RJ','RN'
           'RO','RR','RS','SC','SE','SE','SP','TO']

@app.route('/obrigacoes-estaduais-todos-estados', methods=['GET'])
@cross_origin()
def obrigacoes_estaduais_todos():
        url = 'http://produtos.synchro.com.br/downloads/solfis/Obrigacoes/Estadual/'
        for estado in uf:
            try:
                percorre_tabela(url+estado)
            except selenium.common.exceptions.NoSuchElementException:

                continue

@app.route('/obrigacoes-estaduais', methods=['GET'])
@cross_origin()
def obrigacoes_estaduais_por_estado():
    try:
        url = 'http://produtos.synchro.com.br/downloads/solfis/Obrigacoes/Estadual/'
        percorre_tabela(url+request.args['uf'].upper())
    except selenium.common.exceptions.NoSuchElementException:
        return

@app.route('/obrigacoes-federais', methods=['GET'])
@cross_origin()
def obrigacoes_federais():
    try:
        url = 'http://produtos.synchro.com.br/downloads/solfis/Obrigacoes/Federal'
        percorre_tabela(url)
    except selenium.common.exceptions.NoSuchElementException:
        return

@app.route('/dirf', methods=['GET'])
@cross_origin()
def dirf():
    try:
        url = 'http://produtos.synchro.com.br/downloads/solfis/Obrigacoes/Federal/DIRF'
        percorre_tabela(url)
    except selenium.common.exceptions.NoSuchElementException:
        return

@app.route('/dirv-2016', methods=['GET'])
@cross_origin()
def dirf_2016():
    try:
        url = 'http://produtos.synchro.com.br/downloads/solfis/Obrigacoes/Federal/DIRF/DIRF_2016'
        percorre_tabela(url)
    except selenium.common.exceptions.NoSuchElementException:
        return

@app.route('/dirf-2017', methods=['GET'])
@cross_origin()
def dirf_2017():
    try:
        url = 'http://produtos.synchro.com.br/downloads/solfis/Obrigacoes/Federal/DIRF/DIRF_2017'
        percorre_tabela(url)
    except selenium.common.exceptions.NoSuchElementException:
        return


@app.route('/fci', methods=['GET'])
@cross_origin()
def fci():
    try:
        url = 'http://produtos.synchro.com.br/downloads/solfis/Obrigacoes/Federal/FCI'
        percorre_tabela(url)
    except selenium.common.exceptions.NoSuchElementException:
        return

@app.route('/integracao-oracle-r11i', methods=['GET'])
@cross_origin()
def integracao_oracle_r11i():
    try:
        url = 'http://produtos.synchro.com.br/downloads/solfis/Obrigacoes/Federal/FCI/Integracao_Oracle_R11i'
        percorre_tabela(url)
    except selenium.common.exceptions.NoSuchElementException:
        return

@app.route('/integracao-oracle-r12', methods=['GET'])
@cross_origin()
def integracao_oracle_r12():
    try:
        url = 'http://produtos.synchro.com.br/downloads/solfis/Obrigacoes/Federal/FCI/Integracao_Oracle_R12'
        percorre_tabela(url)
    except selenium.common.exceptions.NoSuchElementException:
        return

@app.route('/obrigacoes-municipais', methods=['GET'])
@cross_origin()
def obrigacoes_municipais():
    try:
        url = 'http://produtos.synchro.com.br/downloads/solfis/Obrigacoes/Municipal_(ISS)'
        percorre_tabela(url)
    except selenium.common.exceptions.NoSuchElementException:
        return

@app.route('/obrigacoes-municipais-rs', methods=['GET'])
@cross_origin()
def obrigacoes_municipais_rs():
    try:
        url = 'http://produtos.synchro.com.br/downloads/solfis/Obrigacoes/Municipal/RS'
        percorre_tabela(url)
    except selenium.common.exceptions.NoSuchElementException:
        return

@app.route('/nfse', methods=['GET'])
@cross_origin()
def nfse():
    try:
        url = 'http://produtos.synchro.com.br/downloads/solfis/Obrigacoes/NFSe'
        percorre_tabela(url)
    except selenium.common.exceptions.NoSuchElementException:
        return


@app.route('/conector-nfse', methods=['GET'])
@cross_origin()
def conector_nfse():
    try:
        url = 'http://produtos.synchro.com.br/downloads/solfis/Obrigacoes/NFSe/Conector_Synchro_NFSe'
        percorre_tabela(url)
    except selenium.common.exceptions.NoSuchElementException:
        return


@app.route('/nfse-rs', methods=['GET'])
@cross_origin()
def nfse_rs():
    try:
        url = 'http://produtos.synchro.com.br/downloads/solfis/Obrigacoes/NFSe/RS'
        percorre_tabela(url)
    except selenium.common.exceptions.NoSuchElementException:
        return


@app.route('/aplicador-service-pack', methods=['GET'])
@cross_origin()
def aplicador_service_pack():
    try:
        url = 'http://produtos.synchro.com.br/downloads/solfis/Solucao_Fiscal_Geral/Aplicador_de_Service_Pack'
        percorre_tabela(url)
    except selenium.common.exceptions.NoSuchElementException:
        return

@app.route('/sped-contabil', methods=['GET'])
@cross_origin()
def sped_contabil():
    try:
        url = 'http://produtos.synchro.com.br/downloads/solfis/SPED_Contabil'
        percorre_tabela(url)
    except selenium.common.exceptions.NoSuchElementException:
        return


@app.route('/sped-fiscal', methods=['GET'])
@cross_origin()
def sped_fiscal():
    try:
        url = 'http://produtos.synchro.com.br/downloads/solfis/SPED_Fiscal'
        percorre_tabela(url)
    except selenium.common.exceptions.NoSuchElementException:
        return


@app.route('/fcont', methods=['GET'])
@cross_origin()
def fcont():
    try:
        url = 'http://produtos.synchro.com.br/downloads/solfis/SPED_Contabil/FCONT'
        percorre_tabela(url)
    except selenium.common.exceptions.NoSuchElementException:
        return


@app.route('/solfis-geral', methods=['GET'])
@cross_origin()
def solfis_geral():
    try:
        url = 'http://produtos.synchro.com.br/downloads/solfis/Solucao_Fiscal_(Geral)'
        percorre_tabela(url)
    except selenium.common.exceptions.NoSuchElementException:
        return


@app.route('/sui', methods=['GET'])
@cross_origin()
def sui():
    try:
        url = 'http://produtos.synchro.com.br/downloads/solfis/Solucao_Fiscal_(Geral)/SUI_(SYNCHRO_Universal_Installer)'
        percorre_tabela(url)
    except selenium.common.exceptions.NoSuchElementException:
        return


@app.route('/integracao-solfis', methods=['GET'])
@cross_origin()
def integracao_solfis():
    try:
        url = 'http://produtos.synchro.com.br/downloads/sfw/Integracao_Solucao_Fiscal'
        percorre_tabela(url)
    except selenium.common.exceptions.NoSuchElementException:
        return

@app.route('/open-in', methods=['GET'])
@cross_origin()
def open_interfaces():
    try:
        url = 'http://produtos.synchro.com.br/downloads/integracoes/Open_Interfaces'
        percorre_tabela(url)
    except selenium.common.exceptions.NoSuchElementException:
        return

@app.route('/r11', methods=['GET'])
@cross_origin()
def r11():
    try:
        url = 'http://produtos.synchro.com.br/downloads/integracoes/Oracle/R11i'
        percorre_tabela(url)
    except selenium.common.exceptions.NoSuchElementException:
        return


@app.route('/r12-fiscal', methods=['GET'])
@cross_origin()
def r12_fiscal():
    try:
        url = 'http://produtos.synchro.com.br/downloads/integracoes/Oracle/R12/Fiscal'
        percorre_tabela(url)
    except selenium.common.exceptions.NoSuchElementException:
        return


@app.route('/r12-nfe', methods=['GET'])
@cross_origin()
def r12_nfe():
    try:
        url = 'http://produtos.synchro.com.br/downloads/integracoes/Oracle/R12/NFe'
        percorre_tabela(url)
    except selenium.common.exceptions.NoSuchElementException:
        return


@app.route('/sap', methods=['GET'])
@cross_origin()
def sap():
    try:
        url = 'http://produtos.synchro.com.br/downloads/integracoes/SAP'
        percorre_tabela(url)
    except selenium.common.exceptions.NoSuchElementException:
        return


@app.route('/sap-bloco-k-sped', methods=['GET'])
@cross_origin()
def sap_bloco_k_sped():
    try:
        url = 'http://produtos.synchro.com.br/downloads/integracoes/SAP/Bloco_K_SPED'
        percorre_tabela(url)
    except selenium.common.exceptions.NoSuchElementException:
        return

@app.route('/sap-bloco-k-instalacao', methods=['GET'])
@cross_origin()
def sap_bloco_k_sped_instalacao():
    try:
        url = 'http://produtos.synchro.com.br/downloads/integracoes/SAP/Bloco_K_SPED/Instalacao'
        percorre_tabela(url)
    except selenium.common.exceptions.NoSuchElementException:
        return

@app.route('/sap-nfe', methods=['GET'])
@cross_origin()
def sap_nfe():
    try:
        url = 'http://produtos.synchro.com.br/downloads/integracoes/SAP/nfe'
        percorre_tabela(url)
    except selenium.common.exceptions.NoSuchElementException:
        return

@app.route('/efd-contribuicoes', methods=['GET'])
@cross_origin()
def efd_contribuicoes():
    try:
        url = 'http://produtos.synchro.com.br/documentacao/sfw/EFD_Contribuicoes'
        percorre_tabela(url)
    except selenium.common.exceptions.NoSuchElementException:
        return

@app.route('/ecf', methods=['GET'])
@cross_origin()
def ecf():
    try:
        url = 'http://produtos.synchro.com.br/documentacao/sfw/ECF'
        percorre_tabela(url)
    except selenium.common.exceptions.NoSuchElementException:
        return

@app.route('/open-in-sped-fiscal', methods=['GET'])
@cross_origin()
def open_in_sped_fiscal():
    url = 'http://produtos.synchro.com.br/downloads/integracoes/Open_Interfaces/SPED_Fiscal'
    try:
        percorre_tabela(url)
    except selenium.common.exceptions.NoSuchElementException:
        return

app.run()

driver.quit()

# from typing import Tuple
# from django.conf import settings
# from enum import Enum, auto
import json
import requests
from abc import ABC, abstractmethod


class AMIS:

    HIR_CLAVE_COMPANIA = 218
    URL_SINIESTROS = 'https://api.amis.com.mx/api/amis/sapt/1.0.0/siniestro/consulta/aye'

    def __init__(self) -> None:
        self.token = requests.post(
            url=settings.AMIS_KEY['url'],
            data={'grant_type': 'client_credentials'},
            verify=False,
            allow_redirects=False,
            auth=(settings.AMIS_KEY["id"], settings.AMIS_KEY["secret"]),
        )
        self.token = json.loads(self.token.text)['access_token']

    def reportarImpedimento(self, url: str, data: dict) -> requests.Response:
        # diccionario de datos
        datosAEnviar = {
            'impedimento': {
                'ramo': data['ramo'],
                'claveDeCompania': data['claveDeCompania'],
                'fechaDeReporte': data['fechaDeReporte'],
                'fechaDeImpedimento': data['fechaDeImpedimento'],
                'claveCie10Oii': data['claveCie10Oii'],
                'parametro1': data['parametro1'],
                'parametro2': data['parametro2'],
                'pais': data['paisImpedimento'],
                'entidadFederativa': data['entidadFederativaImpedimento'],
                'municipio': data['municipioImpedimento'],
                'observaciones': data['observaciones'],
            },
            'asegurado': {
                'nombre': data['nombre'],
                'apellidoPaterno': data['apellidoPaterno'],
                'apellidoMaterno': data['apellidoMaterno'],
                'fechaDeNacimiento': data['fechaDeNacimiento'],
                'genero': data['genero'],
                'rfc': data['rfc'],
                'curp': data['curp'],
                'pais': data['paisAsegurado'],
                'entidadFederativa': data['entidadFederativaAsegurado'],
                'municipio': data['municipioAsegurado'],
            }
        }

        # json a enviar
        jsonData = json.dumps(datosAEnviar, ensure_ascii=False)

        # seteo de cabeceras
        headers = {
            'Authorization': f'Bearer {self.token}',
        }

        # solicitud
        response = requests.post(
            url=url,
            json=jsonData,
            headers=headers,
            verify=False,
        )

        return response

    def registrarSiniestroAP(self, url: str, data: dict) -> requests.Response:
        pass

    def registrarSiniestroVida(self, url: str, data: dict) -> requests.Response:
        pass

    def verificarExistenciaRegistroSiniestroAP(self, data: dict) -> bool:
        url = self.URL_SINIESTROS

        data = {
            'numeroDePoliza': data['noDePoliza'],
            'noCertificado': data['noCertificado'],
            'numeroDeSiniestro': data['noSiniestro'],
        }

        headers = {
            'Authorization': f'Bearer {self.token}',
        }

        response = requests.post(
            url=url,
            json=data,
            headers=headers,
            verify=False,
        )

        if response.status_code == 200 and 'poliza' in response.json().keys():
            return True

        # se ejecuta en casocontrarios
        print(
            f'Sin registro en amis: poliza: {data["noDePoliza"]}, noCertificado: {data["noCertificado"]}, noSiniestro: {data["noSiniestro"]}')
        return False


class SiniestroBuilder(ABC):

    def __init__(self) -> None:
        self.estaRegistradoEnAmis = False
        self.partes = {}

    @abstractmethod
    def obtenerDiccionarioParaConsulta(self):
        pass

    @abstractmethod
    def obtenerDiccionarioParaRegistro(self):
        pass


class SiniestroAP(SiniestroBuilder):

    def construirDatosGenerales(self, data: dict):
        self.partes['General'] = {k: v for k, v in data.items()}

    def construirDatosTitular(self, data: dict):
        self.partes['Titular'] = {k: v for k, v in data.items()}

    def construirDatosDelProveedor(self, data: dict):
        self.partes['Proveedor'] = {k: v for k, v in data.items()}

    def obtenerDiccionarioParaConsulta(self):
        return {
            'numeroDePoliza': self.partes['General']['noPoliza'],
            'noCertificado': self.partes['General']['noCertificado'],
            'numeroDeSiniestro': self.partes['General']['numeroDeSiniestro'],
        }

    def obtenerDiccionarioParaRegistro(self):
        return self.partes


class SiniestroVida(SiniestroBuilder):

    def construirDatosSiniestro(self, data: dict):
        self.partes['siniestro'] = {k: v for k, v in data.items()}

    def construirDateosAsegurado(self, data: dict):
        self.partes['asegurado'] = {k: v for k, v in data.items()}

    def construirDatosBeneficiario(self, data: dict):
        self.partes['beneficiario'] = {k: v for k, v in data.items()}

    def construirDatosContratante(self, data: dict):
        self.partes['contratante'] = {k: v for k, v in data.items()}

    def construirDatosTipoMovimiento(self, data: int):
        self.partes['tipoDeMovimiento'] = data

    def obtenerDiccionarioParaConsulta(self):
        return {
            'noDePoliza': self.partes['siniestro']['poliza']['noDePoliza'],
            'noDeCertificado': self.partes['siniestro']['poliza']['noDeCertificado'],
            'numeroDeSiniestro': self.partes['siniestro']['generales']['identificadorDelSiniestro'],
            'nombre': self.partes['asegurado']['generales']['nombre'],
            'apellidoPaterno': self.partes['asegurado']['generales']['apellidoPaterno'],
            'apellidoMaterno': self.partes['asegurado']['generales']['apellidoMaterno'],
            'genero': self.partes['asegurado']['generales']['genero'],
            'rfc': self.partes['asegurado']['generales']['rfcAsegurado']
        }

    def obtenerDiccionarioParaRegistro(self):
        return self.partes


if __name__ == '__main__':
    from pprint import pprint

    # test siniestroAP
    # s1 = SiniestroAP()
    # s1.construirDatosGenerales({
    #     'noPoliza': '12321',
    #     'numeroDeSiniestro': '0f0asf0',
    #     'numeroDeReclamacion': 'otroreclamo',
    #     'ramoSubramo': 1,
    #     'tipoCoberturaOProducto': 164,
    #     'noCertificado': '1232kf',
    #     'fechaAntiguedadDelAfectado': '10/03/2000',
    #     'nombreDelAfectado': 'John',
    #     'apellidoPaternoDelAfectado': 'Wick',
    #     'apellidoMaternoDelAfectado': 'Adan',
    #     'fechaNacimientoDelAfectado': '10/03/1990',
    #     'generoDelAfectado': 2,
    #     'rfcDelAfectado': 'AAHR900310GV2',
    #     'rfcDelReceptor': 'AA00AA00AA00A',
    # })

    # s1.construirDatosTitular({
    #     'cuentaBancariaClabe': 123421241,
    #     'banco': 1,
    #     'nombreTitularCuentaClabe': 'JUan Perez',
    # })

    # # pprint(s1.obtenerDiccionarioParaConsulta())
    # pprint(s1.obtenerDiccionarioParaRegistro())

    # test siniestroVida
    sVida = SiniestroVida()
    sVida.construirDatosSiniestro({
        'poliza': {
            'bancaseguro': 0,
            'ramo_subramo': 0,
            'noDePoliza': 0,
            'noDeCertificado': 0,
            'fechaDeContratacion': 'none',
            'fechaDeInicioDeVigencia': '',
            'fechaDeFinDeVigencia': '',
        },
        'generales': {
            'formaDePago': 0,
            'medioDePago': 0,
            'identificadorDelSiniestro': 0,
            'causa': '',
            'causaEspecial': 0,
            'entidadFederativa': 0,
            'municipio': 0,
            'fechaDeOcurrido': 0,
        },
        'coberturas': {
            'fechaDeReclamacion': '',
            'estatus': 0,
            'saAlcanzadaBeneficio1': 0,
            'saAlcanzadaBeneficio2': 0,
            'saAlcanzadaBeneficio3': 0,
            'saAlcanzadaBeneficio4': 0,
            'saAlcanzadaBeneficio5': 0,
            'saAlcanzadaBeneficio6': 0,
            'saAlcanzadaBeneficio7': 0,
        },
        'agente': {
            'saAlcanzadaBeneficio8': 0,
            'saAlcanzadaBeneficio9': 0,
            'nombre': '',
            'apellidoPaterno': '',
            'apellidoMaterno': '',
        },
    })

    sVida.construirDateosAsegurado({
        'generales': {
            'claveDelAgente': 0,
            'rfcDelAgente': '',
            'nombre': '',
            'apellidoPaterno': '',
            'apellidoMaterno': '',
            'fechaDeNacimiento': '',
            'genero': 0,
            'rfcAsegurado': '',
            'curp': '',
            'telefonoFIjoDelAsegurado': '',
            'telefonoMovilDelAsegurado': '',
        },
        'direccion': {
            'ocupacion': '',
            'estadoCivil': '',
            'calle': '',
            'noExterior': '',
            'noInterior': '',
            'codigoPostal': '',
            'entidadFederativa': 0,
            'municipio': 0,
            'colonia': 0,
        }
    })

    sVida.construirDatosBeneficiario({
        'telefonoFijo': 0,
        'fisicaCn1': {
            'telefonoMovil': 0,
            'tipoDePersona': 0,
        }
    })

    # sVida.construirDatosContratante({

    # })

    pprint(sVida.partes)

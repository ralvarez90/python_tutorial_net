from typing import Tuple
from django.conf import settings
from enum import Enum, auto
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

    def reportarImpedimento(
            self,
            url: str,
            ramo: int,
            claveDeCompania: int,
            fechaDeReporte: str,
            fechaDeImpedimento: str,
            claveCie10Oii: str,
            parametro1: str,
            parametro2: str,
            paisImpedimento: int,
            entidadFederativaImpedimento: int,
            municipioImpedimento: int,
            observaciones: str,
            nombre: str,
            apellidoPaterno: str,
            apellidoMaterno: str,
            fechaDeNacimiento: str,
            genero: int,
            rfc: str,
            curp: str,
            paisAsegurado: int,
            entidadFederativaAsegurado: int,
            municipioAsegurado: int,
    ) -> requests.Response:
        """Envía impedimento a registra a AMIS.

        Args:
                url (str): destino
                ramo (int): entero del catálogo AM0120
                claveDeCompania (int): clave de HIR
                fechaDeReporte (str): fecha de reporte del impedimento
                fechaDeImpedimento (str): fecha en que sucede el impedemente
                claveCie10Oii (str): string del catálogo CIE-0LL
                parametro1 (str): string descriptivo
                parametro2 (str): string descriptivo
                paisImpedimento (int): entero del catálogo AM0011
                entidadFederativaImpedimento (int): entero del catálogo AM0065
                municipioImpedimento (int): entero del catálogo AM0066
                observaciones (str): string descriptivo
                nombre (str): nombre del asegurado
                apellidoPaterno (str): apellido paterno del asegurado
                apellidoMaterno (str): apellido materno del asegurado
                fechaDeNacimiento (str): fecha de nacimiento
                genero (int): entero del catálogo AM0051
                rfc (str): rfc del asegurado
                curp (str): curp del asegurado
                paisAsegurado (int): entero del catálogo AM0011
                entidadFederativaAsegurado (int): entero del catálogo AM0065
                municipioAsegurado (int): entero del catálogo AM0066

        Returns:
                requests.Response: respuesta HTTP
        """

        # diccionario de datos
        datosAEnviar = {
            'impedimento': {
                'ramo': ramo,
                'claveDeCompania': claveDeCompania,
                'fechaDeReporte': fechaDeReporte,
                'fechaDeImpedimento': fechaDeImpedimento,
                'claveCie10Oii': claveCie10Oii,
                'parametro1': parametro1,
                'parametro2': parametro2,
                'pais': paisImpedimento,
                'entidadFederativa': entidadFederativaImpedimento,
                'municipio': municipioImpedimento,
                'observaciones': observaciones,
            },
            'asegurado': {
                'nombre': nombre,
                'apellidoPaterno': apellidoPaterno,
                'apellidoMaterno': apellidoMaterno,
                'fechaDeNacimiento': fechaDeNacimiento,
                'genero': genero,
                'rfc': rfc,
                'curp': curp,
                'pais': paisAsegurado,
                'entidadFederativa': entidadFederativaAsegurado,
                'municipio': municipioAsegurado,
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

    def registrarSiniestroAP():
        pass

    def registrarSiniestroVida():
        pass

    def existeRegistroSiniestroAP(self, noDePoliza: str, noCertificado: str, noSiniestro: str) -> bool:
        url = self.URL_SINIESTROS

        data = {
            'numeroDePoliza': noDePoliza,
            'noCertificado': noCertificado,
            'numeroDeSiniestro': noSiniestro,
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
        print(response.json(), response.status_code)
        print(
            f'poliza: {noDePoliza}, noCertificado: {noCertificado}, noSiniestro: {noSiniestro}')
        return False

    def existeRegistroSiniestroVida(self, noDePoliza: str, noCertificado: str, noSiniestro: str, nombre: str, apellidoPaterno: str, apellidoMaterno: str, fechaDeNacimiento: str, genero: int, rfc: str):
        url = self.URL_SINIESTROS

        data = {
            'noDePoliza': noDePoliza,
            'noDeCertificado': noCertificado,
            'numeroDeSiniestro': noSiniestro,
            'nombre': nombre,
            'apellidoPaterno': apellidoPaterno,
            'apellidoMaterno': apellidoMaterno,
            'fechaDeNacimiento': fechaDeNacimiento,
            'genero': genero,
            'rfc': rfc,
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

        if response.status_code == 200 and 'siniestro' in response.json().keys():
            return True

        # se ejecuta en casocontrarios
        print(response.json(), response.status_code)
        print(
            f'poliza: {noDePoliza}, noCertificado: {noCertificado}, noSiniestro: {noSiniestro}')
        return False


class SiniestroBuilder(ABC):

    def __init__(self) -> None:
        self.estaRegistradoEnAmis = False
        self.estaAnalizado = False

    def establecerEstatusRegistroManual(self, status: bool):
        self.estaRegistradoEnAmis = status

    @abstractmethod
    def establecerEstatusDeRegistroRemoto(self):
        raise NotImplementedError('Sin implementación')

    @abstractmethod
    def obtenerDiccionarioParaConsulta(self):
        raise NotImplementedError('Sin implemetanción')

    @abstractmethod
    def obtenerDiccionarioParaRegistro(self):
        raise NotImplementedError('Sin implemetanción')

    @abstractmethod
    def construirObjeto(self):
        raise NotImplementedError('Sin implemetanción')


class AP(SiniestroBuilder):

    def __init__(self) -> None:
        pass

    def establecerEstatusDeRegistroRemoto(self):
        pass

    def establecerDatosGenerales(
        self,
        noPoliza: str,
        numeroDeSiniestro: str,
        numeroDeReclamacion: str,
        ramoSubramo: int,
        tipoCoberturaOProducto: int,
        noCertificado: str,
        fechaAntiguiedadDelAfectado: str,
        nombreDelAfectado: str,
        apellidoPaternoDelAfectado: str,
        apellidoMaternoDelAfectado: str,
        fechaNacimientoDelAfectado: str,
        generoDelAfectado: int,
        rfcDelAfectado: str,
        rfcDelReceptor: str,
        cie10DelPadecimiento: str,
        cpt4Procedimiento: int,
        fechaIngresoHospitalatio

    ):
        self.nombreDelAfectado = nombreDelAfectado
        return self


class Vida(SiniestroBuilder):

    def __init__(self) -> None:
        pass

    def establecerEstatusDeRegistroRemoto(self):
        return

def reportarImpedimentosAMIS(parametros: dict) -> dict:
    """Envio de impedimentos a AMIS.
    """
    claveDeCompania = 218
    sheetPaises = pd.read_csv(settings.BASEDATOS_DIR / 'AMIS/AM0011')
    sheetEntidades = pd.read_csv(settings.BASEDATOS_DIR / 'AMIS/AM0065')
    sheetMunicipios = pd.read_csv(settings.BASEDATOS_DIR / 'AMIS/AM0066')

    infoImpedimientos = parametros.get('infoImpedimentos')
    url = parametros.get('url')
    configuracion = parametros.get('configuracion')

    contadorDeFallidos = 0
    contadorDeExitosos = 0
    impedimentosExitosos = parametros.get('impedimentosExitosos', None)
    if impedimentosExitosos is not None:
        contadorDeExitosos = len(impedimentosExitosos.keys())

    # diccionariops con exitosos y fallidos
    enviosFallidos = {}
    enviosExitosos = {}

    # diccionario de mensajes de error
    mensajesDeError = {
        400: 'Error en la petición',
        401: 'Token is not active',
        403: 'Forbidden',
        404: 'No encontrado',
        408: 'Tiempo de espera excedido',
        500: 'Por favor contacte a su administrador de TI'
    }

    # recorre diccionario de impedimentos
    for impedimento in infoImpedimientos.values():
        ramo = int(getValuePath(
            configuracion['ramo'], impedimento).split(' ')[0])
        fechaDeReporte = getValuePath(
            configuracion['fechaDeReporte'], impedimento).replace('-', '/')
        fechaDeImpedimento = getValuePath(
            configuracion['fechaDeImpedimento'], impedimento).replace('-', '/')
        claveCie10Oii = getValuePath(
            configuracion['claveCie10Oii'], impedimento).split(' ')[0]
        parametro1 = getValuePath(configuracion['parametro1'], impedimento)
        parametro2 = getValuePath(configuracion['parametro2'], impedimento)

        paisImpedimento = getValuePath(
            configuracion['paisImpedimento'], impedimento)
        for id, valor, _ in sheetPaises.values:
            if quitarCaracteresEspeciales(valor.upper()) == quitarCaracteresEspeciales(paisImpedimento.upper()):
                paisImpedimento = int(id)
                break

        entidadImpedimento = getValuePath(
            configuracion['entidadFederativaImpedimento'], impedimento)
        for id, valor, *_ in sheetEntidades.values:
            if quitarCaracteresEspeciales(valor.upper()) == quitarCaracteresEspeciales(entidadImpedimento.upper()):
                entidadImpedimento = int(id)
                break

        municipioImpedimento = getValuePath(
            configuracion['municipioImpedimento'], impedimento)
        for id, valor, *_ in sheetMunicipios.values:
            if quitarCaracteresEspeciales(valor.upper()) == quitarCaracteresEspeciales(municipioImpedimento.upper()):
                municipioImpedimento = int(id)
                break

        observaciones = getValuePath(
            configuracion['observaciones'], impedimento, None)
        paragraphText = ''
        if observaciones is not None:
            observaciones = json.loads(observaciones)
            for block in observaciones["blocks"]:
                textBlock = block["text"]
                paragraphText += textBlock
        observaciones = paragraphText

        nombre = getValuePath(configuracion['nombre'], impedimento)
        apellidoPaterno = getValuePath(
            configuracion['apellidoPaterno'], impedimento)
        apellidoMaterno = getValuePath(
            configuracion['apellidoMaterno'], impedimento)
        fechaDeNacimiento = getValuePath(
            configuracion['fechaDeNacimiento'], impedimento).replace('-', '/')
        genero = int(getValuePath(
            configuracion['genero'], impedimento).split(' ')[0])
        rfc = getValuePath(configuracion['rfc'], impedimento)
        curp = getValuePath(configuracion['curp'], impedimento)

        paisAsegurado = getValuePath(
            configuracion['paisAsegurado'], impedimento)
        for id, valor, _ in sheetPaises.values:
            if quitarCaracteresEspeciales(valor.upper()) == quitarCaracteresEspeciales(paisAsegurado.upper()):
                paisAsegurado = int(id)
                break

        entidadAsegurado = getValuePath(
            configuracion['entidadFederativaAsegurado'], impedimento)
        for id, valor, *_ in sheetEntidades.values:
            if quitarCaracteresEspeciales(entidadAsegurado.upper()) == quitarCaracteresEspeciales(valor.upper()):
                entidadAsegurado = int(id)
                break

        municipioAsegurado = getValuePath(
            configuracion['municipioAsegurado'], impedimento)
        for id, valor, *_ in sheetMunicipios.values:
            if quitarCaracteresEspeciales(municipioAsegurado.upper()) == quitarCaracteresEspeciales(valor.upper()):
                municipioAsegurado = int(id)
                break

        # instancia de clase AMIS
        reporteAMIS = amisAPI.AMIS()

        data = {
            'ramo': ramo,
            'claveDeCompania': claveDeCompania,
            'fechaDeReporte': fechaDeReporte,
            'fechaDeImpedimento': fechaDeImpedimento,
            'claveCie10Oii': claveCie10Oii,
            'parametro1': parametro1,
            'parametro2': parametro2,
            'paisImpedimento': paisImpedimento,
            'entidadFederativaImpedimento': entidadImpedimento,
            'municipioImpedimento': municipioImpedimento,
            'observaciones': observaciones,
            'nombre': nombre,
            'apellidoPaterno': apellidoPaterno,
            'apellidoMaterno': apellidoMaterno,
            'fechaDeNacimiento': fechaDeNacimiento,
            'genero': genero,
            'rfc': rfc,
            'curp': curp,
            'paisAsegurado': paisAsegurado,
            'entidadFederativaAsegurado': entidadAsegurado,
            'municipioAsegurado': municipioAsegurado,
        }

        codigoRespuestaTemporal = None
        try:
            response = reporteAMIS.reportarImpedimento(url, data)

            # copia código para tener alcance al bloque de excepción
            codigoRespuestaTemporal = response.status_code

            if response.status_code not in [200, 201]:
                contadorDeFallidos += 1
                impedimento['datosImpedimento']['mensajeError'] = mensajesDeError.get(
                    codigoRespuestaTemporal, 'Error')
                enviosFallidos[f'Impedimento{contadorDeFallidos}'] = impedimento
            else:
                contadorDeExitosos += 1
                enviosExitosos.update(
                    {f'Impedimento{contadorDeExitosos}': impedimento})
        except Exception:
            contadorDeFallidos += 1
            impedimento['datosImpedimento']['mensajeError'] = mensajesDeError.get(
                codigoRespuestaTemporal, 'Error')
            enviosFallidos[f'Impedimento{contadorDeFallidos}'] = impedimento

    if impedimentosExitosos is not None:
        enviosExitosos = updateDatosDelete(
            impedimentosExitosos, enviosExitosos)

    return {
        'datosImpedimentosErrores': enviosFallidos,
        'datosImpedimentosExitosos': enviosExitosos,
    }


def registrarSiniestroAMIS(parametros: dict) -> dict:
    """Envia siniestros a amis para su registro. Envía los siniestros
    ocurridos en el rango de tiempo establecido entre las fechas.

    Las fechas deben estár el el formato dd/mm/aaaa para poder realizar
    la respectiva consulta sql.
    """
    sheetMunicipios = pd.read_csv(settings.BASEDATOS_DIR / 'AMIS/AM0066')
    hilosAUsar = 8
    totalizarMontoBeneficiario = True

    import time

    inicio = time.time()

    def __mostrarDiccionario(d: dict, indent=0):
        for k, v in d.items():
            if isinstance(v, dict):
                print(f'{" "*indent}{k}:')
                __mostrarDiccionario(v, indent+3)
            else:
                print(f'{" "*indent}{k}: {v}')

    class _AP:
        def __init__(self):
            # general
            self.noPoliza: str = None
            self.numeroDeSiniestro: str = None
            self.numeroDeReclamacion: str = None
            self.ramoSubramo: int = None
            self.tipoCoberturaOProducto: int = None
            self.noCertificado: str = None
            self.fechaAntiguedadDelAfectado: str = None
            self.nombreDelAfectado: str = None
            self.apellidoPaternoDelAfectado: str = None
            self.apellidoMaternoDelAfectado: str = None
            self.fechaNacimientoDelAfectado: str = None
            self.generoDelAfectado: int = None
            self.rfcDelAfectado: str = None
            self.rfcReceptor: str = None
            self.cie10DelPadecimiento: str = None
            self.cpt4Procedimiento: int = None
            self.fechaIngresoHospitalarioDelAfectado: str = None
            self.fechaEgresoHospitalarioDelAfectado: str = None
            self.numeroDiasEstanciaHospitalaria: int = None
            self.fechaReclamacion: str = None

            # titular
            self.cuentaBancariaClabe: int = None
            self.banco: int = None
            self.nombreTitularCuentaClabe: str = None
            self.apePatTitularCuentaClabe: str = None
            self.apeMatTitularCuentaClabe: str = None
            self.moneda: int = 1
            self.estatusFactura: int = None
            self.montoAseguradoPagado: int = None

            # proveedor
            self.tipoDeProveedor: int = 90
            self.tipoDePago: int = 3
            self.fechaPrimerGastoDelSiniestro: str = None
            self.montoComprobanteOSumaAsegurada: float = None
            self.fechaComprobante: str = None

            self.nombreProveedor: str = None
            self.apellidoPaternoProveedor: str = None
            self.apellidoMaternoProveedor: str = None
            self.rfcDelProveedor: str = None
            self.entidadDelProveedor: int = None
            self.numeroFolioFiscalComprobante: str = None
            self.calleDelProveedor: str = None
            self.numeroDomicilioProveedor: str = None
            self.coloniaProveedor: str = None
            self.alcaldiaMunicipioProveedor: str = None
            self.codigoPostalProveedor: str = None
            self.cedulaProfesional: str = None

            # campo de estado
            self.estaRegistrado: bool = False
            self.analizado: bool = False

        def getDictForValidate(self):
            """Obtiene diccionario con datos para poder realizar validaciones
            de existencia de siniestro registrado ante AMIS
            """
            return {
                'numeroDePoliza': self.noPoliza,
                'noCertificado': self.noCertificado,
                'numeroDeSiniestro': self.numeroDeSiniestro,
            }

        def getDictToSend(self):
            return {
                "General": {
                    'noPoliza': self.noPoliza,
                    'numeroDeSiniestro': self.numeroDeSiniestro,
                    'numeroDeReclamacion': self.numeroDeReclamacion,
                    'ramoSubramo': self.ramoSubramo,
                    'tipoCoberturaOProducto': self.tipoCoberturaOProducto,
                    'noCertificado': self.noCertificado,
                    'fechaAntiguedadDelAfectado': self.fechaAntiguedadDelAfectado,
                    'nombreDelAfectado': self.nombreDelAfectado,
                    'apellidoPaternoDelAfectado': self.apellidoPaternoDelAfectado,
                    'apellidoMaternoDelAfectado': self.apellidoMaternoDelAfectado,
                    'fechaNacimientoDelAfectado': self.fechaNacimientoDelAfectado,
                    'generoDelAfectado': self.generoDelAfectado,
                    'rfcDelAfectado': self.rfcDelAfectado,
                    'rfcReceptor': self.rfcReceptor,
                    'cie10DelPadecimiento': self.cie10DelPadecimiento,
                    'cpt4Procedimiento': self.cpt4Procedimiento,
                    'fechaIngresoHospitalarioDelAfectado': self.fechaIngresoHospitalarioDelAfectado,
                    'fechaEgresoHospitalarioDelAfectado': self.fechaEgresoHospitalarioDelAfectado,
                    'numeroDiasEstanciaHospitalaria': self.numeroDiasEstanciaHospitalaria,
                    'fechaReclamacion': self.fechaReclamacion,
                },
                "Titular": {
                    'cuentaBancariaClabe': self.cuentaBancariaClabe,
                    'banco': self.banco,
                    'nombreTitularCuentaClabe': self.nombreTitularCuentaClabe,
                    'apePatTitularCuentaClabe': self.apePatTitularCuentaClabe,
                    'apeMatTitularCuentaClabe': self.apeMatTitularCuentaClabe,
                    'moneda': self.moneda,
                    'estatusFactura': self.estatusFactura,
                    'montoAseguradoPagado': self.montoAseguradoPagado,
                },
                "Proveedor": {
                    'nombreProveedor': self.nombreProveedor,
                    'apellidoPaternoProveedor': self.apellidoPaternoProveedor,
                    'apellidoMaternoProveedor': self.apellidoMaternoProveedor,
                    'rfcDelProveedor': self.rfcDelProveedor,
                    'entidadDelProveedor': self.entidadDelProveedor,
                    'tipoDeProveedor': self.tipoDeProveedor,
                    'tipoDePago': self.tipoDePago,
                    'fechaPrimerGastoDelSiniestro': self.fechaPrimerGastoDelSiniestro,
                    'fechaComprobante': self.fechaComprobante,
                    'numeroFolioFiscalComprobante': self.numeroFolioFiscalComprobante,
                    'montoComprobanteOSumaAsegurada': self.montoComprobanteOSumaAsegurada,
                    'calleDelProveedor': self.calleDelProveedor,
                    'numeroDomicilioProveedor': self.numeroDomicilioProveedor,
                    'coloniaProveedor': self.coloniaProveedor,
                    'alcaldiaMunicipioProveedor': self.alcaldiaMunicipioProveedor,
                    'codigoPostalProveedor': self.codigoPostalProveedor,
                    'cedulaProfesional': self.cedulaProfesional,
                }
            }

        def establecerEstatusDeRegistroRemoto(self):
            """Establece si el estado de dicha instancia está registrado en AMIS
            """
            self.estaRegistrado = amisapi.existeRegistroSiniestroAP(
                self.noPoliza, self.noCertificado, self.numeroDeSiniestro)
            self.analizado = True

        def __str__(self) -> str:
            return str(self.getDictForValidate()) + f', registrado: {self.estaRegistrado}, analizado: {self.analizado}'

    class _Vida:
        def __init__(self):
            # siniestro -> poliza
            self.bancaSeguro: int
            self.ramoSubramo: int
            self.noDePoliza: str
            self.noDeCertificado: str = None
            self.fechaDeContratacion: str
            self.fechaDeInicioDeVigencia: str
            self.fechaDeFinDeVigencia: str

            # siniestro -> generales
            self.formaDePago: int = None
            self.medioDePago: int = None
            self.identificadorDelSiniestro: int
            self.causa: str
            self.causaEspecial: str = None
            self.entidadFederativa: int
            self.municipio: int
            self.fechaDeOcurrido: str

            # siniestro -> coberturas
            self.fechaDeReclamacion: str
            self.estatus: int
            self.saAlcanzadaBeneficio1: int = 0
            self.saAlcanzadaBeneficio2: int = None
            self.saAlcanzadaBeneficio3: int = None
            self.saAlcanzadaBeneficio4: int = None
            self.saAlcanzadaBeneficio5: int = None
            self.saAlcanzadaBeneficio6: int = None
            self.saAlcanzadaBeneficio7: int = None

            # siniestro -> agente
            self.saAlcanzadaBeneficio8: int = None
            self.saAlcanzadaBeneficio9: int = None
            self.nombreAgente: str = None
            self.apellidoPaternoAgente: str = None
            self.apellidoMaternoAgente: str = None

            # asegurado -> generales
            self.claveDelAgente: str = None
            self.rfcDelAgente: str = None
            self.nombreAsegurado: str
            self.apellidoPaternoAsegurado: str
            self.apellidoMaternoAsegurado: str = None
            self.fechaDeNacimientoAsegurado: str
            self.generoAsegurado: int
            self.rfcAsegurado: str
            self.curpAsegurado: str = None
            self.telefonoFijoDelAsegurado: str = None
            self.telefonoMovilDelAsegurado: str = None

            # asegurado -> direccion
            self.ocupacionDelAsegurado: int = 30
            self.estadoCivilDelAsegurado: int = None
            self.calleDelAsegurado: str
            self.noExteriorDelAsegurado: str
            self.noInteriorDelAsegurado: str = None
            self.codigoPostalDelAsegurado: str
            self.entidadFederativaDelAsegurado: int
            self.municipioDelAsegurado: int = None
            self.coloniaDelAsegurado: int = None

            # beneficiario
            self.telefonoFijoDelBeneficiario: str = None

            # beneficiario -> fisicaCn1
            self.telefonoMovilFisicaCnlDelBeneficiario: str = None
            self.tipoDePersonaFisicaCnlDelBeneficiario: int
            self.nombreFisicaCnlDelBeneficiario: str = None
            self.apellidoPaternoFisicaCnlDelBeneficiario: str = None
            self.apellidMaternoFisicaCnlDelBeneficiario: str = None
            self.fechaDeNacimientoBeneficiarioFisicaCnl = None
            self.generoFisicaCnlDelBeneficiario: int = None
            self.rfcFisicaCnlDelBeneficiario: str = None
            self.curpFisicaCnlDelBeneficiario: str = None
            self.ocupacionFisicaCnlDelBeneficiario: int = None
            self.estadoCivilFisicaCnlDelBeneficiario: int = None
            self.parentescoFisicaCnlDelBeneficiario: int = None

            # beneficiario -> moralCn1
            self.razonSocialDelBeneficiario: str = None
            self.nombreComercialDelBeneficiario: str = None
            self.rfcMoralCn1DelBeneficiario: str = None

            # beneficiario -> direccion
            self.sectorGiroDelBeneficiario: int = None
            self.calleDelBeneficiario: str
            self.noExteriorDelBeneficiario: str
            self.noInteriorDelBeneficiario: str = None
            self.codigoPostalDelBeneficiario: str
            self.entidadFederativaDelBeneficiario: int
            self.municipioDelBenficiario: int = None
            self.coloniaDelBeneficiario: int = None

            # contratante
            self.telefonoFijoDelContratante: int = None

            # contratante -> fisicaCnl
            self.telefonoMovilFisicaCnlDelContratante: int = None
            self.tipoDePersonaFisicaCnlDelContratante: int
            self.nombreFisicaCnlDelContratante: str = None
            self.apellidoPaternoFisicaCnlDelContratante: str = None
            self.apellidoMaternoFisicaCnlDelContratante: str = None
            self.generoFisicaCnlDelContratante: int = None
            self.rfcFisicaCnlDelContratante: str = None
            self.curpFisicaCnlDelContratante: str = None
            self.ocupacionFisicaCnlDelContratante: int = None
            self.estadoCivilFisicaCnlDelContratante: int = None

            # contratante -> moralCnl
            self.razonSocialDelContratante: str
            self.nombreComercialDelContratante: str
            self.rfcMoralCn1DelContratante: str

            # contratante -> direccion
            self.sectorGiroDelContratante: int = None
            self.calleDelContratante: str
            self.noExteriorDelContratante: str
            self.noInteriorDelContratante: str = None
            self.codigoPostalDeContratante: str
            self.entidadFederativaDelContratante: int = None
            self.municipioDelContratante: int = None
            self.coloniaDelContratante: int = None
            self.telefonoFijoDireccionDelContratante: int = None
            self.telefonoMovilDireccionDelContratante: int

            self.tipoDeMovimiento: int
            self.noDeSiniestro: str

            self.estaRegistrado = False
            self.analizado = False

        def getDictToValidate(self):
            return {
                'noDePoliza': self.noDePoliza,
                'noDeCertificado': self.noDeCertificado,
                'numeroDeSiniestro': self.noDeSiniestro,
                'nombre': self.nombreAsegurado,
                'apellidoPaterno': self.apellidoPaternoAsegurado,
                'apellidoMaterno': self.apellidoMaternoAsegurado,
                'fechaDeNacimiento': self.fechaDeNacimientoAsegurado,
                'genero': self.generoAsegurado,
                'rfc': self.rfcAsegurado,
            }

        def getDictToSend(self):
            return {

            }

        def setEstatusRegistradoDeFormaRemota(self):
            """Establece si el estado de dicha instancia está registrado en AMIS
            """
            self.estaRegistrado = amisapi.existeRegistroSiniestroVida(self.noDePoliza, self.noDeCertificado, self.noDeSiniestro, self.nombreAsegurado,
                                                                      self.apellidoPaternoAsegurado, self.apellidoMaternoAsegurado, self.fechaDeNacimientoAsegurado, self.generoAsegurado, self.rfcAsegurado)
            self.analizado = True

        def __hash__(self) -> int:
            return hash(self.noDeSiniestro)

        def __eq__(self, __value: object) -> bool:
            return isinstance(__value, _Vida) and self.noDeCertificado == __value.noDeCertificado

    # todo cambiar a corchetes
    # fecha final
    fechaSiniestroFinal = parametros['fechaSiniestroFinal']
    fechaSiniestroFinal = fechaSiniestroFinal.split('-')
    fechaSiniestroFinal = f'{fechaSiniestroFinal[2]}/{fechaSiniestroFinal[1]}/{fechaSiniestroFinal[0]}'

    # fecha inicial
    fechaSiniestroInicial = parametros['fechaSiniestroInicial']
    fechaSiniestroInicial = fechaSiniestroInicial.split('-')
    fechaSiniestroInicial = f'{fechaSiniestroInicial[2]}/{fechaSiniestroInicial[1]}/{fechaSiniestroInicial[0]}'

    # tipo de siniestro: 'Vida' o 'Accidente Personal'
    tipoSiniestro = parametros['tipoSiniestro']

    # resultados de consultas
    if tipoSiniestro == 'Accidente Personal':
        results = midasAPI.ConexionMidas('DB_1').obtenerListaSiniestrosAP(
            fechaSiniestroInicial, fechaSiniestroFinal)
    elif tipoSiniestro == 'Vida':
        results = midasAPI.ConexionMidas('DB_1').obtenerListaSiniestrosVida(
            fechaSiniestroInicial, fechaSiniestroFinal)

    # lista de siniestros a registrar
    siniestrosAEnviar: list[_AP | _Vida] = []

    # instancia de api
    amisapi = amisAPI.AMIS()

    def obtenerSumaTotalSiniestrosVida(noSiniestro: str, listaSiniestro: list[_Vida]) -> float:
        sinietros = [
            s for s in listaSiniestro if s.noDeSiniestro == noSiniestro]

    # iteramos resultados y los agregamos a la losta
    if tipoSiniestro == 'Accidente Personal':
        for row in results:
            siniestro = _AP()
            siniestro.noPoliza = str(row[2])
            siniestro.numeroDeSiniestro = str(row[8])
            siniestro.numeroDeReclamacion = str(row[7])
            siniestro.ramoSubramo = int(row[1])
            siniestro.tipoCoberturaOProducto = int(row[35])
            siniestro.noCertificado = str(row[3])
            siniestro.nombreDelAfectado = str(row[16])
            siniestro.apellidoPaternoDelAfectado = str(row[17])
            siniestro.apellidoMaternoDelAfectado = str(row[36])
            siniestro.fechaNacimientoDelAfectado = (
                (str(row[18])).split(' ')[0]).replace('-', '/')
            siniestro.generoDelAfectado = int(row[19])
            siniestro.rfcDelAfectado = str(row[20])
            siniestro.cie10DelPadecimiento = str(row[9])
            siniestro.fechaPrimerGastoDelSiniestro = (
                (str(row[13])).split(' ')[0]).replace('-', '/')
            siniestro.montoComprobanteOSumaAsegurada = float(row[15])
            siniestro.fechaComprobante = (
                (str(row[13])).split(' ')[0]).replace('-', '/')
            siniestrosAEnviar.append(siniestro)

        
    
    elif tipoSiniestro == 'Vida':
        numeroDeSiniestro = 0
        for row in results:
            siniestro = _Vida()

            # poliza
            siniestro.bancaSeguro = int(row[0])
            siniestro.ramoSubramo = int(row[1])
            siniestro.noDePoliza = str(row[2])
            siniestro.fechaDeContratacion = (
                (str(row[3])).split(' ')[0]).replace('-', '/')
            siniestro.fechaDeInicioDeVigencia = (
                (str(row[4])).split(' ')[0]).replace('-', '/')
            siniestro.fechaDeFinDeVigencia = (
                (str(row[5])).split(' ')[0]).replace('-', '/')
            siniestro.noDeCertificado = str(row[37])

            # generales
            siniestro.identificadorDelSiniestro = str(row[7])
            siniestro.causa = str(row[8])
            siniestro.entidadFederativa = int(row[9])
            siniestro.fechaDeOcurrido = str(row[11])
            for id, valor, *_ in sheetMunicipios.values:
                if quitarCaracteresEspeciales(valor.upper()) == quitarCaracteresEspeciales(str(row[10])):
                    siniestro.municipio = int(id)
                    break

            # coberturas
            siniestro.fechaDeReclamacion = str(row[12])
            siniestro.estatus = int(row[13])

            # asegurado
            siniestro.nombreAsegurado = str(row[15])
            siniestro.apellidoPaternoAsegurado = str(row[16])
            siniestro.apellidoMaternoAsegurado = str(row[17])
            siniestro.fechaDeNacimientoAsegurado = (
                (str(row[18])).split(' ')[0]).replace('-', '/')
            siniestro.generoAsegurado = int(row[19])
            siniestro.rfcAsegurado = str(row[20])
            siniestro.calleDelAsegurado = str(row[22])
            siniestro.noExteriorDelAsegurado = str(row[23])
            siniestro.codigoPostalDelAsegurado = str(row[24])
            siniestro.entidadFederativaDelAsegurado = CodigoPostal.objects.obtenerClaveEstado(
                str(row[24]))

            # beneficiario
            siniestro.tipoDePersonaFisicaCnlDelBeneficiario = int(row[26])
            siniestro.calleDelBeneficiario = str(row[32])
            siniestro.noExteriorDelBeneficiario = str(row[33])
            siniestro.codigoPostalDelBeneficiario = str(row[34])
            siniestro.entidadFederativaDelBeneficiario = CodigoPostal.objects.obtenerClaveEstado(
                str(row[34]))

            # contratante
            siniestro.tipoDePersonaFisicaCnlDelContratante = int(row[31])
            siniestro.calleDelContratante = str(row[32])
            siniestro.noExteriorDelContratante = str(row[33])
            siniestro.codigoPostalDeContratante = str(row[34])

            siniestro.tipoDeMovimiento = int(row[35])

            # suma asegurada, se hace posteriormente
            # siniestro.saAlcanzadaBeneficio1 = float(row[14])
            # if(totalizarMontoBeneficiario and len(siniestrosAEnviar) != 0):
            # 	totalSiniestros = len(totalSiniestros)
            # 	if siniestro.noDeSiniestro == siniestrosAEnviar[totalSiniestros]

            siniestro.noDeSiniestro = str(row[7])
            siniestrosAEnviar.append(siniestro)

    print(f'Total de siniestros: {len(siniestrosAEnviar)}')

    # lista de sinistros y ciantos aparecen en estas

    # cambiamos estado de siniestros que no han sido registrados
    # eliminamos siniestros que no han sido registrados.
    # todo hacerlo opcional el numero de hilos
    with ThreadPoolExecutor(max_workers=16) as executor:
        futuros = []
        for s in siniestrosAEnviar:
            futuro = executor.submit(s.establecerEstatusDeRegistroRemoto)
            futuros.append(futuro)

        # espera que se completen
        [f.result() for f in futuros]

    # # imprimimos siniestros a enviar
    print('-'*50)
    siniestrosAEnviar = [
        s for s in siniestrosAEnviar if not s.estaRegistrado and s.analizado]
    fin = time.time()

    print(f'Total de siniestros a enviar: {len(siniestrosAEnviar)}')
    print(f'\nTiempo: {fin-inicio} segundos')
    return {}

    return {}

    return {'siniestrosExcel': {
            "valid": True,
            "vigencia": None,
            "tipo": "Herón",
                    "ruta": "SNS12070/2-1-2.0-2/9/RelacióndePagos-SNS12070.xlsx",
                    "nombre": "Relación de Pagos Beneficiarios.xlsx",
                    "date": "2024/02/12, 11:32 h."
            }}

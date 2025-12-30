from capaDatos.dAsistencia import DAsistenciaDocente

class LDocente:
    def __init__(self):
        self.dAsistenciaDocente = DAsistenciaDocente()

    #  ASISTENCIA 
    def mostrarReporte(self):
        return self.dAsistenciaDocente.mostrarReporte()

    def buscarPorDni(self, dni):
        return self.dAsistenciaDocente.buscarPorDni(dni)

    def estadisticasPorDni(self, dni):
        return self.dAsistenciaDocente.estadisticasPorDni(dni)

    def insertarAsistencia(self, asistencia_docente):
        return self.dAsistenciaDocente.insertarAsistencia(asistencia_docente)

    # DOCENTE 
    def registrarPersonaDocente(self, persona, docente):
        self.dAsistenciaDocente.insertarPersona(persona)
        self.dAsistenciaDocente.insertarDocente(docente)

    def eliminarDocente(self, dni):
        return self.dAsistenciaDocente.eliminarDocenteTotal(dni)



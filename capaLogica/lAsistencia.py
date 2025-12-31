# # from capaDatos.dAsistencia import DAsistenciaDocente 

# # class LDocente:
# #     def __init__(self):
# #         self.dAsistenciaDocente = DAsistenciaDocente()

# #     def mostrarReporte(self):
# #         return self.dAsistenciaDocente.mostrarReporte()
    
# #     def  insertarAsistencia(self,asistencia_Docente:dict):
# #         return self.dAsistenciaDocente.insertarAsistencia(asistencia_Docente)
# # from capaDatos.dAsistencia import DAsistenciaDocente

# # class LDocente:
# #     def __init__(self):
# #         self.dAsistenciaDocente = DAsistenciaDocente()

# #     def mostrarReporte(self):
# #         return self.dAsistenciaDocente.mostrarReporte()
    
# #     def insertarAsistencia(self, asistencia_docente: dict):
# #         # SE GUARDA EXACTAMENTE LOS DATOS QUE VIENEN DE LA CAPA PRESENTACIÓN
# #         return self.dAsistenciaDocente.insertarAsistencia(asistencia_docente)

# # from capaDatos.dAsistencia import DAsistenciaDocente 

# # class LDocente:
# #     def __init__(self):
# #         self.dAsistenciaDocente = DAsistenciaDocente()

# #     def mostrarReporte(self):
# #         return self.dAsistenciaDocente.mostrarReporte()

# #     def buscarPorDni(self, dni):
# #         return self.dAsistenciaDocente.buscarPorDni(dni)

# #     def estadisticasPorDni(self, dni):
# #         return self.dAsistenciaDocente.estadisticasPorDni(dni)

# #     def insertarAsistencia(self, asistencia_docente: dict):
# #         return self.dAsistenciaDocente.insertarAsistencia(asistencia_docente)



# # nuevo :3

# from capaDatos.dAsistencia import DAsistenciaDocente

# class LDocente:
#     def __init__(self):
#         self.dAsistenciaDocente = DAsistenciaDocente()

#     #  ASISTENCIA 
#     def mostrarReporte(self):
#         return self.dAsistenciaDocente.mostrarReporte()

#     def buscarPorDni(self, dni):
#         return self.dAsistenciaDocente.buscarPorDni(dni)

#     def estadisticasPorDni(self, dni):
#         return self.dAsistenciaDocente.estadisticasPorDni(dni)

#     def insertarAsistencia(self, asistencia_docente):
#         return self.dAsistenciaDocente.insertarAsistencia(asistencia_docente)

#     # DOCENTE 
#     def registrarPersonaDocente(self, persona, docente):
#         self.dAsistenciaDocente.insertarPersona(persona)
#         self.dAsistenciaDocente.insertarDocente(docente)

#     def eliminarDocente(self, dni):
#         return self.dAsistenciaDocente.eliminarDocenteTotal(dni)

from capaDatos.dAsistencia import DAsistencia

class LAsistencia:
    def __init__(self):
        self.data = DAsistencia()

    def registrar_persona(self, persona):
        return self.data.insertar_persona(persona)

    def listar_personas(self):
        return self.data.listar_personas()

    def registrar_asistencia(self, dni, rol, estado="FALTA", comentario=""):
        return self.data.registrar_asistencia(dni, rol, estado, comentario)

    def registrar_salida(self, dni, rol):
        return self.data.registrar_salida(dni, rol)

    def listar_asistencias(self, rol):
        return self.data.listar_asistencias(rol)

    def editar_asistencia(self, dni, fecha, datos, rol):
        return self.data.editar_asistencia(dni, fecha, datos, rol)

    def eliminar_asistencia(self, dni, fecha, rol):
        return self.data.eliminar_asistencia(dni, fecha, rol)

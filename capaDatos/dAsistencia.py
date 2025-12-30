
# from conexion import ConexionDB

# class DAsistenciaDocente:
#     def __init__(self):
#         self.__db = ConexionDB().conexionSupabase()
#         self.__nombreTabla = "asistencia_docente"

#     def __ejecutarConsultas(self, consulta, tipoConsulta = None):
#         try:
#             if tipoConsulta == "select":
#                 return consulta.execute().data
#             else: 
#                 return consulta.execute()
#         except Exception as e:
#             return f"error: {e}"

#     def mostrarReporte(self):
#         consulta = self.__db.table(self.__nombreTabla).select("*")
#         return self.__ejecutarConsultas(consulta,"select")
    
#     def insertarAsistencia(self,asistencia_docente:dict):
#         consulta = self.__db.table(self.__nombreTabla).insert(asistencia_docente)
#         return self.__ejecutarConsultas(consulta)

# from conexion import ConexionDB

# class DAsistenciaDocente:
#     def __init__(self):
#         self.__db = ConexionDB().conexionSupabase()
#         self.__nombreTabla = "asistencia_docente"

#     def __ejecutarConsultas(self, consulta, tipoConsulta=None):
#         try:
#             resultado = consulta.execute()
#             # IMPORTANTE: imprimir para depuración
#             print("SUPABASE RESPUESTA:", resultado)
#             return resultado.data if tipoConsulta == "select" else resultado
#         except Exception as e:
#             print(f"ERROR EN SUPABASE: {e}")
#             return None

#     def mostrarReporte(self):
#         consulta = self.__db.table(self.__nombreTabla).select("*")
#         return self.__ejecutarConsultas(consulta, "select")
    
#     def insertarAsistencia(self, asistencia_docente: dict):
#         consulta = self.__db.table(self.__nombreTabla).insert(asistencia_docente)
#         return self.__ejecutarConsultas(consulta)
# from conexion import ConexionDB

# class DAsistenciaDocente:
#     def __init__(self):
#         self.__db = ConexionDB().conexionSupabase()
#         self.__nombreTabla = "asistencia_docente"

#     def __ejecutarConsultas(self, consulta, tipoConsulta=None):
#         try:
#             if tipoConsulta == "select":
#                 return consulta.execute().data
#             else:
#                 return consulta.execute()
#         except Exception as e:
#             return {"error": str(e)}

#     def mostrarReporte(self):
#         consulta = self.__db.table(self.__nombreTabla).select("*")
#         return self.__ejecutarConsultas(consulta, "select")

#     def buscarPorDni(self, dni: str):
#         consulta = (
#             self.__db.table(self.__nombreTabla)
#             .select("*")
#             .eq("dni", dni)
#         )
#         return self.__ejecutarConsultas(consulta, "select")

#     def estadisticasPorDni(self, dni: str):
#         consulta = (
#             self.__db.table(self.__nombreTabla)
#             .select("estado")
#             .eq("dni", dni)
#         )
#         return self.__ejecutarConsultas(consulta, "select")

#     def insertarAsistencia(self, asistencia_docente: dict):
#         consulta = self.__db.table(self.__nombreTabla).insert(asistencia_docente)
#         return self.__ejecutarConsultas(consulta)


# nuevo

from conexion import ConexionDB

class DAsistenciaDocente:
    def __init__(self):
        self.__db = ConexionDB().conexionSupabase()

    def __ejecutar(self, consulta, tipo=None):
        try:
            if tipo == "select":
                return consulta.execute().data
            return consulta.execute()
        except Exception as e:
            return {"error": str(e)}

    # ASISTENCIA 
    def mostrarReporte(self):
        return self.__ejecutar(
            self.__db.table("asistencia_docente").select("*"),
            "select"
        )

    def buscarPorDni(self, dni):
        return self.__ejecutar(
            self.__db.table("asistencia_docente")
            .select("*")
            .eq("dni", dni),
            "select"
        )

    def estadisticasPorDni(self, dni):
        return self.__ejecutar(
            self.__db.table("asistencia_docente")
            .select("estado")
            .eq("dni", dni),
            "select"
        )

    def insertarAsistencia(self, data):
        return self.__ejecutar(
            self.__db.table("asistencia_docente").insert(data)
        )

    #  PERSONA / DOCENTE 
    def insertarPersona(self, persona):
        print(persona)
        return self.__ejecutar(
            self.__db.table("persona").insert(persona)
        )
    
    def insertarDocente(self, docente):
        return self.__ejecutar(
            self.__db.table("docente").insert(docente)
        )


    # ELIMINAR DOCENTE 

    def eliminarDocenteTotal(self, dni):
        
        cursos = self.__ejecutar(
            self.__db.table("docente_curso")
            .select("id_docente_curso")
            .eq("dni_docente", dni),
            "select"
        )

        if cursos:
            for c in cursos:
                # Eliminar notas 
                self.__ejecutar(
                    self.__db.table("nota")
                    .delete()
                    .eq("id_docente_curso", c["id_docente_curso"])
                )

        #  Eliminar asistencia docente
        self.__ejecutar(
            self.__db.table("asistencia_docente")
            .delete()
            .eq("dni", dni)
        )

        # 4️⃣ Eliminar docente_curso
        self.__ejecutar(
            self.__db.table("docente_curso")
            .delete()
            .eq("dni_docente", dni)
        )

        # 5️⃣ Eliminar docente
        self.__ejecutar(
            self.__db.table("docente")
            .delete()
            .eq("dni", dni)
        )

        # 6️⃣ Eliminar persona
        return self.__ejecutar(
            self.__db.table("persona")
            .delete()
            .eq("dni", dni)
        )

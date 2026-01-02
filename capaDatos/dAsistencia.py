

# from conexion import 
# # from conexion import ConexionDB


# # class DAsistenciaDocente:
# #     def __init__(self):
# #         self.__db = ConexionDB().conexionSupabase()
# #         self.__nombreTabla = "asistencia_docente"

# #     def __ejecutarConsultas(self, consulta, tipoConsulta = None):
# #         try:
# #             if tipoConsulta == "select":
# #                 return consulta.execute().data
# #             else: 
# #                 return consulta.execute()
# #         except Exception as e:
# #             return f"error: {e}"

# #     def mostrarReporte(self):
# #         consulta = self.__db.table(self.__nombreTabla).select("*")
# #         return self.__ejecutarConsultas(consulta,"select")
    
# #     def insertarAsistencia(self,asistencia_docente:dict):
# #         consulta = self.__db.table(self.__nombreTabla).insert(asistencia_docente)
# #         return self.__ejecutarConsultas(consulta)

# # from conexion import ConexionDB

# # class DAsistenciaDocente:
# #     def __init__(self):
# #         self.__db = ConexionDB().conexionSupabase()
# #         self.__nombreTabla = "asistencia_docente"

# #     def __ejecutarConsultas(self, consulta, tipoConsulta=None):
# #         try:
# #             resultado = consulta.execute()
# #             # IMPORTANTE: imprimir para depuración
# #             print("SUPABASE RESPUESTA:", resultado)
# #             return resultado.data if tipoConsulta == "select" else resultado
# #         except Exception as e:
# #             print(f"ERROR EN SUPABASE: {e}")
# #             return None

# #     def mostrarReporte(self):
# #         consulta = self.__db.table(self.__nombreTabla).select("*")
# #         return self.__ejecutarConsultas(consulta, "select")
    
# #     def insertarAsistencia(self, asistencia_docente: dict):
# #         consulta = self.__db.table(self.__nombreTabla).insert(asistencia_docente)
# #         return self.__ejecutarConsultas(consulta)
# # from conexion import ConexionDB

# # class DAsistenciaDocente:
# #     def __init__(self):
# #         self.__db = ConexionDB().conexionSupabase()
# #         self.__nombreTabla = "asistencia_docente"

# #     def __ejecutarConsultas(self, consulta, tipoConsulta=None):
# #         try:
# #             if tipoConsulta == "select":
# #                 return consulta.execute().data
# #             else:
# #                 return consulta.execute()
# #         except Exception as e:
# #             return {"error": str(e)}

# #     def mostrarReporte(self):
# #         consulta = self.__db.table(self.__nombreTabla).select("*")
# #         return self.__ejecutarConsultas(consulta, "select")

# #     def buscarPorDni(self, dni: str):
# #         consulta = (
# #             self.__db.table(self.__nombreTabla)
# #             .select("*")
# #             .eq("dni", dni)
# #         )
# #         return self.__ejecutarConsultas(consulta, "select")

# #     def estadisticasPorDni(self, dni: str):
# #         consulta = (
# #             self.__db.table(self.__nombreTabla)
# #             .select("estado")
# #             .eq("dni", dni)
# #         )
# #         return self.__ejecutarConsultas(consulta, "select")

# #     def insertarAsistencia(self, asistencia_docente: dict):
# #         consulta = self.__db.table(self.__nombreTabla).insert(asistencia_docente)
# #         return self.__ejecutarConsultas(consulta)


# # nuevo

# from conexion import ConexionDB

# class DAsistenciaDocente:
#     def __init__(self):
#         self.__db = ConexionDB().conexionSupabase()

#     def __ejecutar(self, consulta, tipo=None):
#         try:
#             if tipo == "select":
#                 return consulta.execute().data
#             return consulta.execute()
#         except Exception as e:
#             return {"error": str(e)}

#     # ASISTENCIA 
#     def mostrarReporte(self):
#         return self.__ejecutar(
#             self.__db.table("asistencia_docente").select("*"),
#             "select"
#         )

#     def buscarPorDni(self, dni):
#         return self.__ejecutar(
#             self.__db.table("asistencia_docente")
#             .select("*")
#             .eq("dni", dni),
#             "select"
#         )

#     def estadisticasPorDni(self, dni):
#         return self.__ejecutar(
#             self.__db.table("asistencia_docente")
#             .select("estado")
#             .eq("dni", dni),
#             "select"
#         )

#     def insertarAsistencia(self, data):
#         return self.__ejecutar(
#             self.__db.table("asistencia_docente").insert(data)
#         )

#     #  PERSONA / DOCENTE 
#     def insertarPersona(self, persona):
#         print(persona)
#         return self.__ejecutar(
#             self.__db.table("persona").insert(persona)
#         )
    
#     def insertarDocente(self, docente):
#         return self.__ejecutar(
#             self.__db.table("docente").insert(docente)
#         )


#     # ELIMINAR DOCENTE 

#     def eliminarDocenteTotal(self, dni):
        
#         cursos = self.__ejecutar(
#             self.__db.table("docente_curso")
#             .select("id_docente_curso")
#             .eq("dni_docente", dni),
#             "select"
#         )

#         if cursos:
#             for c in cursos:
#                 # Eliminar notas 
#                 self.__ejecutar(
#                     self.__db.table("nota")
#                     .delete()
#                     .eq("id_docente_curso", c["id_docente_curso"])
#                 )

#         #  Eliminar asistencia docente
#         self.__ejecutar(
#             self.__db.table("asistencia_docente")
#             .delete()
#             .eq("dni", dni)
#         )

#         # 4️⃣ Eliminar docente_curso
#         self.__ejecutar(
#             self.__db.table("docente_curso")
#             .delete()
#             .eq("dni_docente", dni)
#         )

#         # 5️⃣ Eliminar docente
#         self.__ejecutar(
#             self.__db.table("docente")
#             .delete()
#             .eq("dni", dni)
#         )

#         # 6️⃣ Eliminar persona
#         return self.__ejecutar(
#             self.__db.table("persona")
#             .delete()
#             .eq("dni", dni)
#         )

from supabase import create_client, Client
from datetime import datetime

class DAsistencia:
    def __init__(self):
        self.url = "https://pdscvmdbzisbftyntbvm.supabase.co"
        self.key = "sb_secret_YuifpPDISeOjxdtHrCPLjw_AsImaGWJ"
        self.supabase: Client = create_client(self.url, self.key)

    # ================= Personas =================
    def insertar_persona(self, persona):
        existing = self.supabase.table("persona").select("*")\
                        .eq("nombres", persona["nombres"])\
                        .eq("apellidos", persona["apellidos"]).execute()
        if existing.data:
            return False, "Persona ya registrada"
        result = self.supabase.table("persona").insert(persona).execute()
        return True, "Registrado correctamente"

    def listar_personas(self):
        result = self.supabase.table("persona").select("*").execute()
        return result.data if result.data else []

    # ================= Asistencias =================

    def registrar_asistencia(self, dni, rol, estado="FALTA", comentario=""):
    # 🔒 Validar que el DNI pertenezca al rol correcto
        if not self.validar_dni_por_rol(dni, rol):
            return False, f"❌ El DNI no pertenece a un {rol}"

        fecha = datetime.now().date().isoformat()
        hora = datetime.now().strftime("%H:%M:%S")

        if rol.lower() == "docente":
            tabla = "asistencia_docente"
            data = {
                "dni": dni,
                "fecha": fecha,
                "hora_entrada": hora,
                "hora_salida": None,
                "estado": estado,
                "comentario": comentario
            }
        else:
            tabla = "asistencia_alumno"
            data = {
                "dni": dni,
                "fecha": fecha,
                "hora_entrada": hora,
                "estado": estado,
                "comentario": comentario
            }

        # 🔁 Evitar doble registro el mismo día
        existe = self.supabase.table(tabla) \
            .select("dni") \
            .eq("dni", dni) \
            .eq("fecha", fecha) \
            .execute()

        if existe.data:
            return False, "Ya tiene asistencia registrada hoy"

        self.supabase.table(tabla).insert(data).execute()
        return True, "Asistencia registrada correctamente"

    
    def validar_dni_por_rol(self, dni, rol):
        tabla = "docente" if rol.lower() == "docente" else "alumno"

        res = self.supabase.table(tabla) \
            .select("dni") \
            .eq("dni", dni) \
            .execute()

        return bool(res.data)


    def registrar_salida(self, dni, rol):
        if rol.lower() != "docente":
            return False, "Los alumnos no registran salida"

        hora = datetime.now().strftime("%H:%M:%S")
        fecha = datetime.now().date().isoformat()

        self.supabase.table("asistencia_docente") \
            .update({"hora_salida": hora}) \
            .eq("dni", dni) \
            .eq("fecha", fecha) \
            .is_("hora_salida", None) \
            .execute()

        return True, "Salida registrada"


    def listar_asistencias(self, rol):
        tabla = "asistencia_docente" if rol.lower() == "docente" else "asistencia_alumno"
        result = self.supabase.table(tabla).select("*").execute()
        return result.data if result.data else []

    def editar_asistencia(self, dni, fecha, datos, rol):
        tabla = "asistencia_docente" if rol.lower() == "docente" else "asistencia_alumno"
        result = self.supabase.table(tabla).update(datos)\
            .eq("dni", dni).eq("fecha", fecha).execute()
        return True, "Editado correctamente"

    def eliminar_asistencia(self, dni, fecha, rol):
        tabla = "asistencia_docente" if rol.lower() == "docente" else "asistencia_alumno"
        result = self.supabase.table(tabla).delete().eq("dni", dni).eq("fecha", fecha).execute()
        return True, "Eliminado correctamente"
from supabase import Client

class DPersona:
    def __init__(self, supabase: Client):
        self.supabase = supabase

    def insertar_persona_y_rol(self, persona):
        try:
            # 1️⃣ Insertar en tabla persona
            res = self.supabase.table("persona").insert(persona).execute()

            if not res.data:
                return False, "No se pudo registrar la persona"

            dni = persona["dni"]
            rol = persona["rol"].upper()

            # 2️⃣ Insertar según rol
            if rol == "DOCENTE":
                self.supabase.table("docente").insert({
                    "dni": dni
                }).execute()

            elif rol == "ALUMNO":
                self.supabase.table("alumno").insert({
                    "dni": dni
                }).execute()

            else:
                return False, "Rol no válido"

            return True, "Persona registrada correctamente"

        except Exception as e:
            return False, f"Error BD: {str(e)}"

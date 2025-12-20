# # from capaLogica.lAsistencia import LDocente
# # import streamlit as st

# # class PAsistenciaDocente:
# #     def __init__(self):
# #         self.lDocente = LDocente()
# #         self.construirInterfaz()

# #     # def construirInterfaz(self):
# #     #     st.tittle('REPORTE ASISTENCIAS DOCENTE')
# #     #     with st.form("FormularioRegistro"):
# #     #         txtId = st.text_input("id")
# #     #         txtDni = st.text_input("DNI")
# #     #         txtFecha = st.datetime_input("fecha de registro" )
# #     #         txtHoraEntrada = st.datetime_input()
# #     #         txtHoraSalida =
# #     #         txtEstado =
# #     #         txtComentario = 
# #     #         btnGuardar = st.form_submit_button ("registrar asistencia", type="primary")

# #     def construirInterfaz(self):
# #         st.title("REPORTE ASISTENCIAS DOCENTE")

# #         with st.form("FormularioRegistro"):

# #             txtDni = st.text_input("DNI")
# #             fecha_actual = st.date_input("Fecha")            # hora_entrada = st.time_input("-hora de entrada")
# #             hora_entrada = st.time_input("Hora de entrada (HH:MM)", step=60)
# #             hora_salida = st.time_input("Hora de salida (HH:MM)", step=60)

# #             txtEstado = st.selectbox(
# #                 "Estado de Asistencia",
# #                 ["PRESENTE", "TARDANZA", "FALTA", "JUSTIFICADO"]
# #             )

# #             txtComentario = st.text_input("Comentario / Descripción")
# #             btnGuardar = st.form_submit_button("Registrar Asistencia", type="primary")

# #         if hora_entrada:
# #             hora_entrada_str = hora_entrada.strftime("%H:%M:00")  
# #             st.write("Se enviará a Supabase como:", hora_entrada_str)
# #         if btnGuardar:
            
# #             fecha_str = fecha_actual.strftime("%Y-%m-%d")
# #             hora_entrada_str = f"{hora_entrada.strftime('%H:%M')}:00" if hora_entrada else None
# #             hora_salida_str = f"{hora_salida.strftime('%H:%M')}:00" if hora_salida else None

# #             asistencia_docente = {
# #                 "dni": txtDni,
# #                 "fecha": fecha_str,
# #                 "hora_entrada": hora_entrada_str,
# #                 "hora_salida": hora_salida_str,
# #                 "estado": txtEstado,
# #                 "comentario": txtComentario
# #             }
# #             # asistencia_docente = {
# #             #     "id_asist_doc" :    
# #             #     "dni": txtDni,
# #             #     "fecha": fecha_actual,
# #             #     "hora_entrada": hora_entrada,
# #             #     "hora_salida": hora_salida,
# #             #     "estado": txtEstado,
# #             #     "comentario": txtComentario
# #             # }
# #             self.insertarAsistencia(asistencia_docente)
# #         self.mostrarReportes()
        

# #         st.success("Asistencia registrada correctamente ✔")

# #     def mostrarReportes(self):
# #         listaAsistencia = self.lDocente.mostrarReporte()
# #         st.dataframe(listaAsistencia)

# #     def insertarAsistencia(self, asistencia_docente : dict):
# #         self.lDocente.insertarAsistencia(asistencia_docente)
# #         st.toast("Presionador", icon = "🔥", duration= "short")

# # from capaLogica.lAsistencia import LDocente
# # import streamlit as st

# # class PAsistenciaDocente:
# #     def __init__(self):
# #         self.lDocente = LDocente()
# #         self.construirInterfaz()

# #     def construirInterfaz(self):
# #         st.title("REPORTE ASISTENCIAS DOCENTE")

# #         with st.form("FormularioRegistro"):

# #             txtDni = st.text_input("DNI")
# #             fecha_actual = st.date_input("Fecha (AAAA-MM-DD)")

# #             # SOLO HORA Y MINUTO
# #             hora_entrada = st.time_input("Hora de entrada", step=60)
# #             hora_salida = st.time_input("Hora de salida", step=60)

# #             # ESTADOS PERMITIDOS SEGÚN TU BASE DE DATOS
# #             txtEstado = st.selectbox(
# #                 "Estado de Asistencia",
# #                 ["ASISTIO", "TARDANZA", "FALTA"]     # CORREGIDO
# #             )

# #             txtComentario = st.text_input("Comentario / Descripción")

# #             btnGuardar = st.form_submit_button("Registrar Asistencia", type="primary")

# #         if btnGuardar:

# #             fecha_str = fecha_actual.strftime("%Y-%m-%d")
# #             hora_entrada_str = hora_entrada.strftime("%H:%M") if hora_entrada else None
# #             hora_salida_str = hora_salida.strftime("%H:%M") if hora_salida else None

# #             asistencia_docente = {
# #                 "dni": txtDni,
# #                 "fecha": fecha_str,
# #                 "hora_entrada": hora_entrada_str,
# #                 "hora_salida": hora_salida_str,
# #                 "estado": txtEstado,
# #                 "comentario": txtComentario
# #             }

# #             self.insertarAsistencia(asistencia_docente)

# #             st.success("Asistencia registrada correctamente ✔")

# #         self.mostrarReportes()

# #     def mostrarReportes(self):
# #         lista = self.lDocente.mostrarReporte()
# #         st.dataframe(lista)

# #     def insertarAsistencia(self, asistencia_docente: dict):
# #         self.lDocente.insertarAsistencia(asistencia_docente)
# #         st.toast("Guardado", icon="🔥", duration="short")


# # from capaLogica.lAsistencia import LDocente
# # import streamlit as st
# # import pandas as pd

# # class PAsistenciaDocente:
# #     def __init__(self):
# #         self.lDocente = LDocente()
# #         self.construirInterfaz()

# #     def construirInterfaz(self):
# #         st.title("REPORTE - ASISTENCIA DOCENTE")

# #         # ---------- FORM REGISTRO ----------
# #         with st.form("FormularioRegistro"):
# #             txtDni = st.text_input("DNI del docente")
# #             fecha_actual = st.date_input("Fecha")
# #             hora_entrada = st.time_input("Hora de entrada (HH:MM)", step=60)
# #             hora_salida = st.time_input("Hora de salida (HH:MM)", step=60)

# #             txtEstado = st.selectbox(
# #                 "Estado",
# #                 ["PRESENTE", "TARDANZA", "FALTA", "JUSTIFICADO"]
# #             )

# #             txtComentario = st.text_input("Comentario")

# #             btnGuardar = st.form_submit_button("Registrar Asistencia", type="primary")

# #         if btnGuardar:
# #             fecha_str = fecha_actual.strftime("%Y-%m-%d")
# #             hora_entrada_str = f"{hora_entrada.strftime('%H:%M')}:00"
# #             hora_salida_str = f"{hora_salida.strftime('%H:%M')}:00"

# #             asistencia_docente = {
# #                 "dni": txtDni,
# #                 "fecha": fecha_str,
# #                 "hora_entrada": hora_entrada_str,
# #                 "hora_salida": hora_salida_str,
# #                 "estado": txtEstado,
# #                 "comentario": txtComentario
# #             }

# #             self.insertarAsistencia(asistencia_docente)
# #             st.success("✔ Asistencia registrada correctamente")

# #         st.divider()

# #         # ---------- REPORTE POR DNI ----------
# #         st.subheader("🔍 Buscar reporte por DNI")

# #         dni_buscar = st.text_input("Ingrese DNI a consultar")
# #         btnBuscar = st.button("Generar Reporte")

# #         if btnBuscar:
# #             datos = self.lDocente.buscarPorDni(dni_buscar)

# #             if datos:
# #                 st.dataframe(datos)
# #             else:
# #                 st.warning("⚠ No se encontraron registros para ese DNI")

# #             # ----------- REPORTE ESTADÍSTICO -----------
# #             st.subheader("📊 Estadísticas del docente")

# #             estadisticas = self.lDocente.estadisticasPorDni(dni_buscar)

# #             if estadisticas:
# #                 df = pd.DataFrame(estadisticas)

# #                 total = len(df)

# #                 conteo = df["estado"].value_counts()

# #                 presente = conteo.get("PRESENTE", 0)
# #                 tardanza = conteo.get("TARDANZA", 0)
# #                 falta = conteo.get("FALTA", 0)
# #                 justificado = conteo.get("JUSTIFICADO", 0)

# #                 st.write(f"Total registros: **{total}**")
# #                 st.write(f"Asistencias: **{presente}** ({round((presente/total)*100,2)}%)")
# #                 st.write(f"Tardanzas: **{tardanza}** ({round((tardanza/total)*100,2)}%)")
# #                 st.write(f"Faltas: **{falta}** ({round((falta/total)*100,2)}%)")
# #                 st.write(f"Justificados: **{justificado}** ({round((justificado/total)*100,2)}%)")

# #                 # ----------- GRÁFICO Pie ----------
# #                 st.subheader("📈 Distribución de Asistencias")

# #                 st.pyplot(df["estado"].value_counts().plot.pie(autopct="%1.1f%%").figure)
# #             else:
# #                 st.warning("No hay datos para estadísticas")

# #         st.divider()

# #         # ---------- REPORTE GENERAL ----------
# #         st.subheader("📌 Reporte general")
# #         listaAsistencia = self.lDocente.mostrarReporte()
# #         st.dataframe(listaAsistencia)

# #     def insertarAsistencia(self, asistencia_docente: dict):
# #         self.lDocente.insertarAsistencia(asistencia_docente)
# #         st.toast("Guardado correctamente", icon="🔥", duration="short")

# #nuevo 
# from capaLogica.lAsistencia import LDocente
# import streamlit as st
# import pandas as pd
# from datetime import date

# class PAsistenciaDocente:
#     def __init__(self):
#         self.lDocente = LDocente()
#         self.construirInterfaz()

#     def construirInterfaz(self):
#         st.title("REPORTE - ASISTENCIA DOCENTE")

        
#         st.subheader(" Registrar nuevo docente")

#         with st.form("FormularioNuevoDocente"):
#             dni = st.text_input("DNI")
#             nombres = st.text_input("Nombres")
#             apellidos = st.text_input("Apellidos")
#             telefono = st.text_input("Teléfono")
#             direccion = st.text_input("Dirección")

#             fecha_nac = st.text_input(
#                 "Fecha de nacimiento formato : YYYY-MM-DD"
#             )
          
            
#             sexo = st.selectbox("Sexo", ["M", "F"])
#             correo = st.text_input("Correo")
#             contrasenia = st.text_input("Contraseña", type="password")

#             especialidad = st.text_input("Especialidad")
#             titulo = st.text_input("Título profesional")

#             btnRegistrarDocente = st.form_submit_button("Registrar Docente")

#         if btnRegistrarDocente:
            
#             variableFecha = date.strptime(fecha_nac ,"%Y-%m-%d")
#             variableSql = variableFecha.strftime('%Y-%m-%d')    
#             persona = {
#                 "dni": dni,
#                 "nombres": nombres,
#                 "apellidos": apellidos,
#                 "telefono": telefono,
#                 "direccion": direccion,
#                 "fecha_nacimiento" : variableSql,
#                 "sexo": sexo,
#                 "rol": "DOCENTE",
#                 "correo": correo,
#                 "contrasenia": contrasenia
#             }

#             docente = {
#                 "dni": dni,
#                 "especialidad": especialidad,
#                 "titulo": titulo
#             }

#             self.lDocente.registrarPersonaDocente(persona, docente)
#             st.success("✔ Docente registrado correctamente")

#         st.divider()

        
        
#         st.subheader("Eliminar docente")

#         with st.form("FormularioEliminarDocente"):
#             dni_eliminar = st.text_input("DNI del docente a eliminar")
#             btnEliminar = st.form_submit_button("Eliminar Docente")

#         if btnEliminar:
#             self.lDocente.eliminarDocente(dni_eliminar)
#             st.success("✔ Docente eliminado correctamente")

#         st.divider()

       
#         with st.form("FormularioRegistro"):
#             txtDni = st.text_input("DNI del docente")
#             fecha_actual = st.date_input("Fecha")
#             hora_entrada = st.time_input("Hora de entrada", step=60)
#             hora_salida = st.time_input("Hora de salida", step=60)

#             txtEstado = st.selectbox(
#                 "Estado",
#                 ["PRESENTE", "TARDANZA", "FALTA", "JUSTIFICADO"]
#             )

#             txtComentario = st.text_input("Comentario")
#             btnGuardar = st.form_submit_button("Registrar Asistencia", type="primary")

#         if btnGuardar:
#             hora_salida_final = None
#             if txtEstado not in ["FALTA", "JUSTIFICADO"]:
#                 hora_salida_final = f"{hora_salida.strftime('%H:%M')}:00"

#             asistencia_docente = {
#                 "dni": txtDni,
#                 "fecha": fecha_actual.strftime("%Y-%m-%d"),
#                 "hora_entrada": f"{hora_entrada.strftime('%H:%M')}:00",
#                 "hora_salida": hora_salida_final,
#                 "estado": txtEstado,
#                 "comentario": txtComentario
#             }

#             self.lDocente.insertarAsistencia(asistencia_docente)
#             st.success("✔ Asistencia registrada correctamente")

#         st.divider()

#         st.subheader(" Buscar reporte por DNI")

#         dni_buscar = st.text_input("Ingrese DNI a consultar")
#         btnBuscar = st.button("Generar Reporte")

#         if btnBuscar:
#             datos = self.lDocente.buscarPorDni(dni_buscar)

#             if datos:
#                 st.dataframe(datos)
#             else:
#                 st.warning("No se encontraron registros")

#             st.subheader("Estadísticas del docente")
#             estadisticas = self.lDocente.estadisticasPorDni(dni_buscar)

#             if estadisticas:
#                 df = pd.DataFrame(estadisticas)
#                 total = len(df)
#                 conteo = df["estado"].value_counts()

#                 st.write(f"Total: {total}")
#                 st.write(conteo)

#                 st.subheader("Distribución")
#                 st.pyplot(conteo.plot.pie(autopct="%1.1f%%").figure)

#         st.divider()

#         st.subheader(" Reporte general")
#         st.dataframe(self.lDocente.mostrarReporte())


from capaLogica.lAsistencia import LDocente
import streamlit as st
import pandas as pd
from datetime import datetime,date
import re

class PAsistenciaDocente:
    def __init__(self):
        self.lDocente = LDocente()
        self.construirInterfaz()

    # ================= VALIDACIONES =================
    def validar_dni(self, dni):
        return dni.isdigit() and len(dni) in [8, 9]

    def validar_telefono(self, telefono):
        return telefono.isdigit() and len(telefono) in [9, 10]

    def validar_correo(self, correo):
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(patron, correo)

    def validar_vacios(self, campos):
        for v in campos.values():
            if v.strip() == "":
                return False
        return True

    # ================= INTERFAZ =================
    def construirInterfaz(self):
        st.title("Avance ISCOS")

        # =================================================
        # 1️⃣ REGISTRAR DOCENTE
        # =================================================
        st.subheader("1. Registrar docente")

        with st.form("FormularioNuevoDocente"):
            dni = st.text_input("DNI")
            nombres = st.text_input("Nombres")
            apellidos = st.text_input("Apellidos")
            telefono = st.text_input("Teléfono")
            direccion = st.text_input("Dirección")
            fecha_nac = st.text_input("Fecha de nacimiento (YYYY-MM-DD)")
            sexo = st.selectbox("Sexo", ["M", "F"])
            correo = st.text_input("Correo")
            contrasenia = st.text_input("Contraseña", type="password")
            especialidad = st.text_input("Especialidad")
            titulo = st.text_input("Título profesional")

            btnRegistrar = st.form_submit_button("Registrar Docente")

        if btnRegistrar:
            campos = {
                "dni": dni,
                "nombres": nombres,
                "apellidos": apellidos,
                "telefono": telefono,
                "direccion": direccion,
                "fecha": fecha_nac,
                "correo": correo,
                "contrasenia": contrasenia,
                "especialidad": especialidad,
                "titulo": titulo
            }

            if not self.validar_vacios(campos):
                st.error("❌ No se permiten campos vacíos")
                return

            if not self.validar_dni(dni):
                st.error("❌ DNI inválido (8 o 9 dígitos)")
                return

            if not self.validar_telefono(telefono):
                st.error("❌ Teléfono inválido (9 o 10 dígitos)")
                return

            if not self.validar_correo(correo):
                st.error("❌ Correo inválido")
                return

            # ❗❗❗ FECHA EXACTAMENTE COMO TÚ LA ENVIASTE ❗❗❗
            variableFecha = datetime.strptime(fecha_nac ,"%Y-%m-%d").date
            variableSql = variableFecha.strftime('%Y-%m-%d')

            persona = {
                "dni": dni,
                "nombres": nombres,
                "apellidos": apellidos,
                "telefono": telefono,
                "direccion": direccion,
                "fecha_nacimiento": variableSql,
                "sexo": sexo,
                "rol": "DOCENTE",
                "correo": correo,
                "contrasenia": contrasenia
            }

            docente = {
                "dni": dni,
                "especialidad": especialidad,
                "titulo": titulo
            }

            self.lDocente.registrarPersonaDocente(persona, docente)
            st.success("✔ Docente registrado correctamente")

        st.divider()

        # =================================================
        # 2️⃣ REGISTRAR ASISTENCIA DOCENTE
        # =================================================
        st.subheader("2. Registrar asistencia docente")

        with st.form("FormularioAsistencia"):
            txtDni = st.text_input("DNI del docente")
            fecha_actual = st.date_input("Fecha")
            hora_entrada = st.time_input("Hora de entrada", step=60)
            hora_salida = st.time_input("Hora de salida", step=60)
            estado = st.selectbox(
                "Estado",
                ["PRESENTE", "TARDANZA", "FALTA", "JUSTIFICADO"]
            )
            comentario = st.text_input("Comentario")

            btnGuardar = st.form_submit_button("Registrar asistencia")

        if btnGuardar:
            if not self.validar_dni(txtDni):
                st.error("❌ DNI inválido")
                return

            hora_salida_final = None
            if estado not in ["FALTA", "JUSTIFICADO"]:
                hora_salida_final = f"{hora_salida.strftime('%H:%M')}:00"

            asistencia = {
                "dni": txtDni,
                "fecha": fecha_actual.strftime("%Y-%m-%d"),
                "hora_entrada": f"{hora_entrada.strftime('%H:%M')}:00",
                "hora_salida": hora_salida_final,
                "estado": estado,
                "comentario": comentario
            }

            self.lDocente.insertarAsistencia(asistencia)
            st.success("✔ Asistencia registrada correctamente")

        st.divider()

        # =================================================
        # 3️⃣ REPORTE GENERAL
        # =================================================
        st.subheader("3. Reporte general")
        st.dataframe(self.lDocente.mostrarReporte())

        st.divider()

        # =================================================
        # 4️⃣ ELIMINAR DOCENTE
        # =================================================
        st.subheader("4. Eliminar docente")

        with st.form("FormularioEliminar"):
            dni_eliminar = st.text_input("DNI del docente")
            btnEliminar = st.form_submit_button("Eliminar docente")

        if btnEliminar:
            if not self.validar_dni(dni_eliminar):
                st.error("❌ DNI inválido")
            else:
                self.lDocente.eliminarDocente(dni_eliminar)
                st.success("✔ Docente eliminado correctamente")

        st.divider()

        # =================================================
        # 5️⃣ REPORTE POR DNI (CON GRÁFICO)
        # =================================================
        st.subheader("5. Reporte por DNI")

        dni_buscar = st.text_input("Ingrese DNI")
        btnBuscar = st.button("Generar reporte")

        if btnBuscar:
            if not self.validar_dni(dni_buscar):
                st.error("❌ DNI inválido")
                return

            datos = self.lDocente.buscarPorDni(dni_buscar)
            if datos:
                st.dataframe(datos)
            else:
                st.warning("No se encontraron registros")

            estadisticas = self.lDocente.estadisticasPorDni(dni_buscar)
            if estadisticas:
                df = pd.DataFrame(estadisticas)
                conteo = df["estado"].value_counts()
                st.pyplot(conteo.plot.pie(autopct="%1.1f%%").figure)

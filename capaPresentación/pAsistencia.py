

from capaLogica.lAsistencia import LDocente
import streamlit as st
import pandas as pd
from datetime import datetime, date
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
        return re.match(patron, correo) is not None


    def validar_vacios(self, campos):
        for v in campos.values():
            if v.strip() == "":
                return False
        return True


    def validar_edad_minima(self, fecha_nac):
        try:
            fecha_nacimiento = datetime.strptime(fecha_nac, "%Y-%m-%d").date()
            hoy = date.today()
            edad = hoy.year - fecha_nacimiento.year - (
                (hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day)
            )
            return edad >= 23
        except:
            return False


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
            elif not self.validar_dni(dni):
                st.error("❌ DNI inválido (8 o 9 dígitos)")
            elif not self.validar_telefono(telefono):
                st.error("❌ Teléfono inválido (9 o 10 dígitos)")
            elif not self.validar_correo(correo):
                st.error("❌ Correo inválido")
            elif not self.validar_edad_minima(fecha_nac):
                st.error("❌ El docente debe tener mínimo 23 años")
            else:
                # FECHA EXACTA COMO TÚ LA MANDASTE
                variableFecha = datetime.strptime(fecha_nac, "%Y-%m-%d").date()
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
            else:
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
            else:
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


	

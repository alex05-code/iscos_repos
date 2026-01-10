
# IMPORTS


import streamlit as st              # Interfaz web
import pandas as pd                 # Tablas y dataframes
from datetime import datetime, date # Fechas
import re                           # Expresiones regulares
from capaLogica.lAsistencia import LAsistencia  # Capa lógica


# CLASE PRESENTACIÓN

class PAsistenciaDocente:
    def __init__(self):
        # Instancia de la capa lógica
        self.logic = LAsistencia()
        # Carga el menú principal
        self.menu_principal()


    # VALIDACIONES
    

    def validar_contrasenia(self, contrasenia):
        if len(contrasenia) < 8:
            return False
        if " " in contrasenia:
            return False
        if not re.search(r"[A-Z]", contrasenia):
            return False
        if not re.search(r"[a-zA-Z]", contrasenia):
            return False
        if not re.search(r"[0-9]", contrasenia):
            return False
        if not re.search(r"[^\w\s]", contrasenia):
            return False
        return True

    def validar_dni(self, dni):
        # DNI solo números y 8 o 9 dígitos
        return dni.isdigit() and len(dni) in [8, 9]

    def validar_correo(self, correo):
        # Formato básico de correo
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(patron, correo) is not None

    def validar_solo_letras(self, texto):
        # Solo letras (mayúsculas/minúsculas), espacios y tildes
        patron = r"^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$"
        return re.match(patron, texto) is not None

    def validar_vacios(self, campos):
        # Ningún campo vacío
        for v in campos.values():
            if str(v).strip() == "":
                return False
        return True

    def validar_edad(self, fecha_nac, rol):
        # Valida edad según rol
        try:
            fecha = datetime.strptime(fecha_nac, "%Y-%m-%d").date()
            hoy = date.today()
            edad = hoy.year - fecha.year - (
                (hoy.month, hoy.day) < (fecha.month, fecha.day)
            )

            if rol == "docente":
                return edad >= 23
            elif rol == "alumno":
                return 10 <= edad <= 19
            return True
        except:
            return False

    def validar_dni_logico(self, dni):
    # solo números y exactamente 8 dígitos
        if not dni.isdigit() or len(dni) != 8:
            return False

        # no permitir todos los dígitos iguales (00000000, 66666666, etc)
        if dni == dni[0] * 8:
            return False

        # no permitir que empiece con 0
        if dni.startswith("0"):
            return False

        return True


    # ===============================
    # MENÚ PRINCIPAL
    # ===============================

    def menu_principal(self):
        opciones = [
            "Registrar Persona",
            "Registrar Asistencia",
            "Registrar Salida",
            "Editar/Eliminar Asistencia",
            "Reporte"
        ]

        menu = st.sidebar.selectbox("Menú", opciones)

        if menu == "Registrar Persona":
            self.vista_registrar_persona()
        elif menu == "Registrar Asistencia":
            self.vista_registrar_asistencia()
        elif menu == "Registrar Salida":
            self.vista_registrar_salida()
        elif menu == "Editar/Eliminar Asistencia":
            self.vista_editar_eliminar_asistencia()
        elif menu == "Reporte":
            self.vista_reporte()


    # ===============================
    # REGISTRAR PERSONA
    # ===============================

    def vista_registrar_persona(self):
        st.header("Registrar Persona")

        with st.form("form_persona"):
            dni = st.text_input("DNI")
            nombres = st.text_input("Nombres")
            apellidos = st.text_input("Apellidos")
            sexo = st.selectbox("Sexo", ["M", "F"])
            rol = st.selectbox("Rol", ["docente", "alumno"])
            fecha_nac = st.text_input("Fecha de nacimiento (YYYY-MM-DD)")
            correo = st.text_input("Correo")
            contrasenia = st.text_input("Contraseña", type="password")

            submitted = st.form_submit_button("Registrar")

            if submitted:
                persona = {
                    "dni": dni,
                    "nombres": nombres,
                    "apellidos": apellidos,
                    "sexo": sexo,
                    "rol": rol.upper(),
                    "fecha_nacimiento": fecha_nac,
                    "correo": correo,
                    "contrasenia": contrasenia
                }

                # Validaciones
                
                if not self.validar_vacios(persona):
                    st.error("No se permiten campos vacíos")
                elif not self.validar_dni_logico(dni):
                    st.error("DNI inválido o no real")
                elif not self.validar_contrasenia(contrasenia):
                    st.error("❌ La contraseña debe tener mínimo 8 caracteres, "
                    "una mayúscula, una letra, un número, un símbolo y sin espacios"
                    )
                elif not self.validar_solo_letras(nombres):
                    st.error("❌ Los nombres no deben contener números ni símbolos")
                elif not self.validar_solo_letras(apellidos):
                    st.error("❌ Los apellidos no deben contener números ni símbolos")
                elif correo and not self.validar_correo(correo):
                    st.error("Correo inválido")
                elif not self.validar_edad(fecha_nac, rol):
                    st.error("Edad inválida según rol")
                else:
                    ok, msg = self.logic.registrar_persona(persona)
                    st.success(msg) if ok else st.error(msg)
                
        # Mostrar personas registradas
        personas = self.logic.listar_personas()
        if personas:
            df = pd.DataFrame(personas)[["dni", "nombres", "apellidos", "sexo", "rol"]]
            st.dataframe(df)


    # ===============================
    # REGISTRAR ASISTENCIA
    # ===============================

    def vista_registrar_asistencia(self):
        st.header("Registrar Asistencia")

        dni = st.text_input("DNI")
        rol = st.selectbox("Rol", ["docente", "alumno"])
        estado = st.selectbox("Estado", ["PRESENTE", "FALTA", "JUSTIFICADO"])
        comentario = st.text_area("Comentario")

        if st.button("Registrar Asistencia"):
            ok, msg = self.logic.registrar_asistencia(dni, rol, estado, comentario)
            st.success(msg) if ok else st.error(msg)

        asistencias = self.logic.listar_asistencias(rol)
        if asistencias:
            st.dataframe(pd.DataFrame(asistencias))


    # ===============================
    # REGISTRAR SALIDA
    # ===============================

    def vista_registrar_salida(self):
        st.header("Registrar Salida")

        dni = st.text_input("DNI")
        rol = st.selectbox("Rol", ["docente", "alumno"])

        if st.button("Registrar Salida"):
            ok, msg = self.logic.registrar_salida(dni, rol)
            st.success(msg) if ok else st.error(msg)


    # ===============================
    # EDITAR / ELIMINAR ASISTENCIA
    # ===============================

    def vista_editar_eliminar_asistencia(self):
        st.header("Editar / Eliminar Asistencia")

        rol = st.selectbox("Rol", ["docente", "alumno"])
        asistencias = self.logic.listar_asistencias(rol)

        if not asistencias:
            st.info("No hay asistencias")
            return

        df = pd.DataFrame(asistencias)
        df["seleccionar"] = False

        edited_df = st.data_editor(df, use_container_width=True)

        for i, fila in edited_df.iterrows():
            if fila["seleccionar"]:
                estado = st.selectbox(
                    "Estado",
                    ["PRESENTE", "FALTA", "JUSTIFICADO"],
                    key=f"estado_{i}"
                )
                comentario = st.text_area(
                    "Comentario",
                    fila.get("comentario", ""),
                    key=f"coment_{i}"
                )

                if st.button("Actualizar", key=f"upd_{i}"):
                    self.logic.editar_asistencia(
                        fila["dni"], fila["fecha"],
                        {"estado": estado, "comentario": comentario},
                        rol
                    )

                if st.button("Eliminar", key=f"del_{i}"):
                    self.logic.eliminar_asistencia(
                        fila["dni"], fila["fecha"], rol
                    )


    # ===============================
    # REPORTES
    # ===============================

    def vista_reporte(self):
        st.header("Reporte Estadístico")

        rol = st.selectbox("Rol", ["docente", "alumno"])
        asistencias = self.logic.listar_asistencias(rol)

        if not asistencias:
            st.info("No hay asistencias")
            return

        df = pd.DataFrame(asistencias)

        st.subheader("Reporte General")
        st.bar_chart(df["estado"].value_counts())

        st.subheader("Reporte por DNI")
        dni = st.text_input("Buscar por DNI")

        if dni:
            df_dni = df[df["dni"] == dni]
            if not df_dni.empty:
                st.bar_chart(df_dni["estado"].value_counts())
            else:
                st.info("No hay registros para ese DNI")

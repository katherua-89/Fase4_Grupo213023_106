import tkinter as tk
from tkinter import messagebox, ttk

# Aporte de Katerin Marcela Rua Sanchez: la interfaz se organiza en pestañas
# para separar clientes, servicios, reservas y consulta de eventos.
from Software_FJ.controllers.ClienteControlador import ClienteControlador
from Software_FJ.controllers.ReservaControlador import ReservaControlador
from Software_FJ.controllers.ServicioControlador import ServicioControlador
from Software_FJ.models.AlquilerEquipo import AlquilerEquipo
from Software_FJ.models.AsesoriaEspecializada import AsesoriaEspecializada
from Software_FJ.models.ReservaSala import ReservarSala
from Software_FJ.services.ClienteService import ClienteService
from Software_FJ.services.ReservaService import ReservaService
from Software_FJ.services.ServicioService import ServicioService


class AplicacionSoftwareFJ(tk.Tk):
    """Interfaz visual de escritorio para el sistema Software FJ."""

    def __init__(self):
        super().__init__()
        self.title("Software FJ - Gestión de clientes, servicios y reservas")
        self.geometry("1050x680")
        self.minsize(900, 600)

        self.clientes = ClienteService()
        self.servicios = ServicioService()
        self.reservas = ReservaService(self.clientes, self.servicios)
        self.cliente_ctl = ClienteControlador(self.clientes)
        self.servicio_ctl = ServicioControlador(self.servicios)
        self.reserva_ctl = ReservaControlador(self.reservas)

        # Aporte de Edwin Arley Duarte Escobar: los controladores reciben los
        # servicios por inyección para mantener la vista independiente del dominio.
        self._configurar_estilos()
        self._construir_interfaz()
        self._cargar_servicios_iniciales()
        self._actualizar_todo()

    def _configurar_estilos(self):
        estilo = ttk.Style(self)
        try:
            estilo.theme_use("clam")
        except tk.TclError:
            pass
        estilo.configure("Titulo.TLabel", font=("Arial", 16, "bold"), foreground="#124e78")
        estilo.configure("Subtitulo.TLabel", font=("Arial", 11, "bold"))
        estilo.configure("Accion.TButton", padding=6)

    def _construir_interfaz(self):
        encabezado = ttk.Frame(self, padding=(16, 12, 16, 4))
        encabezado.pack(fill="x")
        ttk.Label(encabezado, text="Sistema Integral Software FJ", style="Titulo.TLabel").pack(anchor="w")
        ttk.Label(encabezado, text="Gestión en memoria: clientes, servicios especializados y reservas").pack(anchor="w")

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=12, pady=8)
        self._crear_pestana_clientes()
        self._crear_pestana_servicios()
        self._crear_pestana_reservas()
        self._crear_pestana_eventos()

        self.estado = tk.StringVar(value="Listo")
        ttk.Label(self, textvariable=self.estado, relief="sunken", anchor="w", padding=4).pack(fill="x", side="bottom")

    def _crear_pestana_clientes(self):
        pestaña = ttk.Frame(self.notebook, padding=12)
        self.notebook.add(pestaña, text="Clientes")
        formulario = ttk.LabelFrame(pestaña, text="Registrar cliente", padding=10)
        formulario.pack(fill="x")
        self.cliente_vars = {campo: tk.StringVar() for campo in ("nombre", "documento", "correo", "telefono")}
        for columna, (campo, variable) in enumerate(self.cliente_vars.items()):
            ttk.Label(formulario, text=campo.capitalize() + ":").grid(row=0, column=columna, padx=5, sticky="w")
            ttk.Entry(formulario, textvariable=variable, width=22).grid(row=1, column=columna, padx=5, pady=4)
        ttk.Button(formulario, text="Registrar cliente", style="Accion.TButton", command=self._registrar_cliente).grid(row=1, column=4, padx=8)

        self.clientes_tree = self._crear_tree(pestaña, ("id", "nombre", "documento", "correo", "telefono"), (180, 180, 130, 220, 130))

    def _crear_pestana_servicios(self):
        pestaña = ttk.Frame(self.notebook, padding=12)
        self.notebook.add(pestaña, text="Servicios")
        acciones = ttk.Frame(pestaña)
        acciones.pack(fill="x", pady=(0, 8))
        ttk.Button(acciones, text="Cargar servicios de ejemplo", command=self._cargar_servicios_ejemplo).pack(side="left")
        ttk.Button(acciones, text="Actualizar catálogo", command=self._actualizar_servicios).pack(side="left", padx=8)
        self.servicios_tree = self._crear_tree(pestaña, ("id", "tipo", "descripcion", "disponible"), (220, 190, 420, 120))

    def _crear_pestana_reservas(self):
        pestaña = ttk.Frame(self.notebook, padding=12)
        self.notebook.add(pestaña, text="Reservas")
        formulario = ttk.LabelFrame(pestaña, text="Crear reserva", padding=10)
        formulario.pack(fill="x")
        ttk.Label(formulario, text="Cliente:").grid(row=0, column=0, sticky="w", padx=5)
        self.cliente_combo = ttk.Combobox(formulario, state="readonly", width=38)
        self.cliente_combo.grid(row=1, column=0, padx=5, pady=4)
        ttk.Label(formulario, text="Servicio:").grid(row=0, column=1, sticky="w", padx=5)
        self.servicio_combo = ttk.Combobox(formulario, state="readonly", width=48)
        self.servicio_combo.grid(row=1, column=1, padx=5, pady=4)
        ttk.Label(formulario, text="Duración:").grid(row=0, column=2, sticky="w", padx=5)
        self.duracion_var = tk.StringVar(value="1")
        ttk.Entry(formulario, textvariable=self.duracion_var, width=10).grid(row=1, column=2, padx=5, pady=4)
        ttk.Button(formulario, text="Crear reserva", command=self._crear_reserva).grid(row=1, column=3, padx=8)

        acciones = ttk.Frame(pestaña)
        acciones.pack(fill="x", pady=8)
        ttk.Button(acciones, text="Confirmar seleccionada", command=self._confirmar_reserva).pack(side="left")
        ttk.Button(acciones, text="Cancelar seleccionada", command=self._cancelar_reserva).pack(side="left", padx=8)
        ttk.Button(acciones, text="Actualizar", command=self._actualizar_reservas).pack(side="left")
        self.reservas_tree = self._crear_tree(pestaña, ("id", "cliente", "servicio", "duracion", "estado", "total"), (220, 170, 220, 90, 120, 100))

    def _crear_pestana_eventos(self):
        pestaña = ttk.Frame(self.notebook, padding=12)
        self.notebook.add(pestaña, text="Eventos y errores")
        ttk.Label(pestaña, text="Registro generado por los servicios y controladores", style="Subtitulo.TLabel").pack(anchor="w")
        self.log_text = tk.Text(pestaña, height=25, state="disabled", wrap="none")
        self.log_text.pack(fill="both", expand=True, pady=8)
        ttk.Button(pestaña, text="Actualizar logs", command=self._actualizar_logs).pack(anchor="e")

    def _crear_tree(self, contenedor, columnas, anchos):
        marco = ttk.Frame(contenedor)
        marco.pack(fill="both", expand=True, pady=(10, 0))
        tree = ttk.Treeview(marco, columns=columnas, show="headings", selectmode="browse")
        for columna, ancho in zip(columnas, anchos):
            tree.heading(columna, text=columna.capitalize())
            tree.column(columna, width=ancho, anchor="w")
        scroll = ttk.Scrollbar(marco, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scroll.set)
        tree.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")
        return tree

    def _cargar_servicios_iniciales(self):
        if not self.servicios.listar():
            self._cargar_servicios_ejemplo()

    def _cargar_servicios_ejemplo(self):
        ejemplos = [
            AlquilerEquipo("Cámara profesional", "Equipo audiovisual", 100, True, "Cámara", 50, 2),
            ReservarSala("Sala grande", "Sala para reuniones", 80, True, 20, "Grande", 40),
            AsesoriaEspecializada("Asesoría Python", "Acompañamiento técnico", 50, True, "Desarrollo", 75, 2),
        ]
        agregados = 0
        for servicio in ejemplos:
            if not any(actual.nombre == servicio.nombre for actual in self.servicios.listar()):
                resultado = self.servicio_ctl.registrar(servicio)
                agregados += int(resultado["exito"])
        self.estado.set(f"Catálogo actualizado: {agregados} servicio(s) agregado(s)")
        self._actualizar_todo()

    def _registrar_cliente(self):
        valores = [self.cliente_vars[campo].get().strip() for campo in ("nombre", "documento", "correo", "telefono")]
        resultado = self.cliente_ctl.registrar(*valores)
        self._mostrar_resultado(resultado, "Cliente")
        if resultado["exito"]:
            for variable in self.cliente_vars.values():
                variable.set("")
            self._actualizar_todo()

    def _crear_reserva(self):
        if not self.cliente_combo.get() or not self.servicio_combo.get():
            messagebox.showwarning("Datos incompletos", "Seleccione un cliente y un servicio.")
            return
        try:
            duracion = int(self.duracion_var.get())
        except ValueError:
            messagebox.showerror("Duración inválida", "La duración debe ser un número entero.")
            return
        cliente_id = self.cliente_combo.get().split(" | ", 1)[0]
        servicio_id = self.servicio_combo.get().split(" | ", 1)[0]
        resultado = self.reserva_ctl.crear(cliente_id, servicio_id, duracion)
        self._mostrar_resultado(resultado, "Reserva")
        if resultado["exito"]:
            self._actualizar_reservas()

    def _reserva_seleccionada(self):
        seleccion = self.reservas_tree.selection()
        if not seleccion:
            messagebox.showwarning("Selección requerida", "Seleccione una reserva en la tabla.")
            return None
        return self.reservas_tree.item(seleccion[0], "values")[0]

    def _confirmar_reserva(self):
        id_reserva = self._reserva_seleccionada()
        if id_reserva:
            self._mostrar_resultado(self.reserva_ctl.confirmar(id_reserva), "Reserva")
            self._actualizar_reservas()

    def _cancelar_reserva(self):
        id_reserva = self._reserva_seleccionada()
        if id_reserva:
            self._mostrar_resultado(self.reserva_ctl.cancelar(id_reserva), "Reserva")
            self._actualizar_reservas()

    def _mostrar_resultado(self, resultado, entidad):
        # Aporte de Jose David Sauma Zaretsky: todos los resultados siguen el
        # mismo contrato {exito, datos/error}, evitando que la interfaz se detenga.
        if resultado["exito"]:
            self.estado.set(f"{entidad} procesado correctamente")
            messagebox.showinfo("Operación exitosa", str(resultado.get("datos", "Operación completada")))
        else:
            self.estado.set(f"Error en {entidad.lower()}: {resultado['error']}")
            messagebox.showerror(f"Error en {entidad.lower()}", resultado["error"])
        self._actualizar_logs()

    def _actualizar_todo(self):
        self._actualizar_clientes()
        self._actualizar_servicios()
        self._actualizar_reservas()
        self._actualizar_logs()

    def _actualizar_clientes(self):
        for item in self.clientes_tree.get_children():
            self.clientes_tree.delete(item)
        for cliente in self.clientes.listar():
            datos = cliente.obtenerInformacion()
            self.clientes_tree.insert("", "end", values=(datos["idCliente"], datos["nombre"], datos["documento"], datos["correo"], datos["telefono"]))
        self.cliente_combo["values"] = [f"{c.idCliente} | {c.nombre}" for c in self.clientes.listar()]

    def _actualizar_servicios(self):
        for item in self.servicios_tree.get_children():
            self.servicios_tree.delete(item)
        for servicio in self.servicios.listar():
            self.servicios_tree.insert("", "end", values=(servicio.idServicio, type(servicio).__name__, servicio.describirServicio(), "Sí" if servicio.disponible else "No"))
        self.servicio_combo["values"] = [f"{s.idServicio} | {s.nombre}" for s in self.servicios.listar(True)]

    def _actualizar_reservas(self):
        for item in self.reservas_tree.get_children():
            self.reservas_tree.delete(item)
        for reserva in self.reservas.listar():
            self.reservas_tree.insert("", "end", values=(reserva.idReserva, reserva.cliente.nombre, reserva.servicio.nombre, reserva.duracion, reserva.estado, reserva.costoTotal))

    def _actualizar_logs(self):
        self.log_text.configure(state="normal")
        self.log_text.delete("1.0", "end")
        self.log_text.insert("1.0", self.reservas.logger.consultarLogs())
        self.log_text.configure(state="disabled")


if __name__ == "__main__":
    app = AplicacionSoftwareFJ()
    app.mainloop()

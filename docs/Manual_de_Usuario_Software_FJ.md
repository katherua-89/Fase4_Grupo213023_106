# Manual de usuario — Software FJ

**Sistema integral de gestión de clientes, servicios y reservas**

Programación 213023 · Grupo 213023_106 · Fase 4

**Integrantes:** Jose David Sauma Zaretsky · Edwin Arley Duarte Escobar · Katerin Marcela Rua Sanchez

---

## 1. Descripción general

Software FJ es una aplicación de escritorio desarrollada en Python con interfaz gráfica Tkinter. Permite registrar clientes, administrar un catálogo de servicios y crear reservas, sin utilizar ningún motor de base de datos: toda la información vive en memoria durante la ejecución y los eventos relevantes se guardan en un archivo de texto.

La aplicación está organizada en cuatro pestañas: **Clientes**, **Servicios**, **Reservas** y **Eventos y errores**. Cada operación se valida antes de ejecutarse; si algo es incorrecto, el sistema muestra un mensaje claro, registra el error y continúa funcionando.

## 2. Requisitos

| Elemento | Requisito |
|---|---|
| Sistema operativo | Windows, macOS o Linux con entorno gráfico |
| Python | 3.10 o superior |
| Tkinter | Incluido en la instalación estándar de Python |
| Dependencias externas | Ninguna |

En Ubuntu o Debian, si Tkinter no está disponible, se instala con:

```bash
sudo apt-get install python3-tk
```

## 3. Instalación y ejecución

1. Descargue o clone el repositorio.
2. Abra una terminal en la carpeta raíz del proyecto, es decir, la carpeta que contiene `Software_FJ`.
3. Ejecute la aplicación:

```bash
python3 -m Software_FJ.main
```

En Windows puede usar `python` en lugar de `python3`.

Al iniciar, la ventana se abre con el catálogo de servicios de ejemplo ya cargado, de modo que pueda probar una reserva de inmediato.

## 4. Estructura de la ventana

La ventana principal tiene tres zonas:

- **Encabezado**: nombre del sistema y descripción breve.
- **Área de pestañas**: contiene las cuatro secciones de trabajo.
- **Barra de estado** (parte inferior): indica el resultado de la última operación realizada.

Cada acción que modifica datos abre un cuadro de diálogo de confirmación o de error y actualiza las tablas automáticamente.

## 5. Pestaña Clientes

### 5.1 Registrar un cliente

1. Abra la pestaña **Clientes**.
2. Complete los cuatro campos: **Nombre**, **Documento**, **Correo** y **Teléfono**.
3. Pulse **Registrar cliente**.

Si los datos son válidos, el cliente aparece en la tabla inferior y los campos se limpian. Si hay un error, se muestra el motivo y el formulario conserva lo escrito para corregirlo.

### 5.2 Reglas de validación

| Campo | Regla |
|---|---|
| Nombre | Mínimo 3 caracteres, sin espacios vacíos al inicio o al final |
| Documento | Mínimo 6 caracteres y no puede repetirse en otro cliente |
| Correo | Mínimo 5 caracteres y debe contener el símbolo `@` |
| Teléfono | Mínimo 7 caracteres |

Todos los campos son obligatorios y deben ser texto.

### 5.3 Tabla de clientes

Muestra el identificador generado (formato `CLI-ENT-...`), el nombre, el documento, el correo y el teléfono de cada cliente registrado.

## 6. Pestaña Servicios

### 6.1 Catálogo disponible

Al iniciar se cargan tres servicios de ejemplo:

| Servicio | Tipo | Datos principales |
|---|---|---|
| Cámara profesional | Alquiler de equipo | 100 de precio base + 50 por día |
| Sala grande | Reserva de sala | Capacidad 20, 80 de precio base + 40 por hora |
| Asesoría Python | Asesoría especializada | 50 de precio base + 75 por hora, 2 horas |

### 6.2 Acciones disponibles

- **Cargar servicios de ejemplo**: agrega los tres servicios anteriores si aún no existen.
- **Actualizar catálogo**: vuelve a leer el catálogo en memoria y refresca la tabla.

La tabla muestra el identificador (`SER-...`), el tipo de servicio, su descripción completa y si está disponible.

### 6.3 Reglas de validación de servicios

**Alquiler de equipo**: el tipo debe ser Cámara, Proyector o Micrófono; el costo por día debe ser mayor que cero y la cantidad debe ser un entero positivo.

**Reserva de sala**: el tipo debe ser Pequeña, Mediana o Grande; la capacidad y el costo por hora deben ser mayores que cero.

**Asesoría especializada**: la especialidad no puede estar vacía; el costo por hora y la cantidad de horas deben ser mayores que cero.

En todos los casos, el nombre y la descripción son obligatorios, el precio base no puede ser negativo y el campo de disponibilidad debe ser verdadero o falso.

## 7. Pestaña Reservas

### 7.1 Crear una reserva

1. Abra la pestaña **Reservas**.
2. En **Cliente**, seleccione uno de la lista (solo aparecen clientes registrados).
3. En **Servicio**, seleccione uno de los servicios disponibles.
4. Escriba la **Duración** como número entero positivo: días para alquiler de equipos, horas para salas y asesorías.
5. Pulse **Crear reserva**.

La reserva se crea en estado **PENDIENTE** y el costo total se calcula con la fórmula del servicio elegido.

### 7.2 Confirmar o cancelar

1. Seleccione una fila de la tabla de reservas.
2. Pulse **Confirmar seleccionada** para pasar la reserva a estado **CONFIRMADA**.
3. Pulse **Cancelar seleccionada** para pasarla a estado **CANCELADA**.

Una reserva ya confirmada no puede cancelarse; el sistema informa la restricción mediante un mensaje y registra el intento en el archivo de logs.

### 7.3 Tabla de reservas

Muestra el identificador (`RES-...`), el cliente, el servicio, la duración, el estado actual y el costo total calculado.

### 7.4 Cálculo del costo

| Servicio | Fórmula |
|---|---|
| Alquiler de equipo | Precio base + costo por día × duración |
| Reserva de sala | Precio base + costo por hora × duración |
| Asesoría especializada | Precio base + costo por hora × horas |

El cálculo admite de forma opcional un descuento y un impuesto expresados en porcentaje, que se aplican sobre el valor base.

## 8. Pestaña Eventos y errores

Esta pestaña muestra el contenido del archivo de logs generado por la aplicación. Cada línea incluye fecha y hora, nivel del registro, tipo, acción y descripción.

Ejemplo de un registro:

```text
2026-11-22 18:02:58 | ERROR | ValueError | REGISTRAR_SERVICIO | Los costos no son válidos
```

Pulse **Actualizar logs** después de realizar operaciones para ver los nuevos registros. El archivo se guarda en:

```text
logs/software_fj.log
```

## 9. Mensajes frecuentes y cómo resolverlos

| Mensaje | Causa | Solución |
|---|---|---|
| El nombre debe tener al menos 3 caracteres | Nombre demasiado corto | Escriba el nombre completo |
| El documento debe tener al menos 6 caracteres | Documento incompleto | Verifique el número de documento |
| El correo debe contener un '@' | Correo mal formado | Corrija el correo |
| Ya existe un cliente con ese documento | Documento duplicado | Use otro documento o consulte el cliente existente |
| Los costos no son válidos | Precio base negativo o tarifa en cero | Corrija los valores del servicio |
| Los parámetros del equipo no son válidos | Tipo de equipo o cantidad incorrectos | Use Cámara, Proyector o Micrófono y una cantidad positiva |
| El servicio no está disponible | Servicio marcado como no disponible | Elija otro servicio del catálogo |
| La duración debe ser un entero mayor a 0 | Duración vacía, negativa o con decimales | Escriba un número entero positivo |
| No se puede cancelar una reserva confirmada | Intento de cancelar una reserva ya confirmada | Cree una reserva nueva si necesita otro estado |
| Seleccione una reserva en la tabla | No hay fila seleccionada | Haga clic sobre la reserva antes de confirmar o cancelar |
| Seleccione un cliente y un servicio | Faltan datos en el formulario | Complete ambas listas desplegables |

## 10. Preguntas frecuentes

**¿La información se conserva al cerrar la aplicación?**
No. Los datos viven en memoria y se pierden al cerrar la ventana; solo el archivo de logs permanece en disco.

**¿Puedo registrar un servicio con un tipo distinto a los permitidos?**
No. El sistema valida los tipos admitidos para cada clase de servicio y rechaza los valores no reconocidos.

**¿Qué ocurre si una operación falla?**
El controlador captura la excepción, la registra en el archivo de logs y devuelve un resultado con `exito=False`. La ventana permanece abierta y lista para la siguiente operación.

**¿Puedo modificar un cliente ya registrado?**
Sí, a través de la capa de servicios se pueden actualizar el correo y el teléfono, aplicando las mismas validaciones del registro.

**¿La aplicación necesita internet?**
No. Funciona completamente sin conexión y sin base de datos.

## 11. Cierre recomendado de una sesión de prueba

1. Registrar dos clientes, uno válido y uno con datos incorrectos.
2. Revisar el catálogo de servicios y verificar la disponibilidad.
3. Crear una reserva, confirmarla y observar el costo total.
4. Intentar cancelar la reserva confirmada para comprobar el mensaje de restricción.
5. Abrir la pestaña **Eventos y errores** y verificar que las operaciones anteriores quedaron registradas.

Con este recorrido se comprueba el funcionamiento de los tres módulos, el manejo de excepciones y el registro de eventos del sistema.

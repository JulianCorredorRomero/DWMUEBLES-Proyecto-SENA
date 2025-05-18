# Historias de Usuario - Proyecto DWMUEBLES

---

## HU-01 - Registro de usuarios con diferentes roles

**Como** administrador,  
**quiero** registrar nuevos usuarios con roles específicos (asesor de ventas, carpintero, administrador, cliente),  
**para que** cada uno acceda solo a las funcionalidades correspondientes.

### Criterios de Aceptación
- El formulario solicita nombre, correo, contraseña y selección de rol.
- El correo debe ser único y validado.
- El sistema asigna permisos según el rol.
- Se envía un correo de confirmación tras el registro.
- El usuario puede iniciar sesión y ver su entorno según el rol.

---

## HU-02 - Autenticación de usuarios

**Como** usuario registrado,  
**quiero** iniciar sesión con mis credenciales,  
**para acceder** a las funcionalidades de mi rol.

### Criterios de Aceptación
- El sistema muestra formulario de inicio de sesión.
- Se validan las credenciales frente a la base de datos.
- Si son correctas, se redirige al área correspondiente.
- Si son incorrectas, se muestra un mensaje de error.
- Las contraseñas están encriptadas.
- Se puede recuperar la contraseña vía correo.
- Tras varios intentos fallidos, la cuenta se bloquea y se notifica por correo.

---
# Historias de Usuario - Proyecto DWMUEBLES

---

## HU-03 - Registro de ventas de muebles al contado

**Como** asesor de ventas,  
**quiero** poder registrar las ventas de muebles al contado,  
**para** procesar transacciones rápidas y efectivas y proporcionar un recibo a los clientes.

### Criterios de Aceptación
1. **Captura de Detalles de la Venta**  
   - El sistema debe proporcionar un formulario para capturar los detalles de la venta: productos vendidos, cantidad, precio y total.
2. **Actualización del Inventario**  
   - El sistema debe actualizar el inventario en tiempo real para reflejar la venta realizada.  
   - La cantidad de productos vendidos debe descontarse automáticamente del stock disponible.
3. **Generación de Recibo**  
   - El sistema debe generar un recibo con productos vendidos, cantidad, precio, total y fecha.
4. **Envío del Recibo**  
   - El recibo debe enviarse automáticamente al correo electrónico del cliente en formato PDF.
5. **Seguridad y Precisión**  
   - Los datos deben almacenarse de forma segura y precisa.  
   - El sistema debe operar sin demoras perceptibles.

### Notas
- El sistema debe ser intuitivo para los asesores de ventas.
- La integración con el inventario debe garantizar actualización en tiempo real.
- La experiencia del usuario y la seguridad de la información son prioridades clave.

---

## HU-04 - Registro de ventas de muebles a crédito

**Como** asesor de ventas,  
**quiero** poder registrar las ventas de muebles a crédito,  
**para** ofrecer opciones de financiamiento a los clientes y aumentar las ventas.

### Criterios de Aceptación
1. **Captura de Detalles de la Venta**  
   - Formulario para registrar productos, cantidad, precio, total y términos de crédito.
2. **Creación de Plan de Pagos**  
   - El sistema permite configurar fechas y montos de cada cuota.
3. **Actualización del Inventario**  
   - Descuento automático del stock disponible al registrar la venta.
4. **Generación y Envío de Recibo**  
   - Generación de un recibo con productos, precio, total, términos de crédito y fecha.  
   - Envío del recibo inicial en formato PDF por correo electrónico al cliente.
5. **Envío del Plan de Pagos**  
   - Envío automático del plan de pagos en PDF por correo electrónico al cliente.
6. **Seguridad y Precisión**  
   - Los datos deben almacenarse de forma segura y precisa.  
   - El sistema debe ser rápido para evitar demoras.

### Notas
- Interfaz amigable para asesores de ventas.
- Integración fluida con inventario en tiempo real.
- Seguridad de datos y experiencia del usuario como pilares.
- Integración con el módulo de gestión de pagos para hacer seguimiento de cuotas.

---

## HU-05 - Gestión eficiente del inventario

**Como** administrador de inventario,  
**quiero** que el sistema mantenga un inventario actualizado de los productos,  
**para** asegurar disponibilidad, planificar la producción y tomar decisiones informadas.

### Criterios de Aceptación
1. **Registro de Entradas y Salidas**  
   - Posibilidad de registrar entradas/salidas con cantidad, fecha y motivo.
2. **Actualización en Tiempo Real**  
   - El inventario debe reflejar automáticamente cada movimiento en todas las ubicaciones.
3. **Alertas de Inventario Bajo**  
   - Generación automática de alertas cuando un producto está por debajo del mínimo.  
   - Notificación al administrador de inventario y jefe de producción.
4. **Múltiples Ubicaciones de Inventario**  
   - Gestión de inventarios en diferentes sedes (almacenes, sucursales).  
   - Posibilidad de consultar y consolidar datos entre ubicaciones.
5. **Integridad y Precisión de los Datos**  
   - Mecanismos para garantizar precisión y proteger los datos.  
   - Inclusión de validaciones y corrección de errores.
6. **Auditoría del Inventario**  
   - Capacidad para generar informes, identificar discrepancias y revisar historial de cambios.

### Notas
- Los asesores y el jefe de producción deben tener acceso a la información actualizada.
- Los administradores gestionan parámetros clave, como umbrales de alerta.

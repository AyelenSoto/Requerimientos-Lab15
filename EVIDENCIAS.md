# Paso 5 – Cierre y reflexión

## ¿Qué aprendimos sobre separar configuración y código?
Separar la configuración del código permite ajustar el comportamiento de la aplicación sin necesidad de alterar la lógica interna. Esto facilita el mantenimiento, reduce errores y permite manejar diferentes entornos (desarrollo, prueba y producción) sin modificar el código fuente. También evita mezclar parámetros sensibles o temporales dentro del programa.

## ¿Qué pasaría si la producción usa parámetros equivocados?
Si en producción se cargan parámetros incorrectos, podrían activarse funciones no preparadas para ese entorno, habilitar el modo debug (exponiendo detalles internos), disminuir el rendimiento por un nivel de logs demasiado detallado o incluso comprometer la seguridad. Por eso es clave validar cada archivo de configuración antes de desplegar.

## ¿Cómo ayuda Git a mantener el orden del proyecto?
Git permite crear un historial organizado de cambios, trabajar con ramas para nuevas funcionalidades sin tocar la versión estable, realizar merges controlados y evitar pérdida de versiones. Esto ordena el desarrollo, facilita la colaboración y permite rastrear cualquier modificación del proyecto.

---

# Checklist del laboratorio

- ☑ **Archivos .ini correctos.**  
  (config_dev.ini, config_test.ini, config_prod.ini creados y configurados)

- ☑ **Código que selecciona entorno según APP_ENV.**  
  (app.py usa APP_ENV para elegir la configuración)

- ☑ **Rama de cambio creada y mergeada.**  
  (feature/versionado creada, desarrollada y fusionada en main)

- ☑ **CHANGELOG.md con 2 versiones.**  
  (0.1.0 inicial y 0.2.0 con mejoras)

- ☑ **Evidencias completas.**  
  (salidas de los tres entornos agregadas en este mismo archivo)

- ☑ **Reflexión final.**  
  (sección incluida arriba)

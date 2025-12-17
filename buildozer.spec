[app]

# Nombre de la aplicación
title = El Mariano

# Nombre del paquete (NO usar mayúsculas)
package.name = elmariano
package.domain = org.mariano

# Archivo principal
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,yaml

# Versión
version = 1.0

# Requerimientos Python
# NO agregar python-for-android acá
requirements = python3,kivy,requests,pyyaml

# Archivo de entrada
entrypoint = main.py

# Orientación
orientation = portrait

# Pantalla completa
fullscreen = 1

# Permisos Android
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# ===== ANDROID =====

# API y SDK (ESTO ES CLAVE)
android.api = 33
android.minapi = 21
android.sdk = 24
android.ndk = 25b

# Rama estable de python-for-android
p4a.branch = v2023.09.24

# Arquitecturas soportadas
android.archs = arm64-v8a,armeabi-v7a

# Aceptar licencias automáticamente
android.accept_sdk_license = True

# Evita errores de compilación
android.enable_androidx = True

# Logs útiles
log_level = 2

# ===== BUILD =====

# No usar gradle propio
android.gradle_dependencies =

# Optimización
android.release_artifact = apk

# Limpieza automática
android.clean_intermediate = True

# ===== DEBUG =====

# Mantener consola activa
android.debuggable = True

# ===== FIN =====

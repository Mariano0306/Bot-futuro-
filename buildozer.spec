[app]

# Nombre visible de la app
title = Dale que hacés platita

# Nombre del paquete (NO cambiar después de publicar)
package.name = dalequehacesplatita
package.domain = org.mariano

# Archivo principal
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,txt,yaml

# Versión
version = 1.0

# Requerimientos Python
requirements = python3,kivy,requests,pyyaml

# Pantalla
orientation = portrait
fullscreen = 0

# Icono (si no tenés, comentá la línea)
# icon.filename = %(source.dir)s/icon.png

# Splash (opcional)
# presplash.filename = %(source.dir)s/splash.png


[buildozer]

log_level = 2
warn_on_root = 1


[android]

# API recomendada y estable
android.api = 31
android.minapi = 21

# Arquitecturas
android.arch = armeabi-v7a, arm64-v8a

# Fuerza uso de AndroidX
android.use_androidx = True

# PERMISOS (agregá más si necesitás)
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# === SOLUCIÓN AL ERROR DEL 15% / libffi ===
android.environment = USE_SYSTEM_LIBFFI=1

# Versión estable de python-for-android
p4a.branch = v2023.09.24

# No usar recetas locales
p4a.local_recipes =

# Limpieza controlada
android.skip_update = False

# Logs completos
android.logcat_filters = *:S python:D

# Java
android.gradle_dependencies =
android.enable_r8 = True


[graphics]

# DPI adaptable
resizable = 1


[input]

mouse = mouse

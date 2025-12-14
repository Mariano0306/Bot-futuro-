[app]
# Nombre visible de la app
title = El Mariano

# Nombre interno del paquete
package.name = elmariano
package.domain = org.mariano

# Carpeta donde está main.py
source.dir = .

# Extensiones que se incluyen en el paquete
source.include_exts = py,kv,png,jpg,jpeg,svg,ttf,otf,wav,ogg,mp3

# Versión de la app
version = 0.1

# Módulos Python que se empacan dentro de la app
# (ajusta si tienes más dependencias)
requirements = python3,kivy,kivy_garden.mapview,requests

# Orientación principal de la app (cámbiala si la quieres vertical)
orientation = landscape

# Pantalla completa
fullscreen = 1

# Plataformas/targets
osx.python_version = 3
osx.kivy_version = 2.3.0

# Configuración Android
android.api = 31
android.minapi = 21
android.archs = arm64-v8a,armeabi-v7a
android.accept_sdk_license = True

# Permisos necesarios para GPS y red
android.permissions = INTERNET,ACCESS_NETWORK_STATE,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Icono (opcional) – pon el path si ya tienes uno
# icon.filename = %(source.dir)s/icon.png


[buildozer]
# Nivel de log detallado para ver bien los errores
log_level = 2

# Carpeta donde se guardan los archivos temporales de buildozer
build_dir = .buildozer

# Evitar errores si se ejecuta como root (no es el caso en GitHub, pero no molesta)
warn_on_root = 1

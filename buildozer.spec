[app]
# Nombre que se verá en el teléfono
title = El Mariano

# Nombre interno del paquete
package.name = elmariano
package.domain = org.mariano

# Directorio donde está tu main.py (la raíz del repo)
source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,svg,ttf,otf,wav,ogg,mp3

# Versión de la app
version = 0.1

# Requisitos de Python para una app Kivy sencilla
requirements = python3,kivy

# Archivo principal de tu app
source.main = main.py

# Orientación
orientation = landscape

# Pantalla completa
fullscreen = 1

# Nivel de log (2 = más detallado, útil para ver el error real)
log_level = 2

# Icono (si no tenés, esto se ignora)
#icon.filename = %(source.dir)s/icon.png

# --------- CONFIG ANDROID ----------
[buildozer]
log_level = 2

[app:android]
# API objetivo
android.api = 33
android.minapi = 21

# NDK que está bajando Buildozer en tu log
android.ndk = 25b
android.ndk_api = 21

# Arquitecturas que soporta tu APK
android.archs = arm64-v8a, armeabi-v7a

# Para usar gradle (es lo estándar hoy)
android.build_type = gradle

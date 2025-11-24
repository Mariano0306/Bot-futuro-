[app]
# Nombre visible de la app
title = El Mariano

# Nombre interno de paquete
package.name = elmariano
package.domain = org.mariano

# Carpeta donde está main.py
source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,svg,ttf,otf,wav,ogg,mp3

# Versión
version = 0.1

# LIBRERÍAS QUE USA TU main.py
requirements = python3,kivy,kivy_garden.mapview,plyer

# Archivo principal
source.main = main.py

# Orientación horizontal
orientation = landscape

# Pantalla completa
fullscreen = 1

# Permisos Android (GPS + internet para los mapas)
android.permissions = INTERNET,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION

# Nivel de log (útil para ver errores reales)
log_level = 2


[buildozer]
log_level = 2


[app:android]
# API y NDK (lo que ya estaba usando tu build)
android.api = 33
android.minapi = 21

android.ndk = 25b
android.ndk_api = 21

# Arquitecturas soportadas
android.archs = arm64-v8a, armeabi-v7a

# Usar Gradle
android.build_type = gradle

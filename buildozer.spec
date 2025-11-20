[app]
# Nombre que va a ver el usuario
title = El Mariano

# Nombre interno del paquete
package.name = elmariano
package.domain = org.agro

# Carpeta donde está tu main.py
source.dir = .

# Extensiones de archivos que se incluyen en el APK
source.include_exts = py,png,jpg,kv,atlas

# Versión de la app
version = 1.0

# Módulos de Python que se van a compilar dentro del APK
requirements = python3,kivy,plyer,kivy_garden.mapview,certifi,requests
garden_requirements = mapview

# Rama de python-for-android
p4a.branch = master

# Orientación de la pantalla
orientation = landscape

# 0 = no forzar fullscreen (barra de estado visible)
fullscreen = 0

# Permisos Android que usa la app
android.permissions = ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,INTERNET,ACCESS_NETWORK_STATE

# Aceptar automáticamente las licencias del SDK de Android
android.accept_sdk_license = 1

# API objetivo (la que instalamos en el workflow: android-33)
android.api = 33
# API mínima soportada
android.minapi = 21

# Arquitecturas
android.archs = armeabi-v7a,arm64-v8a


[buildozer]
# Nivel de log
log_level = 2

# Avisar si se corre como root
warn_on_root = 1

# Carpeta donde buildozer guarda los archivos temporales
build_dir = .buildozer

# Carpeta donde se guardan los APK generados
bin_dir = bin

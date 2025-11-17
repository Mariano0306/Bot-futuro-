[app]
title = El Mariano
package.name = elmariano
package.domain = org.agro

# Código de la app
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Versión de la app
version = 1.0.0
android.version_code = 1

# Dependencias de Python
requirements = python3,kivy,plyer,kivy_garden.mapview,certifi,requests
garden_requirements = mapview

# Rama de python-for-android
p4a.branch = master

# Orientación y pantalla
orientation = landscape
fullscreen = 0

# Permisos Android
android.permissions = ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,INTERNET,ACCESS_NETWORK_STATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Config Android (APIs)
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 23b
android.ndk_api = 21
android.archs = armeabi-v7a,arm64-v8a

# Otras opciones útiles
android.enable_androidx = True
android.private_storage = True
android.allow_backup = False

[buildozer]
log_level = 2
warn_on_root = 1
build_dir = .buildozer
bin_dir = bin

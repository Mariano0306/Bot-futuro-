[app]
title = El Mariano
package.name = elmariano
package.domain = org.mariano

# carpeta raíz del proyecto
source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,svg,ttf,otf,wav,ogg,mp3

version = 0.1

# librerías usadas por main.py
requirements = python3,kivy,kivy_garden.mapview,plyer

# archivo principal
source.main = main.py

orientation = landscape
fullscreen = 1

android.permissions = INTERNET,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION

# para que el log sea más detallado
log_level = 2


[buildozer]
log_level = 2
# desactiva el aviso de root (pero lo importante es la env var del workflow)
warn_on_root = 0


[app:android]
android.api = 33
android.minapi = 21

android.ndk = 25b
android.ndk_api = 21

android.archs = arm64-v8a, armeabi-v7a

android.build_type = gradle

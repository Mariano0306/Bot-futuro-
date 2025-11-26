[app]
title = El Mariano
package.name = elmariano
package.domain = org.mariano

# Carpeta del proyecto
source.dir = .
source.include_exts = py, kv, png, jpg, jpeg, svg, ttf, otf, wav, ogg, mp3
source.main = main.py

# Versión de la app
version = 0.1

# Requisitos con versiones correctas para Android
requirements = python3==3.10.5, kivy==2.1.0, kivy_garden.mapview, plyer

orientation = landscape
fullscreen = 1

# Permisos Android
android.permissions = INTERNET, ACCESS_FINE_LOCATION, ACCESS_COARSE_LOCATION

# Nivel de logs
log_level = 2


[buildozer]
log_level = 2
warn_on_root = 1


[app:android]
# API/NDK compatibles con Buildozer actual
android.api = 33
android.minapi = 21

android.ndk = 25b
android.ndk_api = 21

# Arquitecturas soportadas
android.archs = arm64-v8a, armeabi-v7a

# Usar Gradle (obligatorio en 2024/2025)
android.build_type = gradle

# Evita errores de licencia del SDK
android.accept_sdk_license = True
android.accept_android_sdk_license = True

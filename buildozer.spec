[app]

title = Bot Futuro
package.name = botfuturo
package.domain = org.mariano

source.dir = .
source.include_exts = py,png,jpg,kv,txt

version = 0.1

requirements = python3==3.10.12,kivy==2.2.1

orientation = portrait

fullscreen = 0

icon.filename = icon.png
presplash.filename = presplash.png

log_level = 2

# Entry point
entrypoint = main.py


[buildozer]

log_level = 2
warn_on_root = 0


[app.android]

# API estable
android.api = 31
android.minapi = 21

# Arquitecturas
android.archs = arm64-v8a,armeabi-v7a

# SDK / NDK compatibles
android.ndk = 25b
android.sdk = 31

# Java
android.gradle_dependencies =

# Permisos mínimos
android.permissions = INTERNET

# Evita errores de p4a
android.allow_backup = True
android.private_storage = True

# Fuerza descarga limpia de p4a
p4a.branch = develop
p4a.bootstrap = sdl2

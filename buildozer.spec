[app]
# Nombre que verá el usuario
title = El Mariano

# Nombre interno del paquete
package.name = elmariano
package.domain = org.mariano

# Directorio del código fuente
source.dir = .

# Extensiones que se incluyen en el APK
source.include_exts = py,kv,png,jpg,atlas

# Archivo principal de tu app
# (tu proyecto tiene main.py en la raíz)
main.py = main.py

# Orientación de la app (landscape / portrait / all)
orientation = landscape

# Pantalla completa
fullscreen = 1

# Versión de la app (la puedes ir cambiando)
version = 0.1

# Módulos de Python a incluir
requirements = python3,kivy,plyer,requests

# Arquitecturas Android a compilar
android.archs = armeabi-v7a, arm64-v8a

# API / SDK / NDK que usaremos
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b

# Aceptar licencias del SDK automáticamente
android.accept_sdk_license = True

# Permisos que necesita tu app (puedes ajustar después)
android.permissions = INTERNET,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Icono (lo podemos ajustar más adelante si quieres)
# icon.filename = %(source.dir)s/data/icon.png


[buildozer]
# Nivel de log (1 = mínimo, 2 = normal, 3 = verbose)
log_level = 2

# No mostrar warnings por compilar como root
warn_on_root = 1

# Directorio de binarios donde va a dejar el APK
bin_dir = bin

# Carpeta donde guarda el estado de buildozer
build_dir = .buildozer

[app]

# =========================
# Información básica
# =========================
title = Bot Futuro
package.name = botfuturo
package.domain = org.mariano

source.dir = .
source.include_exts = py,png,jpg,kv,json,yaml

version = 0.1

# Archivo principal
entrypoint = main.py

# Icono (ya lo tenés)
icon.filename = icon.png

# =========================
# Requisitos Python
# =========================
requirements = python3,kivy

# Forzar rama estable de python-for-android
p4a.branch = stable

# =========================
# Permisos Android
# =========================
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# =========================
# Configuración ANDROID (CLAVE)
# =========================

# SOLO UNA arquitectura (evita cuelgues)
android.arch = arm64-v8a

# APIs compatibles y probadas
android.api = 33
android.minapi = 21

# NDK estable (evita errores AIDL)
android.ndk = 25.2.9519653

# Evitar rebuilds innecesarios
android.skip_update = True

# No compilar tests de Python
android.enable_androidx = True

# =========================
# Orientación y UI
# =========================
orientation = portrait
fullscreen = 0

# =========================
# Logging
# =========================
log_level = 2

# =========================
# Buildozer
# =========================
warn_on_root = 1

# =========================
# Extras (seguridad)
# =========================
android.allow_backup = False

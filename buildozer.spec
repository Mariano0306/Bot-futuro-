[app]
title = El Mariano
package.name = elmariano
package.domain = org.agro
source.dir = .
source.include_exts = py,png,jpg,kv
version = 1.0

# Dependencias de Python/Kivy
requirements = python3,kivy,requests

# Modo de pantalla (para banderillero es mejor horizontal)
orientation = landscape
fullscreen = 0

# Permisos Android (GPS + Internet para mapas)
android.permissions = ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,INTERNET,ACCESS_NETWORK_STATE

# Icono y pantalla de inicio (opcionales, se pueden agregar después)
# icon.filename = icon.png
# presplash.filename = presplash.png

[buildozer]
log_level = 2
warn_on_root = 1
build_dir = .buildozer

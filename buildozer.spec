[app]
title = El Mariano
package.name = elmariano
package.domain = org.agro
source.dir = .
source.include_exts = py,png,jpg,kv
version = 1.0

requirements = python3, kivy, plyer, kivy_garden.mapview, certifi, requests
garden_requirements = mapview
p4a.branch = master

orientation = landscape
fullscreen = 0
android.permissions = ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,INTERNET,ACCESS_NETWORK_STATE

# --- AGREGAR ESTO ---
# (SDK que va a usar p4a / buildozer)
android.api = 30
android.minapi = 21
# Fuerza a usar Build-Tools 33.0.2 (que sí trae aidl)
android.build_tools_version = 33.0.2
# --- FIN DE LO NUEVO ---

[buildozer]
log_level = 2
warn_on_root = 1
build_dir = .buildozer

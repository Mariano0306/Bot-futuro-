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
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 0
build_dir = .buildozer

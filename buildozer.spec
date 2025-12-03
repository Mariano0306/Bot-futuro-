[app]
title = El Mariano
package.name = elmariano
package.domain = org.mariano

source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,svg,ttf,otf,wav,ogg,mp3
version = 0.1

requirements = python3,kivy,kivy_garden.mapview,plyer
source.main = main.py

orientation = landscape
fullscreen = 1

android.permissions = INTERNET,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION
log_level = 2


[buildozer]
log_level = 2
allow_root = 1


[app:android]
android.api = 33
android.minapi = 21

android.ndk = 25b
android.ndk_api = 21

android.archs = arm64-v8a, armeabi-v7a
android.build_type = gradle

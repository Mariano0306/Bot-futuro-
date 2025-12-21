[app]
title = Bot Futuro
package.name = botfuturo
package.domain = org.mariano

source.dir = .
source.include_exts = py,png,jpg,kv,json

version = 0.1
requirements = python3,kivy

orientation = portrait
fullscreen = 0

icon.filename = icon.png

android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33

android.archs = arm64-v8a
android.allow_backup = True

android.logcat_filters = *:S python:D

[buildozer]
log_level = 2
warn_on_root = 1

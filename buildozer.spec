[app]

title = Bot Futuro
package.name = botfuturo
package.domain = org.botfuturo

source.dir = .
source.include_exts = py,yaml,json,txt,png

version = 0.1

requirements = python3,kivy,requests,pyyaml

orientation = portrait

fullscreen = 0

icon.filename = icon.png

log_level = 2


[buildozer]

log_level = 2
warn_on_root = 1


[android]

android.api = 21
android.minapi = 21

# NO forzar ndk ni python-for-android
# Esto es CLAVE para que no falle en GitHub Actions

android.archs = arm64-v8a

android.allow_backup = True

android.permissions = INTERNET

android.debuggable = 1

android.gradle_dependencies =

android.accept_sdk_license = True


[graphics]

width = 720
height = 1280

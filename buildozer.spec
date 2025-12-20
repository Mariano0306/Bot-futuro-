[app]

title = Bot Futuro
package.name = botfuturo
package.domain = org.bot.futuro

source.dir = .
source.include_exts = py,png,jpg,kv

version = 0.1

requirements = python3,kivy,requests

orientation = portrait

icon.filename = icon.png

fullscreen = 0


# -------- ANDROID --------

android.api = 33
android.minapi = 21

android.ndk = 25.2.9519653
android.ndk_api = 21

android.archs = arm64-v8a

android.permissions = INTERNET

android.allow_backup = True

android.gradle_dependencies = 

android.enable_androidx = True

android.use_androidx = True

android.accept_sdk_license = True

# 🔴 CLAVE PARA TU ERROR
p4a.branch = stable
p4a.force_build = True
p4a.clean_build = False

log_level = 2

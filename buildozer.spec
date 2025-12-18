[app]

title = El Mariano
package.name = elmariano
package.domain = org.mariano

source.dir = .
source.include_exts = py,png,jpg,kv,json,txt

version = 0.1

requirements = python3==3.10.9,kivy==2.2.1

orientation = portrait
fullscreen = 0

icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/presplash.png

log_level = 2

android.permissions = INTERNET,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION

android.api = 31
android.minapi = 21

android.ndk = 25b
android.ndk_api = 21

android.accept_sdk_license = True

android.archs = arm64-v8a,armeabi-v7a

android.gradle_dependencies =
android.enable_androidx = True

android.private_storage = True

android.allow_backup = True

android.manifest.application_attributes = android:usesCleartextTraffic="true"

android.debuggable = True

android.copy_libs = 1

[buildozer]

log_level = 2
warn_on_root = 1

[python]

use_legacy_setup_py = False

[android]

bootstrap = sdl2
build_tools_version = 34.0.0

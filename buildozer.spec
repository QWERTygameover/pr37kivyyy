[app]
# (str) Title of your application
title = pr37

# (str) Package name
package.name = pr37

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py is located
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Presplash of the application (optional)
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application (optional)
# icon.filename = %(source.dir)s/data/icon.png

# (one of landscape, sensorLandscape, portrait or sensorPortrait)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (int) Android API to use
android.api = 30

# (int) Minimum API for android
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 23b

# (str) Gradle dependencies to add
android.gradle_dependencies = 'com.android.support:multidex:1.0.3'

# (list) Permissions
android.permissions = INTERNET

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D

# (bool) Enable android's logging
log_enable = 1

[app]

# App title
title = 24点游戏求解器

# Package name
package.name = game24solver

# Package domain
package.domain = org.game24

# Source code directory
source.dir = .

# Main file
source.main = game_24_mobile.py

# Source files to include
source.include_exts = py,png,jpg,kv,atlas

# App version
version = 1.0.0

# Requirements
requirements = python3,kivy,hostpython3,cython

# Orientation
orientation = portrait

# Fullscreen
fullscreen = 0

# Android permissions
android.permissions = INTERNET

# Android API level
android.api = 33

# Android minimum API level
android.minapi = 21

# Android NDK version
android.ndk = 25b

# Android SDK version
android.sdk = 33

# Bootstrap
bootstrap = sdl2

# Architecture
android.archs = arm64-v8a, armeabi-v7a

# Icon
icon.filename = %(source.dir)s/icon.png

# Debug mode
debug = 0

# Log level
log_level = 2

# P4A platform
p4a.platform = android

# P4A bootstrap
p4a.bootstrap = sdl2

# P4A requirements
p4a.requirements = python3,kivy

# Android entry point
android.entrypoint = org.kivy.android.PythonActivity

# Android app theme
android.apptheme = "@android:style/Theme.NoTitleBar"
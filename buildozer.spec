[app]
title = تطبيق دمج الخطوط
package.name = font_merger
package.domain = org.example
source.dir = .
version = 0.1
# أضفنا cython لضمان التوافق مع حزم البناء
requirements = python3,kivy,cython,fonttools
android.api = 31
android.minapi = 21
android.archs = armeabi-v7a, arm64-v8a
android.permissions = INTERNET
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

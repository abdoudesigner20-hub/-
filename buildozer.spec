[app]
title = Currency Converter Pro
package.name = currencyconverter
package.domain = org.abdoudesigner
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,mp3
version = 1.0

# المتطلبات (لا تحذف أي واحدة ليعمل التطبيق)
requirements = python3,kivy==2.2.1,requests,urllib3,charset_normalizer,idna,certifi,kivmob,pyjnius,android

orientation = portrait
fullscreen = 0

# الأذونات المطلوبة
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# إعدادات أندرويد 2026
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = armeabi-v7a, arm64-v8a

# ربط إعلانات AdMob
android.gradle_dependencies = 'com.google.android.gms:play-services-ads:22.0.0'

[buildozer]
log_level = 2
warn_on_root = 1


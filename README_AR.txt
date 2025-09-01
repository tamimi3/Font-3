ملف مصحّح لتشغيل GitHub Actions لبناء APK (مختصر)
-----------------------------------------------
ما تم إصلاحه:
- استبدال الحزمة غير المتوفرة `libncursesw-dev` بـ `libncurses-dev`.
- إضافة خطوة إعداد JDK (action outputs path مستخدمة).
- خطوات كاش لملفات Gradle، ومنح صلاحية تنفيذ gradlew.

ملاحظات:
- إن كنت تريد تضمين Android SDK/NDK أو توقيع keystore داخل الـ workflow، أعلمني لأضيف الخطوات.
- هذا الملف `android.yml` هو نموذج؛ تأكد أن بنية مشروع أندرويد لديك تحتوي على ملف `gradlew` وملف `app/build.gradle` لتوليد APK.

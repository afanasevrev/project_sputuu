from django.contrib import admin
from .models import UserProfile, Course, Material, Homework, HomeworkSubmission

# Регистрация модели UserProfile
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_teacher', 'bio')  # Поля, отображаемые в списке
    list_filter = ('is_teacher',)  # Фильтры в боковой панели
    search_fields = ('user__username', 'user__email', 'bio')  # Поля для поиска
    ordering = ('user__username',)  # Сортировка по умолчанию

# Регистрация модели Course
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher', 'description')  # Поля, отображаемые в списке
    list_filter = ('teacher',)  # Фильтры
    search_fields = ('name', 'description')  # Поля для поиска
    filter_horizontal = ('students',)  # Удобный интерфейс для ManyToManyField
    ordering = ('name',)  # Сортировка по умолчанию

# Регистрация модели Material
@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'uploaded_at', 'uploaded_by')  # Поля в списке
    list_filter = ('course', 'uploaded_at', 'uploaded_by')  # Фильтры
    search_fields = ('title', 'description')  # Поля для поиска
    ordering = ('-uploaded_at',)  # Сортировка по дате (новые сверху)

# Регистрация модели Homework
@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'deadline', 'created_by', 'created_at')  # Поля в списке
    list_filter = ('course', 'deadline', 'created_by')  # Фильтры
    search_fields = ('title', 'description')  # Поля для поиска
    ordering = ('-created_at',)  # Сортировка по дате (новые сверху)

# Регистрация модели HomeworkSubmission
@admin.register(HomeworkSubmission)
class HomeworkSubmissionAdmin(admin.ModelAdmin):
    list_display = ('homework', 'student', 'submitted_at', 'grade')  # Поля в списке
    list_filter = ('homework', 'student', 'submitted_at', 'grade')  # Фильтры
    search_fields = ('homework__title', 'student__username', 'feedback')  # Поля для поиска
    ordering = ('-submitted_at',)  # Сортировка по дате (новые сверху)

from django.db import models


class Diplom(models.Model):
    org_name = models.CharField("Название образовательной организации", max_length=200)
    qualification = models.CharField("Квалификация", max_length=100)
    # ser_number = models.
    student_name = models.CharField("ФИО студента", max_length=200)
    title = models.CharField("Название диплома", max_length=300)
    supervisor = models.CharField("Руководитель", max_length=200)
    year = models.DateField("Год защиты")
    description = models.TextField("Описание", blank=True)

    class Meta:
        ordering = ('year',)
        verbose_name = 'Диплом'
        verbose_name_plural = 'Дипломы'

    def __str__(self):
        return f"{self.student_name} - {self.title} ({self.year})"

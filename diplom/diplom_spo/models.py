from django.db import models


class Diplom(models.Model):
    org_name = models.CharField("Название образовательной организации", max_length=200, default=True)
    qualification = models.CharField("Квалификация", max_length=100, default=True)
    ser_number = models.IntegerField("Номер серии", default=True)
    reg_number = models.CharField("Регистрационный номер", max_length=10, default=True)
    grant_date = models.DateField("Дата выдачи", default=True)
    student_name = models.CharField("Настоящий диплом"
                                    "свидетельствует о том, что", max_length=200, default=True)
    complete = models.CharField("Осовил(а) образовательную программу"
                                "среднего профессионального образования и успешно"
                                "прошёл(шла) государственную итоговую аттестацию"
                                "по специальности", max_length=100, default=True)
    title = models.CharField("Название диплома", max_length=300, default=True)
    supervisor = models.CharField("Руководитель", max_length=200, default=True)
    year = models.DateField("Дата решения", default=True)
    copy = models.FileField("Копия диплома", default=True)

    class Meta:
        ordering = ('year',)
        verbose_name = 'Диплом'
        verbose_name_plural = 'Дипломы'

    def __str__(self):
        return f"{self.student_name} - {self.title} ({self.year})"

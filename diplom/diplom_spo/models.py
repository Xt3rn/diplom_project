from django.db import models


class Diplom(models.Model):
    org_name = models.CharField(verbose_name="Название образовательной организации",
                                help_text="Введите навзвание образовательной организации",
                                max_length=200, default=True)
    qualification = models.CharField(max_length=100,   
                                    verbose_name="Квалификация",
                                    help_text="Напишите квалификацию",
                                    default=True)
    ser_number = models.CharField(max_length=100,
                                    verbose_name="Номер серии",
                                    help_text="Введите номер серии",
                                    default=True)
    reg_number = models.CharField(max_length=10,
                                verbose_name="Регистрационный номер",
                                help_text="Введите регистрационный номер",
                                default=True)
    grant_date = models.DateField("Дата выдачи", default=True)
    student_name = models.CharField(max_length=200,
                                    verbose_name="ФИО",
                                    help_text="ФИО",
                                    default=True)
    speciality = models.CharField(max_length=100,
                                verbose_name="Специальность",
                                help_text="Введите специальность",
                                default=True)
    supervisor = models.CharField(max_length=200,
                                verbose_name="Руководитель",
                                help_text="Введите ФИО руководителя",
                                default=True)
    chairman = models.CharField(max_length=200,
                                verbose_name="Руководитель",
                                help_text="Введите ФИО руководителя",
                                default=True)
    year = models.DateField(verbose_name="Дата решения",
                            help_text="Введите дату решения",
                            default=True)
    copy = models.FileField(verbose_name="Копия диплома",
                            help_text="Вставьте копию диплома",
                            default=True)

    class Meta:
        ordering = ('year',)
        verbose_name = 'Диплом'
        verbose_name_plural = 'Дипломы'

    def __str__(self):
        return f"{self.student_name} - ({self.year})"

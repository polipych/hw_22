from django.db import models
from django.shortcuts import reverse
import datetime


class Task(models.Model):
    status = models.BooleanField(
        default=False,
        verbose_name="Status",
    )
    title = models.CharField(
        max_length=160,
        verbose_name="Title",
        # help_text='Description'
    )
    start = models.DateTimeField(auto_now_add=True, help_text="Created")
    end = models.DateTimeField(
        default=None,
        verbose_name="Closed",
        blank=True,
        null=True,
    )

    def get_absolute_url(self):
        return reverse("task", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs) -> None:
        """Переопределение сохранения.

        Убирается дата выполнения если галочка активности задачи снята и ставится дата если устанавливается галка.
        """
        if self.end is None and self.status:
            self.status = True
            self.end = datetime.datetime.now()
        elif self.end and not self.status:
            self.end = None
        return super().save(*args, **kwargs)

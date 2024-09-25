from django.db import models

from config.settings import NULLABLE


class Contact(models.Model):
    """
    Модель `Контакты` - контакты субъектов.
    """
    email = models.EmailField(
        unique=True,
        max_length=150,
        verbose_name='E-mail',
        help_text='Введите e-mail'
    )
    country = models.CharField(
        max_length=60,
        verbose_name='Страна',
        help_text='Введите страну',
        **NULLABLE
    )
    city = models.CharField(
        max_length=60,
        verbose_name='Город',
        help_text='Введите город',
        **NULLABLE
    )
    street = models.CharField(
        max_length=60,
        verbose_name='Улица',
        help_text='Введите улицу',
        **NULLABLE
    )
    house = models.PositiveIntegerField(
        verbose_name='Номер дома',
        help_text='Введите номер дома',
        **NULLABLE
    )

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Product(models.Model):
    """
    Модель `Продукты` - продукты субъекта.
    """
    name = models.CharField(
        max_length=60,
        verbose_name='Название',
        help_text='Введите название'
    )
    model = models.CharField(
        max_length=60,
        verbose_name='Модель',
        help_text='Введите модель',
        **NULLABLE
    )
    release = models.DateField(
        verbose_name='Дата выхода',
        help_text='Введите дату выхода на рынок',
        **NULLABLE
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class DataMixin(models.Model):
    """
    Модель `Данные субъекта`.
    """
    name = models.CharField(
        max_length=60,
        verbose_name='Название',
        help_text='Введите название'
    )
    contacts = models.OneToOneField(
        Contact,
        on_delete=models.CASCADE,
        verbose_name='Контакты',
        help_text='Введите контакты'
    )
    products = models.ManyToManyField(
        Product,
        verbose_name='Продукты',
        help_text='Введите продукты'
    )
    dept = models.DecimalField(
        default=0,
        max_digits=8,
        decimal_places=2,
        verbose_name='Задолженность',
        help_text='Введите задолженность перед поставщиком'
    )
    creation_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время',
        help_text='Введите время создания'
    )

    def __str__(self):
        return self.name


class Entrepreneur(DataMixin):
    """
    Модель `Индивидуальный предприниматель`.
    """
    supplier = models.ForeignKey(
        'RetailChain',
        on_delete=models.SET_NULL,
        verbose_name='Поставщик',
        help_text='Введите поставщика',
        **NULLABLE
    )

    class Meta:
        verbose_name = 'Предприниматель'
        verbose_name_plural = 'Предприниматели'


class RetailChain(DataMixin):
    """
    Модель `Розничная сеть`.
    """
    supplier = models.ForeignKey(
        Entrepreneur,
        on_delete=models.SET_NULL,
        verbose_name='Поставщик',
        help_text='Введите поставщика',
        **NULLABLE
    )

    class Meta:
        verbose_name = 'Розничная сеть'
        verbose_name_plural = 'Розничные сети'


class Factory(DataMixin):
    """
    Модель `Завод` - завод производитель.
    """
    supplier = models.ForeignKey(
        RetailChain,
        on_delete=models.SET_NULL,
        verbose_name='Поставщик',
        help_text='Введите поставщика',
        **NULLABLE
    )

    class Meta:
        verbose_name = 'Завод'
        verbose_name_plural = 'Заводы'

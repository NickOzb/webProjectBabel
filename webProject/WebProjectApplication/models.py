from django.db import models
import string
import random

# Create your models here.
class Kategoriitovara(models.Model):
    namekategorii = models.CharField(max_length=20)
    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товара'
    def __str__(self):
        return self.namekategorii

class Tovar(models.Model):
    name = models.CharField(max_length=20)
    edizm = models.CharField(max_length=10)
    kodkategorii = models.ForeignKey(Kategoriitovara, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
    def __str__(self):
        return self.name

class Bank(models.Model):
    namebanka = models.CharField(max_length=20)
    class Meta:
        verbose_name = 'Банк'
        verbose_name_plural = 'Банки'
    def __str__(self):
        return str(self.id) + " " + self.namebanka

class Nalogi(models.Model):
    namenaloga = models.CharField(max_length=20)
    percent = models.IntegerField(null=1)
    class Meta:
        verbose_name = 'Налог'
        verbose_name_plural = 'Налоги'
    def __str__(self):
        return str(self.id) + " " + self.namenaloga

class Dvizhenie(models.Model):
    articul = models.ForeignKey(Tovar, on_delete=models.CASCADE)
    kolvotovara = models.IntegerField(null=1)
    cena = models.IntegerField(null=1)
    class Meta:
        verbose_name = 'Движение товара'
        verbose_name_plural = 'Движение товаров'
    def __str__(self):
        return str(self.id)


class Organizatsiya(models.Model):
    nameorg = models.CharField(max_length=20)
    kodbanka = models.ForeignKey(Bank, on_delete=models.CASCADE)
    schetorg = models.IntegerField(null=1)
    adress = models.CharField(max_length=40)
    fioruk = models.CharField(max_length=40)
    phone = models.IntegerField(null=1)
    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
    def __str__(self):
        return str(self.id) + " " + self.nameorg


class Nakladnie(models.Model):
    nnakladnoy = models.ForeignKey(Dvizhenie, on_delete=models.CASCADE)
    date = models.CharField(max_length=20)
    priznak = models.CharField(max_length=20)
    kodorg = models.ForeignKey(Organizatsiya, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Накладная'
        verbose_name_plural = 'Накладные'
    def __str__(self):
        return str(self.id)

class Podrazdeleniya(models.Model):
    kodsklada = models.ForeignKey(Nakladnie, on_delete=models.CASCADE)
    namesklada = models.CharField(max_length=20)
    fio = models.CharField(max_length=40)
    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'
    def __str__(self):
        return str(self.id)


class Taksirovka(models.Model):
    nnakladnoy = models.ForeignKey(Dvizhenie, on_delete=models.CASCADE)
    kodnaloga = models.ForeignKey(Nalogi, on_delete=models.CASCADE)
    sumnaloga = models.IntegerField(null=1)
    class Meta:
        verbose_name = 'Таксировка'
        verbose_name_plural = 'Таксировки'
    def __str__(self):
        return str(self.id)

class Ostatki(models.Model):
    articul = models.ForeignKey(Tovar, on_delete=models.CASCADE)
    srcena = models.IntegerField(null=1)
    kolvotovarananachalo = models.IntegerField(null=1)
    kolvoprihod = models.IntegerField(null=1)
    kolvorashod = models.IntegerField(null=1)
    class Meta:
        verbose_name = 'Остаток'
        verbose_name_plural = 'Остатки'
    def __str__(self):
        return str(self.id)


def generate_unique_code():
    length = 6

    while True:
        code = ''.join(random.choises(string.ascii_uppercase, k=length))
        if Room.objects.filter(code=code).count == 0:
            break

    return code

class Room(models.Model):
    code = models.CharField(max_length=8, default="", unique=True)
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=2)
    created_at = models.DateTimeField(auto_now_add=True)


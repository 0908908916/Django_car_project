from django.db import models


class Brand(models.Model):
    """汽車品牌"""
    name = models.CharField(max_length=100, verbose_name='品牌名稱')
    logo = models.ImageField(
        upload_to='brands/', blank=True, null=True, verbose_name='品牌 Logo')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '品牌'
        verbose_name_plural = '品牌管理'


class Car(models.Model):
    """汽車車款"""
    FUEL_CHOICES = [
        ('gasoline', '汽油'),
        ('diesel', '柴油'),
        ('electric', '電動'),
        ('hybrid', '油電混合'),
    ]

    TRANSMISSION_CHOICES = [
        ('auto', '自動'),
        ('manual', '手動'),
    ]

    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, verbose_name='品牌')
    name = models.CharField(max_length=200, verbose_name='車款名稱')
    year = models.IntegerField(verbose_name='年份')
    price = models.DecimalField(
        max_digits=12, decimal_places=0, verbose_name='售價（元）')
    fuel_type = models.CharField(
        max_length=20, choices=FUEL_CHOICES, verbose_name='燃料類型')
    transmission = models.CharField(
        max_length=10, choices=TRANSMISSION_CHOICES, verbose_name='變速箱')
    engine_cc = models.IntegerField(
        verbose_name='排氣量（cc）', blank=True, null=True)
    seats = models.IntegerField(default=5, verbose_name='座位數')
    description = models.TextField(blank=True, verbose_name='車款說明')
    image = models.ImageField(
        upload_to='cars/', blank=True, null=True, verbose_name='車款圖片')
    is_available = models.BooleanField(default=True, verbose_name='上架中')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.brand.name} {self.name} ({self.year})'

    class Meta:
        verbose_name = '車款'
        verbose_name_plural = '車款管理'
        ordering = ['-created_at']


class Inquiry(models.Model):
    """詢價 / 預約表單"""
    STATUS_CHOICES = [
        ('pending', '待處理'),
        ('contacted', '已聯絡'),
        ('done', '已完成'),
    ]

    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='詢問車款')
    name = models.CharField(max_length=100, verbose_name='姓名')
    phone = models.CharField(max_length=20, verbose_name='電話')
    email = models.EmailField(verbose_name='Email')
    message = models.TextField(blank=True, verbose_name='留言')
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name='狀態')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} — {self.car}'

    class Meta:
        verbose_name = '詢價紀錄'
        verbose_name_plural = '詢價管理'
        ordering = ['-created_at']

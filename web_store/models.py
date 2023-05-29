from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255,unique=True) #ชื่อประเภทสินค้า(ห้ามชื่อซ้ำกัน)
    slug = models.SlugField(max_length=255,unique=True) #ตั้งชื่อเล่นให้ข้อมูล จัดหมวดหมู่(ผูกข้อมูลกับ url)


    def __str__(self): # แปลงข้อมูล model ที่สร้างแปลงเป็น string q
        return self.name 
    
    class Meta :
        ordering = ('name',) #เรียงลำดับชื่อ
        verbose_name = 'หมวดหมู่สินค้า'
        verbose_name_plural = 'ข้อมูลประเภทสินค้า'
    
class Product(models.Model):
    name = models.CharField(max_length=255,unique=True) 
    slug = models.SlugField(max_length=255,unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2) #เป็นทศนิยม  และทศนิยม 2 ตำแหน่ง
    catagory = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product',blank=True) 
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    create = models.DateTimeField(auto_now_add=True) #วันเวลา ปัจจุบันที่กดบันทึกสินค้า 
    update = models.DateField(auto_now=True)  # หลังจาก
    
    def __str__(self) -> str:
        return self.name
    
    class Meta :
        ordering = ('name',) #เรียงลำดับชื่อ
        verbose_name = 'สินค้า'
        verbose_name_plural = 'ข้อมูลสินค้า'

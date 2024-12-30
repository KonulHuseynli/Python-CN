from django.db import models
from django.contrib.auth.models import User
from core.utils.image_size_validator import validate_image
#classlari yaziriq. ne deyişiklik etsek migration elemek lazimdir.
#python paketlerinden istifade zamani ise migration elemeye ehtiyac qalmir
"""
bu fieldler hal hazirda user modeliynen blog modelin elaqelendirmek ucun istifade olunur

OneToOneField -bir userin bir blogu ola biler
ForeignKey - bir userin coxlu blogu ola biler.bir muellifin coxlu blogu var
ManyToManyField - coxlu userin coxlu blogu.bir blogun coxlu yazicisi olur

#author = models.OneToOneField(User, on_delete=models.SET_NULL, null = True)#models.Setnull= user silinse ona aid olan bloglara null deyer verilir #author_id=NULL, bloglara hecne olmur
Qeyd :on_delete = models.SET_NULL verilse mutleqq null =True verilmelidir

#author =models.OneToOneField(User, on_delete = models.CASCADE) user obj-silinse onun butun bloglarini sileceksen(databaza sevyesinde aparir)
"""

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Category name: ') #admin panel ve ya formda name categoryname kimi gorunecek

    def __str__(self) ->str:
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        

class Watches(models.Model): #Model classindan miras aliriq
    author = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    categories = models.ManyToManyField(Category)
    
    name = models.CharField(max_length = 120)
    brand = models.CharField(max_length = 80) #max length olur
    price = models.DecimalField(max_digits = 10 , decimal_places=2)
    description = models.TextField() #max olmur
    release_date = models.DateTimeField(auto_now_add=True) #null-database sevyesinde melumatin olmamasin() yeni null olmasin qebul edir.blank ise form sevyesinde bos gonderilmesin qebul edir.
    image = models.ImageField(upload_to='media', null=True, blank=True, validators=[validate_image])
    
    def __str__(self) ->str:  #magic(dunder) metodlari yazandan sonra migrate elemeye ehtiyac qalmir(python seviyyesinde olan metoddur-sql-ile elaqesi yoxdur)
        try:
           return  f'{self.author.username} <---> {self.name}'
        except:
            return f' null <---> {self.name}'
# auto_now =True her save metodu cagrilanda yenilenir
# auto_now_add=true ilk yaradilan zaman olan tarixi goturur
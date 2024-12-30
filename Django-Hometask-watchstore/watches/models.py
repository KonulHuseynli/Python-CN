#classlari yaziriq. ne deyişiklik etsek migration elemek lazimdir.
#python paketlerinden istifade zamani ise migration elemeye ehtiyac qalmir

from django.db import models


class Watches(models.Model): #Model classindan miras aliriq
    name = models.CharField(max_length = 120)
    brand = models.CharField(max_length = 80) #max length olur
    price = models.DecimalField(max_digits = 10 , decimal_places=2)
    description = models.TextField() #max olmur
    release_date = models.DateTimeField(null=True, blank=True) #null-database sevyesinde melumatin olmamasin() yeni null olmasin qebul edir.blank ise form sevyesinde bos gonderilmesin qebul edir.

    
    def __str__(self) ->str:  #magic(dunder) metodlari yazandan sonra migrate elemeye ehtiyac qalmir(python seviyyesinde olan metoddur-sql-ile elaqesi yoxdur)
        return  f'{self.name} <---> {self.brand}'
from django import forms

from watches.models import Watches

class WatchForm(forms.ModelForm): #birbasa modelin fieldlerinden istifade etmek ucun modelform yaziriq
    release_date = forms.DateTimeField(input_formats=['%d-%m-%Y %H:%M '],required=False) #required true o demekdirki hemen fieldi bos gondermek olmaz,Bos gondermek isteyirsense required=False ve  modelden tenzimlemek lazimdir.
    class Meta:
        model = Watches
        # fields = ('__all__')
        exclude = ('author',) #authordan basqa butun fieldleri gosterir
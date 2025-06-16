from django import forms
from .models import Toko, Produk

class TokoForm(forms.ModelForm):
    class Meta:
        model = Toko
        fields = ['nama', 'alamat', 'kabupaten', 'latitude', 'longitude']
        widgets = {
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }


class ProdukForm(forms.ModelForm):
    class Meta:
        model = Produk
        fields = ['nama', 'deskripsi', 'harga','foto_produk', 'is_active']
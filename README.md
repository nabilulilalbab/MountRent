# 🏔️ Mount Project

Proyek Django untuk manajemen dan eksplorasi informasi gunung. Termasuk fitur komentar, rating, penghitungan pengunjung, serta pengelompokan berdasarkan kategori kesulitan.

## 📁 Struktur Folder

```

myproject/
├── accounts/           # Manajemen user
├── gunung/             # Fitur utama (data gunung, komentar, rating)
├── rental/             # (opsional) penyewaan peralatan
├── toko/               # (opsional) toko atau marketplace
├── feedback/           # (opsional) masukan dan testimoni
├── media/              # File upload (foto, template, dsb)
├── static/             # Static files (CSS, JS, gambar)
├── templates/          # Template HTML
├── db.sqlite3          # Database lokal (ignored in Git)
├── manage.py           # Entrypoint Django

````

---

## 🚀 Cara Menjalankan Proyek

### 1. Clone Repositori

```bash
git clone https://github.com/username/nama-repo.git
cd nama-repo
````

### 2. Buat dan Aktifkan Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> Jika belum ada `requirements.txt`, kamu bisa buat dengan:
>
> ```bash
> pip freeze > requirements.txt
> ```

### 4. Migrasi Database

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Buat Superuser

```bash
python manage.py createsuperuser
```

### 6. Jalankan Server

```bash
python manage.py runserver
```

Buka di browser: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🧪 Fitur Utama

* [x] Registrasi & login user
* [x] CRUD data gunung
* [x] Komentar dan rating per gunung
* [x] Hitung rata-rata rating
* [x] Hitung total view tiap gunung
* [ ] Testimoni & feedback
* [ ] Sewa peralatan (rental)
* [ ] Toko/affiliate produk outdoor

---

## 📦 Media & Static Files

Pastikan folder `media/` dan `static/` tersedia:

```bash
mkdir media static
```

Jangan lupa di development, tambahkan ini di `settings.py`:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
```

Dan tambahkan ini di `urls.py` utama:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## ✅ TODO (opsional)

* [ ] Pagination komentar
* [ ] Dashboard admin dengan grafik sederhana
* [ ] Filter gunung berdasarkan kategori & pencarian
* [ ] Integrasi upload file template per gunung

---

## 🧑‍💻 Kontribusi

Pull request dan ide sangat diterima!
Silakan fork dan kirim perubahanmu.

---

## 📄 Lisensi

MIT License – bebas digunakan dan dimodifikasi.

```




# Instaloader - Instagram Data Downloader

Instaloader adalah sebuah library Python yang memungkinkan Anda untuk mengunduh data dari Instagram, termasuk postingan, cerita, profil, dan banyak lagi. Library ini mudah digunakan dan tidak memerlukan API resmi dari Instagram.

## Fitur
- Mengunduh foto, video, dan cerita dari Instagram
- Mendapatkan informasi profil pengguna Instagram (seperti jumlah pengikut, bio, dsb.)
- Mendownload seluruh konten dari akun publik atau akun yang diikuti
- Mendukung pengunduhan post berdasarkan tagar atau lokasi tertentu
- Bisa dijalankan tanpa autentikasi (untuk akun publik)

## Instalasi

Untuk menginstal Instaloader, gunakan perintah `pip` berikut:

```bash
pip install instaloader
```

## Cara Penggunaan

### 1. Mendapatkan Postingan dari Akun Instagram

Berikut adalah contoh kode untuk mengambil postingan dari profil Instagram tertentu.

```python
import instaloader

# Inisialisasi instaloader
loader = instaloader.Instaloader()

# Ambil profil Instagram
profile = instaloader.Profile.from_username(loader.context, "username_Instagram")

# Loop melalui postingan dan tampilkan
for post in profile.get_posts():
    print(f"Post URL: https://www.instagram.com/p/{post.shortcode}/")
    print(f"Caption: {post.caption}")
    print(f"Likes: {post.likes}")
    print(f"Date: {post.date}")
    print("-" * 30)
```

**Penjelasan:**
- Gantilah `"username_Instagram"` dengan nama pengguna yang ingin Anda ambil datanya.
- Kode ini akan mengambil semua postingan dari akun yang ditentukan dan menampilkan informasi seperti URL, caption, jumlah suka (likes), dan tanggal postingan.

### 2. Mengunduh Foto atau Video

Untuk mengunduh foto atau video dari akun Instagram, Anda bisa menggunakan kode berikut:

```python
import instaloader

# Inisialisasi instaloader
loader = instaloader.Instaloader()

# Ambil profil Instagram
profile = instaloader.Profile.from_username(loader.context, "username_Instagram")

# Loop untuk mengunduh postingan
for post in profile.get_posts():
    loader.download_post(post, target=profile.username)
```

**Penjelasan:**
- Kode ini akan mengunduh semua postingan (foto atau video) dari akun Instagram yang ditentukan dan menyimpannya di folder dengan nama pengguna profil.

### 3. Mengunduh Profil Pengguna

Untuk mengunduh informasi lengkap tentang sebuah profil pengguna (seperti jumlah pengikut, bio, dsb.), Anda bisa menggunakan kode berikut:

```python
import instaloader

# Inisialisasi instaloader
loader = instaloader.Instaloader()

# Ambil profil Instagram
profile = instaloader.Profile.from_username(loader.context, "username_Instagram")

# Tampilkan informasi profil
print(f"Username: {profile.username}")
print(f"Full Name: {profile.full_name}")
print(f"Bio: {profile.biography}")
print(f"Followers: {profile.followers}")
print(f"Following: {profile.followees}")
print(f"Posts: {profile.mediacount}")
```

**Penjelasan:**
- Kode ini akan menampilkan informasi profil pengguna Instagram seperti nama lengkap, bio, jumlah pengikut, jumlah yang diikuti, dan jumlah postingan.

## Pengunduhan Berbasis Tagar atau Lokasi

Selain mengunduh postingan dari pengguna tertentu, Anda juga bisa mencari postingan berdasarkan **hashtag** atau **lokasi**. Berikut adalah contoh untuk mengunduh postingan dengan tagar tertentu:

```python
import instaloader

# Inisialisasi instaloader
loader = instaloader.Instaloader()

# Tentukan tagar yang ingin diunduh
hashtag = "nature"

# Ambil postingan berdasarkan tagar
for post in instaloader.Hashtag.from_name(loader.context, hashtag).get_posts():
    loader.download_post(post, target=hashtag)
```

**Penjelasan:**
- Kode ini akan mengunduh semua postingan dengan tagar `nature` dan menyimpannya di folder yang dinamai tagar tersebut.

## Autentikasi (Opsional)

Instaloader memungkinkan Anda untuk login menggunakan akun Instagram jika Anda ingin mengakses konten pribadi atau lebih banyak konten yang diikuti. Untuk login, Anda bisa menambahkan kode berikut:

```python
import instaloader

# Inisialisasi instaloader
loader = instaloader.Instaloader()

# Login menggunakan akun Instagram
loader.context.log("Masukkan username dan password")
loader.load_session_from_file("username")  # Untuk memuat sesi yang sudah disimpan sebelumnya
# atau
loader.login("username", "password")  # Login langsung dengan username dan password

# Setelah login, Anda dapat mengunduh konten pribadi
```

**Penting:**
- Pastikan untuk menggunakan akun yang sah dan tidak melanggar kebijakan privasi Instagram.
- Jangan gunakan kredensial yang bocor atau akun yang tidak sah.

## Catatan
- Library ini dapat digunakan untuk akun **publik** atau akun yang **sudah diikuti** (jika login dilakukan).
- Jika Anda ingin mengunduh seluruh konten akun pribadi, Anda perlu melakukan login menggunakan akun Instagram yang sah.
- Instaloader tidak mengubah atau memodifikasi konten Instagram dan hanya digunakan untuk mengunduh data dari platform.

## Referensi
- [Instaloader Documentation](https://instaloader.github.io/)
- [Instagram Graph API](https://developers.facebook.com/docs/instagram-api)

---

Dengan Instaloader, Anda dapat mengunduh dan mengakses berbagai data dari Instagram secara efisien menggunakan Python.
```

### Penjelasan Struktur Dokumentasi:
- **Instalasi**: Menyediakan petunjuk untuk menginstal Instaloader menggunakan `pip`.
- **Cara Penggunaan**: Menyediakan contoh kode untuk penggunaan dasar seperti mengunduh postingan, mengunduh foto/video, dan mendapatkan informasi profil pengguna.
- **Pengunduhan Berdasarkan Tagar atau Lokasi**: Menyediakan kode untuk mencari dan mengunduh postingan berdasarkan tagar atau lokasi.
- **Autentikasi**: Menyediakan contoh untuk login menggunakan akun Instagram jika perlu mengakses konten pribadi atau lebih banyak postingan.
- **Catatan**: Mengingatkan pengguna untuk mematuhi kebijakan privasi Instagram.


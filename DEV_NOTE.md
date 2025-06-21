# Catatan Pengembangan

## Aktivasi Python Virtual Environment (Python)

**Langkah 0** (lakukan 1x saja) buath _virtual environment_

Pindah ke home dari direktori proyek lalu

```bash
python -m venv venv
```

**Langkah 1** : Jalankan Terminal / Powershell sbg `administrator`

**Langkah 2** : Ubah _execution policies_

```bash
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

penjelasan:

- `Set-ExecutionPolicy`: The cmdlet to change execution policies.
- `-Scope Process`: the change only applies to the current PowerShell session. Once you close the PowerShell window, the execution policy reverts to its default.
- `-ExecutionPolicy RemoteSigned`: allows local scripts to run, but scripts downloaded from the internet must be signed by a trusted publisher.

**Langkah 3** : Aktifkan _virtual environment_

```bash
.\venv\Scripts\Activate.ps1
```

**Langkah -1** (lakukan saat selesai) : deaktivasi virtual environment

```bash
deactivate
```

## Branching

```tree
main / production
│
└───dev / staging
     ├───feature/strava-integration
     ├───feature/ui-layout
     ├───feature/db-setup
     ├───feature/oauth-login
     └───fix/bug-title-truncation
```

| Branch      | Tujuan                                                                                                              |
| ----------- | ------------------------------------------------------------------------------------------------------------------- |
| `main`      | Berisi **kode stabil** dan siap **deploy ke production**                                                            |
| `dev`       | Tempat **integrasi semua fitur** yang masih dalam pengembangan.                                                     |
| `feature/*` | Digunakan untuk **mengembangkan satu fitur spesifik** seperti koneksi ke Strava API, tampilan UI, login OAuth, dsb. |
| `fix/*`     | Untuk memperbaiki **bug spesifik**.                                                                                 |
| `hotfix/*`  | Jika nanti sudah ada production dan perlu perbaikan                                                                 |

### Penggunaan Branch dalam Proyek

```bash
git branch dev         # Buat branch dev
git checkout dev       # Pindah ke dev
```

| Tujuan                      | Perintah Git                                 |
| --------------------------- | -------------------------------------------- |
| Buat branch baru dari `dev` | `git checkout -b feature/nama-fitur`         |
| Pindah ke branch lain       | `git checkout nama-branch`                   |
| Lihat semua branch          | `git branch`                                 |
| Gabung branch ke `dev`      | `git checkout dev` → `git merge feature/...` |
| Hapus branch setelah merge  | `git branch -d feature/yang-sudah-merged`    |

### Buat Repo

```bash
git branch dev         # Buat branch dev
git checkout dev       # Pindah ke dev
```

### Otomatis update requirements.txt setelah install library pip

```bash
pip install Flask stravalib python-dotenv
pip freeze > requirements.txt # maka segala library & dependencynya akan masuk ke requirements.txt

pip install sqlalchemy psycopg2-binary flask-sqlalchemy flask-migrate
pip freeze > requirements.txt
```

### Generate secrets

Cara mudah :

```bash
echo "sesuatu" | md5sum
```

### Inisialisasi Database

```bash
flask db init
flask db migrate -m "create users table"
flask db upgrade
```

Ekstensi Flask-Migrate memungkinkan kita untuk melakukan migrasi database secara terprogram.

`flask db init` : inisialisasi sebuah direktori migrasi (biasanya bernama migrations/) di dalam root proyek.
`flask db migrate -m "create users table"` : Membuat skrip migrasi baru berdasarkan perbedaan antara skema database saat ini (atau skema kosong jika ini migrasi pertama) dan definisi model SQLAlchemy.
`flask db upgrade` :  Menjalankan migrasi yang tertunda (yang telah dibuat dengan `flask db migrate`) untuk memperbarui skema database ke versi terbaru.

output:

```log
(venv) PS C:\Users\ASUS\Documents\Projects\platform-lomba-strava-simpel> flask db migrate -m "create users table"
WARNI [py.warnings] C:\Users\ASUS\Documents\Projects\platform-lomba-strava-simpel\migrations\env.py:21: DeprecationWarning: 'get_engine' is deprecated and will be removed in Flask-SQLAlchemy 3.2. Use 'engine' or 'engines[key]' instead. If you're using Flask-Migrate or Alembic, you'll need to update your 'env.py' file.
  return current_app.extensions['migrate'].db.get_engine()

INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.env] No changes in schema detected.
(venv) PS C:\Users\ASUS\Documents\Projects\platform-lomba-strava-simpel> flask db upgrade
WARNI [py.warnings] C:\Users\ASUS\Documents\Projects\platform-lomba-strava-simpel\migrations\env.py:21: DeprecationWarning: 'get_engine' is deprecated and will be removed in Flask-SQLAlchemy 3.2. Use 'engine' or 'engines[key]' instead. If you're using Flask-Migrate or Alembic, you'll need to update your 'env.py' file.
  return current_app.extensions['migrate'].db.get_engine()

INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
```

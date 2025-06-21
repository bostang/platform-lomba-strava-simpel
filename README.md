# platform-lomba-strava-simpel

Sebuah platform (web) lomba sederhana yang berinteraksi dengan ekosistem Strava (via API) berbasis bahasa pemrograman Python

## Desain

### Desain Database

<!-- ![Skema Database](./img/db_schema.png) -->

![Skema Database](./img/db_schema_initial.png)

#### Uraian Tabel

##### `users`

Individu peserta yang login dengan akun Strava.

| Kolom                | Tipe Data    | Keterangan                    |
| ------------------   | ----------   | ----------------------------- |
| `id`                 | `UUID`       | Primary Key                   |
| `strava_id`          | `BIGINT`     | ID dari Strava                |
| `username`           | `VARCHAR`    | Nama tampilan                 |
| `full_name`          | `VARCHAR`    | Nama lengkap                  |
| `access_token`       | `TEXT`       | Token OAuth untuk akses API   |
| `refresh_token`      | `TEXT`       | Token untuk refresh           |
| `token_expires_at`   | `TIMESTAMP`  | Token expiry time             |
| `created_at`         | `TIMESTAMP`  | Timestamp saat user terdaftar |

<!-- ##### `teams`

tim tempat peserta bergabung pada lomba.

| Kolom         | Tipe Data    | Keterangan                       |
| ------------  | ----------   | -------------------------------- |
| `id`          | `UUID`       | Primary Key                      |
| `name`        | `VARCHAR`    | Nama tim                         |
| `code`        | `VARCHAR`    | Kode unik  untuk join ke tim     |
| `created_at`  | `TIMESTAMP`  | Tanggal dibuat                   | -->

<!-- ##### `team_members`

Tabel penghubung untuk menyatakan relasi _many-to-many_ antara `users` dan `teams`.

| Kolom        | Tipe Data    | Keterangan             |
| ----------   | ----------   | ---------------------- |
| `id`         | `INT`        | Primary Key            |
| `user_id`    | FK → `users` | Peserta                |
| `team_id`    | FK → `teams` | Tim                    |
| `joined_at`  | `TIMESTAMP`  | Waktu bergabung ke tim | -->

##### `activities`

Aktivitas dari Strava (run, bike). Berisi detail informasi performa seperti jarak, waktu aktivitas, pace, dan lain-lain.

| Kolom          | Tipe Data  | Keterangan                  |
| -------------- | ---------- | --------------------------- |
| `id`           | UUID       | Primary Key                 |
| `strava_id`    | BIGINT     | ID aktivitas dari Strava    |
| `user_id`      | FK → users | Pemilik aktivitas           |
| `name`         | VARCHAR    | Nama aktivitas (judul)      |
| `distance`     | FLOAT      | Dalam meter                 |
| `moving_time`  | INTEGER    | Dalam detik                 |
| `elapsed_time` | INTEGER    | Dalam detik                 |
| `type`         | VARCHAR    | Jenis: Run, Ride, Swim, dll |
| `start_date`   | TIMESTAMP  | Tanggal aktivitas           |
| `created_at`   | TIMESTAMP  | Waktu data ini disimpan     |

<!-- ##### `team_scores`

hasil agregat perolehan performa dari seluruh anggota tim.

| Kolom            | Tipe Data           | Keterangan                          |
| ---------------  | -----------------   | ----------------------------------- |
| `id`             | `INT`               | Primary Key                         |
| `team_id`        | FK → `teams`        | Tim                                 |
| `total_distance` | `NUMERIC`           | Total jarak                         |
| `elapsed_time`   | `NUMERIC`           | Total waktu aktivitas               |
| `avg_pace`       | `NUMERIC`           | Rata-rata pace tim untuk total 20km |
| `submitted_at`   | `TIMESTAMP`         | Terakhir kali diperbarui            | -->

## Implementasi

### Struktur File

```tree
.
├── DEV_NOTE.md
├── LICENSE
├── README.md
├── app
│   ├── __init__.py
│   ├── config.py
│   ├── extensions.py
│   ├── models.py
│   ├── templates
│   │   ├── base.html
│   │   ├── choose_activities.html
│   │   ├── dashboard.html
│   │   ├── index.html
│   │   ├── login.html
│   │   └── my_activities.html
│   └── views
│       ├── __init__.py
│       ├── activities.py
│       ├── auth.py
│       ├── dashboard.py
│       └── home.py
├── img
│   └── db_schema.png
├── migrations
│   ├── README
│   ├── alembic.ini
│   ├── env.py
│   ├── script.py.mako
│   └── versions
│       ├── 5a2797440a47_create_activities_table.py
│       └── 967c1aaee5bf_create_users_table.py
├── requirements.txt
├── .env
└── run.py
```

## Cara Menjalankan

**Langkah 1** : Aktifkan virtual environment python dan install library

> lihat `DEV_NOTE.md`

**Langkah 2** : Siapkan `.env` di root proyek

```conf
###### STRAVA ######
# Didapat dari https://www.strava.com/settings/api
# paduan : https://developers.strava.com/docs/getting-started/
STRAVA_CLIENT_ID=XXXXXX
STRAVA_CLIENT_SECRET=XXXXXXXXXXX
STRAVA_REDIRECT_URI=http://localhost:5000/authorize
    # contoh redirect nanti : http://localhost:5000/authorize?state=&code=XXXX&scope=read,activity:read
    
SECRET_KEY=a18642c4852a9cd51f4b8ed72455027b
    # saya generate dengan : echo "platform-lomba-strava-simpel" | md5sum

###### POSTGRESQL ######
DATABASE_URL=postgresql://postgres:password@localhost:5432/strava_db
```

**Langkah 3** : Jalankan aplikasi

```bash
python run.py
```

## Pranala

- [SQLAlchemy](https://www.sqlalchemy.org/)
- [flask](https://flask.palletsprojects.com/en/stable/)
- [stravalib](https://github.com/stravalib/stravalib)
- [Strava Developer](https://developers.strava.com/)

# platform-lomba-strava-simpel

Sebuah platform (web) lomba sederhana yang berinteraksi dengan ekosistem Strava (via API) berbasis bahasa pemrograman Python

## Desain

### Desain Database

![Skema Database](./img/db_schema.png)

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

##### `teams`

tim tempat peserta bergabung pada lomba.

| Kolom         | Tipe Data    | Keterangan                       |
| ------------  | ----------   | -------------------------------- |
| `id`          | `UUID`       | Primary Key                      |
| `name`        | `VARCHAR`    | Nama tim                         |
| `code`        | `VARCHAR`    | Kode unik  untuk join ke tim     |
| `created_at`  | `TIMESTAMP`  | Tanggal dibuat                   |

##### `team_members`

Tabel penghubung untuk menyatakan relasi _many-to-many_ antara `users` dan `teams`.

| Kolom        | Tipe Data    | Keterangan             |
| ----------   | ----------   | ---------------------- |
| `id`         | `INT`        | Primary Key            |
| `user_id`    | FK → `users` | Peserta                |
| `team_id`    | FK → `teams` | Tim                    |
| `joined_at`  | `TIMESTAMP`  | Waktu bergabung ke tim |

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

##### `team_scores`

hasil agregat perolehan performa dari seluruh anggota tim.

| Kolom            | Tipe Data           | Keterangan                          |
| ---------------  | -----------------   | ----------------------------------- |
| `id`             | `INT`               | Primary Key                         |
| `team_id`        | FK → `teams`        | Tim                                 |
| `total_distance` | `NUMERIC`           | Total jarak                         |
| `elapsed_time`   | `NUMERIC`           | Total waktu aktivitas               |
| `avg_pace`       | `NUMERIC`           | Rata-rata pace tim untuk total 20km |
| `submitted_at`   | `TIMESTAMP`         | Terakhir kali diperbarui            |

## Implementasi

### Struktur File

```tree
.
```

## Pranala

- [SQLAlchemy](https://www.sqlalchemy.org/)
- [flask](https://flask.palletsprojects.com/en/stable/)
- [stravalib](https://github.com/stravalib/stravalib)
- [Strava Developer](https://developers.strava.com/)

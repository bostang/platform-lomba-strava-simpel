# platform-lomba-strava-simpel

Sebuah platform (web) lomba sederhana yang berinteraksi dengan ekosistem Strava (via API) berbasis bahasa pemrograman Python

## Desain

### Desain Database

![Skema Database](./img/db_schema.png)

#### Uraian Tabel

##### `users`

Individu peserta yang login dengan akun Strava.

| Kolom              | Tipe Data  | Keterangan                    |
| ------------------ | ---------- | ----------------------------- |
| id                 | UUID       | Primary Key                   |
| strava\_id         | BIGINT     | ID dari Strava                |
| username           | VARCHAR    | Nama tampilan                 |
| full\_name         | VARCHAR    | Nama lengkap                  |
| access\_token      | TEXT       | Token OAuth untuk akses API   |
| refresh\_token     | TEXT       | Token untuk refresh           |
| token\_expires\_at | TIMESTAMP  | Token expiry time             |
| created\_at        | TIMESTAMP  | Timestamp saat user terdaftar |

##### `teams`

tim tempat peserta bergabung pada lomba.

| Kolom       | Tipe Data  | Keterangan                       |
| ----------- | ---------- | -------------------------------- |
| id          | UUID       | Primary Key                      |
| name        | VARCHAR    | Nama tim                         |
| code        | VARCHAR    | Kode unik  untuk join ke tim     |
| created\_at | TIMESTAMP  | Tanggal dibuat                   |

##### `team_members`

Tabel penghubung untuk menyatakan relasi _many-to-many_ antara `users` dan `teams`.

| Kolom      | Tipe Data  | Keterangan             |
| ---------- | ---------- | ---------------------- |
| id         | INT        | Primary Key            |
| user\_id   | FK → Users | Peserta                |
| team\_id   | FK → Teams | Tim                    |
| joined\_at | TIMESTAMP  | Waktu bergabung ke tim |

##### `activities`

Aktivitas dari Strava (run, bike). Berisi detail informasi performa seperti jarak, waktu aktivitas, pace, dan lain-lain.

| Kolom              | Tipe Data   | Keterangan                              |
| ------------------ | ----------- | --------------------------------------- |
| id                 | BIGINT      | ID dari Strava (unik global)            |
| user\_id           | FK → Users  | Pemilik aktivitas                       |
| type               | VARCHAR     | Jenis aktivitas (Run, Ride, Swim, Hike) |
| distance\_km       | NUMERIC     | Jarak dalam kilometer                   |
| elapsed\_time      | INT (detik) | Waktu bergerak                          |
| pace               | NUMERIC     | Pace (jika applicable, misal untuk Run) |
| start\_date        | TIMESTAMP   | Tanggal dan waktu mulai aktivitas       |
| submit\_date       | TIMESTAMP   | Waktu aktivitas diambil                 |
| is\_valid          | BOOLEAN     | Untuk keperluan validasi manual/admin   |
| activity\url       | VARCHAR     | Link menuju aktivitas stravanya         |

##### `team_scores`

hasil agregat perolehan performa dari seluruh anggota tim.

| Kolom           | Tipe Data         | Keterangan                          |
| --------------- | ----------------- | ----------------------------------- |
| id              | INT / UUID        | Primary Key                         |
| team\_id        | FK → Teams        | Tim                                 |
| total\_distance | NUMERIC           | Total jarak                         |
| elapsed\time    | NUMERIC           | Total waktu aktivitas               |
| avg\_pace       | NUMERIC           | Rata-rata pace tim untuk total 20km |
| submitted\_at   | TIMESTAMP         | Terakhir kali diperbarui            |

## Implementasi

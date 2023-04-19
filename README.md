# Esercizio Django Docker Compose

## Django Get Started
https://docs.djangoproject.com/en/4.2/intro/tutorial01/

## Architettura

### Servizio 1: Django

1. Creare un **Dockerfile** FROM **python:3**
2. Per creare il Dockerfile prendete spunto da quello usato per **Flask**
3. Esporre la porta 8000 del container sulla porta 8000 dell'host
4. Usare le variabili d'ambiente per definire la stringa di connessione al database (postgres)
5. Creare una bind mount **./mysite** per modificare i files

### Servizio 2: PostresSQL

1. Usare l'immagine **postgres**
2. Creare un volume **con nome** che punti alla cartella **/var/lib/postgresql/data**
3. Usare le variabili d'ambiente per la configurazione
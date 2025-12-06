# task2/back-end/Dockerfile

# Əsas şəkil: Python-un yüngül versiyasını istifadə edin
FROM python:3.9-slim

# Ətraf Mühit Dəyişənləri (Isteğe bağlı, amma yaxşı praktikadır)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Kapsayıcı daxilində işçi qovluğu təyin edin
WORKDIR /usr/src/app

# Flask və digər asılılıqları quraşdırmaq üçün tələb olunanlar.
# Task 1-də tələb olunan "upgrade" burada lazım deyil, çünki Python əsas şəklini istifadə edirik.
# Əgər requirements.txt istifadə etsəydiniz, bu əmr lazım olardı.
RUN pip install Flask

# Tətbiqin kodunu kapsayıcıya kopyalayın
COPY api.py .

# Flask tətbiqinin dinləyəcəyi portu ifşa edin
EXPOSE 5000

# Tətbiqi işə salan əmr
CMD ["python", "api.py"]

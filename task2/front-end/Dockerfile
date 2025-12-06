# Dockerfile

# Ən son Nginx şəklini istifadə edin
FROM nginx:latest

# softy-pinko-front-end qovluğunu tələb olunan yerə kopyalayın
# Nginx-in standart root kataloqu /usr/share/nginx/html/ olsa da, 
# təlimatda /var/www/html/softy-pinko-front-end tələb olunur.
COPY softy-pinko-front-end /var/www/html/softy-pinko-front-end

# softy-pinko-front-end.conf konfiqurasiya faylını 
# Nginx-in standart konfiqurasiya yerinə kopyalayın (mövcud default.conf-u əvəz edir)
COPY softy-pinko-front-end.conf /etc/nginx/conf.d/default.conf

# Kapsayıcı Nginx-in standart portu olan 80-i ifşa etsə də, 
# Nginx konfiqurasiyamız 9000-i dinləyir.
# Bu təlimat isteğe bağlıdır, çünki Nginx əsas şəkilindədir, 
# lakin aydınlıq üçün saxlanıla bilər.
EXPOSE 9000

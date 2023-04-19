# DRF-JWT-OAuth2

DRF와 JWT를 이용해서 Oauth2 소셜로그인기능 구현

## installation


### makefile  .env
```
# django
SECRET_KEY = ""

# database
DB_NAME = "DB_NAME"
DB_HOST = "DB_HOST"
DB_PORT = "DB_PORT"
DB_USER = "DB_USER"
DB_PASSWORD = "DB_PASSWORD"

# google socialaccount
SOCIAL_AUTH_GOOGLE_CLIENT_ID = ""
SOCIAL_AUTH_GOOGLE_SECRET = ""
STATE = ""

# kakao socialaccount
SOCIAL_AUTH_KAKAO_CLIENT_ID = ""
SOCIAL_AUTH_KAKAO_SECRET = ""

# google socialaccount
SOCIAL_AUTH_GITHUB_CLIENT_ID = ""
SOCIAL_AUTH_GITHUB_SECRET = ""
```

### make superuser
```
python manage.py createsuperuser
```

### host/admin setup
1) change site

![image](https://user-images.githubusercontent.com/36651040/232979510-733aa08b-ec9d-4392-9a19-451e4fccf321.png)

2) add socialapp

![image](https://user-images.githubusercontent.com/36651040/232979667-bab87691-04a9-41f8-9469-902c9b6742a3.png)




## TEST
host/account/google/login

host/account/kakao/login

host/account/github/login

host/account/naver/login






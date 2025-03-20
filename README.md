How to run -  
1) clone repo
2) swtich to develop branch
3) Install Docker desktop from internet
3) Run `docker compose up` in terminal to get up the env
4) If `db` is up and not `django_live` then run below command in psql 
     ``CREATE COLLATION case_insensitive (provider = icu, locale = 'und-u-ks-level2', deterministic = false);``
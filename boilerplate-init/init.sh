#!/bin/bash


# Initiate Docker Compose file
touch ../docker-compose.yml
mkdir ../.envs
touch ../.envs/.env
touch ../src/entrypoint.sh


printf '#This is primary docker-compose file for selected services.\n\n' >> ../docker-compose.yml
printf "version: '3.6'\n\n" >> ../docker-compose.yml
printf "services:\n" >> ../docker-compose.yml


# Get project name
read -p "Name your project: " project_title


# Select DB
PS3='Select what type of database: '
options=("PostgreSQL")
select db_opt in "${options[@]}"
do
    case $db_opt in
        "PostgreSQL")
            ./postgres.sh
            break
            ;;
        *) exit;;
    esac
done


# Select Cache
PS3='Select what type of cache: '
options=("Redis" "Database")
select cache_opt in "${options[@]}"
do
    case $cache_opt in
        "Redis")
            ./redis.sh
            cache_type="Redis"
            break
            ;;
        "Database")
            cache_type="Database"
            break
            ;;
        *) exit;;
    esac
done

# Init Django
./django.sh


# Add requirements based on selections
req_file="../src/requirements.txt"

if [ $cache_type == "Redis" ]
then
    printf 'django-redis==4.11.0' >> $req_file
fi
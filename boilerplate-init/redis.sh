#!/bin/bash


dc_file="../docker-compose.yml"
env_file="../.envs/.env"


# Generate code for PostgreSQL service
printf "  redis:\n" >> $dc_file
printf "    container_name: redis\n" >> $dc_file
printf "    image: redis:5.0.7-alpine\n" >> $dc_file
printf "    env_dc_file:\n" >> $dc_file
printf "      - ./.envs/.env\n" >> $dc_file
printf "    volumes:\n" >> $dc_file
printf "      - redis_data:/var/lib/redis/data/\n" >> $dc_file
printf "    ports:\n" >> $dc_file
printf "      - 6378:6379\n" >> $dc_file
printf "    networks:\n" >> $dc_file
printf "      - net\n" >> $dc_file
printf "\n" >> $dc_file


# Generate code for PostgreSQL service
printf "\n" >> $env_file
printf "REDIS_HOST=redis\n" >> $env_file



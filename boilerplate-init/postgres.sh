#!/bin/bash


dc_file="../docker-compose.yml"
env_file="../.envs/.env"


# Generate code for PostgreSQL service
printf "  db:\n" >> $dc_file
printf "    container_name: db\n" >> $dc_file
printf "    image: postgres:12.0-alpine\n" >> $dc_file
printf "    env_dc_file:\n" >> $dc_file
printf "      - ./.envs/.env\n" >> $dc_file
printf "    volumes:\n" >> $dc_file
printf "      - postgres_data:/var/lib/postgresql/data/\n" >> $dc_file
printf "    ports:\n" >> $dc_file
printf "      - 5433:5432\n" >> $dc_file
printf "    networks:\n" >> $dc_file
printf "      - net\n" >> $dc_file
printf "\n" >> $dc_file


# Generate code for PostgreSQL service
printf "\n" >> $env_file
printf "POSTGRES_DB=core\n" >> $env_file
printf "POSTGRES_USER=system_handler\n" >> $env_file
printf "POSTGRES_PASSWORD=hje((*%518dgvrt+*^\n" >> $env_file
printf "SQL_HOST=db\n" >> $env_file
printf "SQL_PORT=5432\n" >> $env_file
printf "DATABASE=postgres\n" >> $env_file






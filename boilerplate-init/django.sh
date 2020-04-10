#!/bin/bash

#!/bin/bash


dc_file="../docker-compose.yml"
ep_file="../src/entrypoint.sh"
env_file="../.envs/.env"
req_file="../src/requirements.txt"


# Generate code for PostgreSQL service
printf "  app:\n" >> $dc_file
printf "    container_name: core\n" >> $dc_file
printf "    build:\n" >> $dc_file
printf "      context: ./src\n" >> $dc_file
printf "      dockerfile: Dockerfile\n" >> $dc_file
printf "    command: python -u manage.py runserver 0.0.0.0:8000\n" >> $dc_file
printf "    env_dc_file:\n" >> $dc_file
printf "      - ./.envs/.env\n" >> $dc_file
printf "    volumes:\n" >> $dc_file
printf "      ./src:/usr/src/app\n" >> $dc_file
printf "    ports:\n" >> $dc_file
printf "      - 8000:8000\n" >> $dc_file
printf "    networks:\n" >> $dc_file
printf "      - net\n" >> $dc_file
printf "    depends_on:\n" >> $dc_file
printf "      - db\n" >> $dc_file
printf "      - redis\n" >> $dc_file
printf "    links:\n" >> $dc_file
printf "      - db\n" >> $dc_file
printf "      - redis\n" >> $dc_file
printf "    restart: always\n" >> $dc_file
printf "\n" >> $dc_file



# Want to use Tenants?
PS3='Do you want to implement tenants?: '
options=("Yes" "No")
select db_opt in "${options[@]}"
do
    case $db_opt in
        "Yes")
            printf "SQL_ENGINE=tenant_schemas.postgresql_backend\n" >> $env_file
            tenant=1
            break
            ;;
        "Yes")
            printf "SQL_ENGINE=django.db.backends.postgresql\n" >> $env_file
            tenant=0
            break
            ;;
        *) exit;;
    esac
done


# Generate entrypoint
printf "#!/bin/sh\n\n" >> $ep_file
printf '
if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."
    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done
    echo "PostgreSQL started"
fi \n\n' >> $ep_file
printf '
mkdir static/media
python manage.py makemigrations
' >> $ep_file


if [ $tenant == 1 ]
then
    printf '
    python manage.py migrate_schemas
    echo "Stage:"
    echo ${VERSION}
    python manage.py create_public_tenant --${VERSION}
    python manage.py migrate_schemas --executor=parallel
    ' >> $ep_file
else
    printf 'python manage.py migrate' >> $ep_file
fi


printf '
python manage.py collectstatic --no-input --clear
exec "$@"
' >> $ep_file


# Add requirements based on selections
if [ $tenant == 1 ]
then
    printf 'django-tenant-schemas==1.10.0' >> $req_file
fi
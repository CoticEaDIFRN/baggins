#!/bin/bash
#
# Deploy the PTD applications.

source env.sh

deploy_laravel()
{
  echo_info "Deploying $i..."
  if [[ ! -f "../apps/$i/.env" ]]; then
    cp ../apps/$i/$ENVFILE ../apps/$i/.env
  fi
  docker-compose run $1 composer install
  if [[ -z "$(grep APP_KEY ../apps/$i/.env | head -1 | cut - -d = -f 2)" ]]; then
    docker-compose run $i php artisan key:generate
  fi
  docker-compose run $1 php artisan migrate --seed --force
  docker-compose run $1 chown :www-data -R storage
  docker-compose run $1 chmod 775 -R storage
  docker-compose run $1 php artisan sentry:message "Deployed"
}

if [[ $# -ne 0 ]]; then
  SERVICES=($1);
fi

./down.sh
./build.sh --dev $1
./init_infra.sh
for i in "${SERVICES[@]}"; do
  deploy_laravel $i
done
./down.sh

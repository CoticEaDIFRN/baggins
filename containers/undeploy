#!/bin/bash
#
# Undeploy the PTD applications.

source env.sh

./down.sh
rm -f .env
for i in "${SERVICES[@]}"; do
  echo_info "Undeploying $i..."
  rm -f ../apps/$i/.env
  rm -rf ../apps/$i/vendor
done


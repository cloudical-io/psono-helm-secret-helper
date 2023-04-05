#!/bin/bash

SERVICEACCOUNT_TOKEN=`cat /var/run/secrets/kubernetes.io/token`

SECRET_NAME="${SECRET_NAME:-psono-secret}"
RELEASE_NAMESPACE="${RELEASE_NAMESPACE:-psono}"

create_kubeconf () {
    sed "s|SATOKEN|$SERVICEACCOUNT_TOKEN|" config > $(pwd)/kubeconfig
}

create_psono_secret () {
    /usr/bin/python3 create-psono-secrets.py
    kubectl -n $RELEASE_NAMESPACE create secret generic $SECRET_NAME --from-env-file secrets.env
}

create_kubeconf

create_psono_secret

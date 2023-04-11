# Psono Secret Helper

This Repo contains helper scripts creating secrets for a PSONO deployment via the Helmchart https://github.com/cloudical-io/psono-helm-chart

It uses a all in one k8s image to create the secrets on the cluster via the mounted Service Account Token.

## Scripts and files

> create-secret.sh

Creates the `kubeconfig` for the `kubectl` command and creates the secret on the k8s cluster

> create-psono-secrets.py

Creates the ENV Vars and its contents according to the PSONO specifications

> config

A Template file to be used for the generated `kubeconfig`

## Usage

If you want to use the image by itself by using the folowing manifest but change the Service Account and env-variables

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: psono-secret-creator
spec:
  template:
    spec:
      # CHANGE THIS TO A VALID SERVICE ACCOUNT
      serviceAccountName: "PSONO-SERVICE-ACCOUNT"
      automountServiceAccountToken: true
      restartPolicy: Never
      containers:
        - name: secret-creator
          image: harbor.cloudical.net/cci-tools/psono-helm-secret-helper:latest
          env:
            # Fill in your values
            - name: RELEASE_NAMESPACE
              value: YOUR_NAMESPACE
            - name: SECRET_NAME
              value: YOUR_SECRET_NAME
```
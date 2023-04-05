FROM docker.io/alpine/k8s:1.26.3

RUN pip3 install pynacl bcrypt

COPY ["config", "create-psono-secrets.py", "create-secret.sh", "/apps/"]

ENTRYPOINT ["/bin/bash", "./create-secret.sh"]

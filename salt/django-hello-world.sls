django_hello-world-image:
  docker.pulled:
    - name: mruediger/django_hello-world:latest

django_hello-world-container:
  docker.installed:
    - image: mruediger/django_hello-world
    - watch:
      - docker: django_hello-world-image

django_hello-world:
  docker.running:
    - image: mruediger/django_hello-world
    - ports:
        - "8000/tcp":
            HostIp: ""
            HostPort: "80"
    - watch:
      - docker: django_hello-world-container

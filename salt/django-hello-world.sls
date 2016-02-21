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
    - container: mruediger/django_hello-worl
    - hostname: mruediger/django_hello-world
    - watch:
      - docker: django_hello-world-container
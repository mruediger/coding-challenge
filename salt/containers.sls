dubsmash-django-image:
  docker.pulled:
    - name: mruediger/dubsmash-django
    - tag: latest

dubsmash-django-container:
  docker.installed:
    - image: mruediger/dubsmash-django
    - watch:
      - docker: dubsmash-django-image

dubsmash-django:
  docker.running:
    - image: mruediger/dubsmash-django
    - container: dubsmash-django
    - hostname: dubsmash-django
    - watch:
      - docker: dubsmash-django-container
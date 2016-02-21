Dubsmash Challenge
==================

I have never used any of the tools/libraries/projects myself. It was an interesting experience and I learned more than in every coding challenge I had before. Thanks!

## Project Structure

The root folder holds everything Vagrant needs to work. The Salt setup is in the folder ``salt`` and everything that is needed for Django, including the Dockerfile, is found under ``django_hello-world``

## Django

The web app just returns "Hello World. Hello Dubsmash!". I tried to get fancy using the fortune library in combination with a Serenity/Firefly themed fortune file, but I encountered a bug and chose to focus on the rest of the challenge instead.

## Docker

The Dockerfile is a simple modification of https://github.com/docker-library/django/blob/master/2.7/onbuild/Dockerfile. I chose to remove the handling of the``requirements.txt`` file. It is a well established pattern in the python world, but maintaining dependencies in two different places feels very error prone to me. A built version of this Docker image can be found ``https://hub.docker.com`` under ``mruediger/django_hello-world``.

## Salt

I have had a hard time wrapping my head around the differences between *State*, *State* Declaration* and *State Function*. As a result my *Formulas* might look funny.

I also had some trouble getting ``dockerng`` and ``dockerio`` working. In the end didn't use ``dockerng`` because ``dockerng.running`` didn't pull the image advertised (https://github.com/saltstack/salt/issues/29727). Working around this issue using ``dockerng.image_present`` meant I had to use my credentials (https://github.com/saltstack/salt/issues/28004) - something I tried to avoid since the image is publicly accessible.

The older, soon to be deprecated ``dockerio`` worked - till I tried to update the docker image. Using the ``docker.pulled`` with the ``force`` parameter produced an error when running ``docker.pull`` that I couldn't resolve. I had to omit the parameter which results in Salt not noticing image updates. Only having 1 whole day of Salt experience, I did not file an issue on Github. The most probable cause in my opinion is a case of pebkac.

I intentionally avoided using variables throughout the Formulas. With only one service running, they only provide confusion and no benefit. As a long time Java developer, I often saw what happens if you try to abstract code before knowing where it will go.

All that said, I really liked working with Salt. The folder layout makes a lot more sense in Salt than in Ansible and the documentation is definitely better.

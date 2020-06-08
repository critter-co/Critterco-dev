[![Build Status](https://travis-ci.com/critter-co/critterco-dev.svg?branch=master)](https://travis-ci.com/critter-co/critterco-dev)
# Critter 
Temporary repository for Critter app development. 

## Software Requirements.
- Docker > v19.03

## Working on the project.

### How to run the app.
- Make sure Docker engine is running.
- [For Linux] Make sure you can run sudo commands or your user is in docker group, and you have docker-compose installed.
- Open a terminal and navigate to project directory where "docker-compose.yml" file resides.
- Run ```docker-compose up --build```; wait for docker to download and build images.
- You can access API endpoint at "localhost/api/", and frontend at "localhost".
- Portainer is accessible at "localhost:9000". Make sure you create an admin account before 5 minutes or container stops.
- Redis-commander is accessible at "localhost:8085" for monitoring redis caches.
- Endpoint documentation will be added at a later date here (most probably Postman Documenting).

## Phase A

### Frontend todos.
- [ ] Implement testing modules/libraries and coverage reports for TDD.
- [ ] Configure TravisCI for frontend tests/build report on each push.
- [ ] Add basic landing page using bootstrap/? based on given design templates, including header, main body, footer.
- [ ] Implement authentication system using VueX. 
- [ ] Handle user profile management functions (logout, edit info, etc.).
- [ ] Add user profile template based on user profile management functions.
- [ ] Add a map API for nearby businesses/services viewing.
- [ ] Load data from biz API to map.
- [ ] Filter businesses/services by location according to API search queries.

### Backend todos.
- [x] Add a consistant test method or library (such as pytest, paramteraized.). [commit](https://github.com/critter-co/critterco-dev/commit/4095c7526588ea001ab4677c7efde27e456970d8 "Fixing commit") 
- [x] Cover tests for existing functions (+90% coverage). [commit](https://github.com/critter-co/critterco-dev/commit/0ff5bd451da2900c910ae10f399be260a5721e29 "Fixing commit") 
- [x] Implement flake8, and configure it for needed files; fix linting errors. [commit](https://github.com/critter-co/critterco-dev/commit/5104dc88efedbc58d2c954445517cb1f6bfd8286 "Fixing commit")
- [ ] Add Celery for asynchronous tasks such as sending emails for confirmation/password reset.
- [ ] Add automated password reset via email through Celery.
- [ ] Implement email confirmation at signup.
- [x] Configure django's setting to cache biz queries via Redis. [commit](https://github.com/critter-co/critterco-dev/commit/5037049df12288ce1722da5c04a060c7ea2b1bcd "Fixing commit")
- [ ] Move all django apps to an "apps" folder for a cleaner environment.
- [x] Move all scripts to a "scripts" folder, and make sure docker works properly with new paths. [commit](https://github.com/critter-co/critterco-dev/commit/dd1810a584648f84cf960cb0da3ba8a0702dd399 "Fixing commit") 

### Build (or Docker) todos.
- [ ] Fix the error with pgadmin (not working after adding nginx.).
- [ ] Add Celery for asynchronous backend tasks.
- [x] Add Redis for caching. [commit](https://github.com/critter-co/critterco-dev/commit/96b7ae7bbb325af4a3b4e5b0c83ea477b8dabb51 "Fixing commit") 
- [ ] [FAILED] Replace nginx with Traefik if it offers better solution for https and certs.

### Phase A Ending:
- [ ] Web has a frontend that shows User info/Biz info.
- [ ] Users can post and edit Biz, and update their info, according to permissions.
- [ ] Users can request "forgot password" and do it via email confirmation.
- [ ] User location is determined via IP/permission for gps info. Or they select location.
- [ ] Nearby Bizs will be shown on a map.
- [ ] Users can comment on each biz and these comments show up on Biz pages.

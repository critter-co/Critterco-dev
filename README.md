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
- **IMPORTANT** make sure u rename the file ".env_example" to ".env" and write desired environment variables.
- Run ```docker-compose up --build```; wait for docker to download and build images.
- You can access API endpoint at "localhost/api/", and frontend at "localhost".
- Portainer is accessible at "localhost:9000". Make sure you create an admin account before 5 minutes or container stops.
- Redis-commander is accessible at "localhost:8085" for monitoring redis caches.
- [API endpoints documentation](https://documenter.getpostman.com/view/10900080/SzzdC1NW) .

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
- [x] Add a consistant test method or library (such as pytest, paramteraized.). [commit](https://github.com/critter-co/critterco-dev/commit/4095c7526588ea001ab4677c7efde27e456970d8 "Job commit") 
- [x] Cover tests for existing functions (+90% coverage). [commit](https://github.com/critter-co/critterco-dev/commit/0ff5bd451da2900c910ae10f399be260a5721e29 "Job commit") 
- [x] Implement flake8, and configure it for needed files; fix linting errors. [commit](https://github.com/critter-co/critterco-dev/commit/5104dc88efedbc58d2c954445517cb1f6bfd8286 "Job commit")
- [x] Add Celery for asynchronous tasks such as sending emails for confirmation/password reset. [commit](https://github.com/critter-co/critterco-dev/commit/28cc5ec9ddfb3212d5d08e91436997f7fdafba9a "Job commit")
- [x] Add automated password reset via email through Celery. [commit](https://github.com/critter-co/critterco-dev/commit/508474206fe969df6520cacee683b13da408d385 "Job commit")
- [x] Implement email confirmation at signup. [commit](https://github.com/critter-co/critterco-dev/commit/644bbfe8d2ce11e951a98918a0f3c358eefc2d0d "Job commit")
- [x] Configure django's setting to cache biz queries via Redis. [commit](https://github.com/critter-co/critterco-dev/commit/5037049df12288ce1722da5c04a060c7ea2b1bcd "Job commit")
- [x] Move all django apps to an "apps" folder for a cleaner environment. [commit](https://github.com/critter-co/critterco-dev/commit/7abbb0bcf317acc4361c1ebc0650995ab6cbb490 "Job commit")
- [x] Move all scripts to a "scripts" folder, and make sure docker works properly with new paths. [commit](https://github.com/critter-co/critterco-dev/commit/dd1810a584648f84cf960cb0da3ba8a0702dd399 "Job commit") 

### Build (or Docker) todos.
- [x] Fix the error with pgadmin (not working after adding nginx). [commit](https://github.com/critter-co/critterco-dev/commit/10273f283e93219a3a35e04377fe535eb7b652be "Job commit")
- [x] Add Celery for asynchronous backend tasks. [commit](https://github.com/critter-co/critterco-dev/commit/28cc5ec9ddfb3212d5d08e91436997f7fdafba9a "Job commit")
- [x] Add Redis for caching. [commit](https://github.com/critter-co/critterco-dev/commit/96b7ae7bbb325af4a3b4e5b0c83ea477b8dabb51 "Job commit") 
- [x] [FAILED] Replace nginx with Traefik if it offers better solution for https and certs.

### Phase A Ending:
- [ ] Web has a frontend that shows User info/Biz info.
- [ ] Users can post and edit Biz, and update their info, according to permissions.
- [ ] Users can request "forgot password" and do it via email confirmation.
- [ ] User location is determined via IP/permission for gps info. Or they select location.
- [ ] Nearby Bizs will be shown on a map.
- [ ] Users can comment on each biz and these comments show up on Biz pages.

## Phase B

### Android/iOS Apps.
- [ ] Basic app layout with logo, map functionality, sign-up, login.
- [ ] Users able to edit their personal info.
- [ ] Users can post, edit Biz info based on their permissions.
- [ ] App receive live GPS location and update user location info.
- [ ] Show nearby Biz based on location.
- [ ] Direct contact(phone call, etc.) from Biz page if Biz phone number was provided.
- [ ] Users able to write comments, reviews, etc.

### Backend todos.
- [ ] Add user avatar. One image for user profile.
- [ ] Differentiate reviews and comments in separate models/serializers.
- [ ] Add likes/upvotes/reactions to comments and/or reviews.
- [ ] Expand the Gallery of Biz to support multiple images possibly in a separate model.
- [ ] Implement users uploading pictures of Biz.
- [ ] Add editor/owner field to Biz so only owner user(s) can edit info.
- [ ] Add blog/news to Biz (only owners can publish).
- [ ] Add poll/surverys to Biz (only owners can publish).
- [ ] Implement IP blacklists and concurrent request to prevent brute-forcing.
- [ ] Email confirmation/password reset done through LINKS instead of 6-digit codes.
- [ ] Add Biz info from available APIs (Google places, etc.) through web crawling.
- [ ] Add categories/tag feature for Biz to be separated by them.
- [ ] Implement Graphql if needed for specific needs.

### Frontend todos.
- [ ] Use Graphql for needed functionality, if any.
- [ ] Run different performance tests and improve if results aren't satisfying.
- [ ] Implement newly added Backend functions, such as like/reaction, differentiated comment/reviews, etc.

### Build (or Docker) todos.
- [ ] Add https certification(automated cert refresh), through either Nginx or Traefik.
- [ ] Add MongoDB if it's needed for image upload, and gallery management.
- [ ] Network mapping according to services and their communication needs.
- [ ] Implement Docker Swarm for seamless and automated updates.
- [ ] Implement Gitlab CI/CD if the service is better than current Travis CI.
- [ ] Deploy the app on an appropriate host for live beta testing.
- [ ] Run stress performance tests and debug the issues.

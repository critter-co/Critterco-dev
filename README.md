# Critter Project Dev Repository.
Temporary repository for Critter app development.

## Phase A

### Frontend requirements.
- Add basic landing page using bootstrap/? based on given design templates, including header, main body, footer.
- Implement authentication system using VueX. 
- Handle user profile management functions (logout, edit info, etc.).
- Add user profile template based on user profile management functions.
- Add a map API for nearby businesses/services viewing.
- Load data from biz API to map.
- filter businesses/services by location according to API search queries.

### Backend requirements.
- [[DONE]](https://github.com/critter-co/critterco-dev/commit/4095c7526588ea001ab4677c7efde27e456970d8 "Fixing commit") Add a consistant test method or library (such as pytest, paramteraized.).
- [[DONE]](https://github.com/critter-co/critterco-dev/commit/5a4b5fa158f51d579d87585137f1c871d2eebf23) Cover tests for existing functions (+90% coverage).
- [[DONE]](https://github.com/critter-co/critterco-dev/commit/5104dc88efedbc58d2c954445517cb1f6bfd8286 "Fixing commit") Implement flake8, and configure it for needed files; fix linting errors.
- Add Celery for asynchronous tasks such as sending emails for confirmation/password reset.
- Add automated password reset via email through Celery.
- [[DONE]](https://github.com/critter-co/critterco-dev/commit/5037049df12288ce1722da5c04a060c7ea2b1bcd "Fixing commit") Configure django's setting to cache biz queries via Redis.
- Move all django apps to an "apps" folder for a cleaner environment.
- [[DONE]](https://github.com/critter-co/critterco-dev/commit/dd1810a584648f84cf960cb0da3ba8a0702dd399 "Fixing commit") Move all scripts to a "scripts" folder, and make sure docker works properly with new paths.

### Build (or Docker) requirements.
- Fix the error with pgadmin (not working after adding nginx.).
- Add Celery for asynchronous backend tasks.
- [[DONE]](https://github.com/critter-co/critterco-dev/commit/96b7ae7bbb325af4a3b4e5b0c83ea477b8dabb51 "Fixing commit") Add Redis for caching.
- [FAILED] Replace nginx with Traefik if it offers better solution for https and certs.

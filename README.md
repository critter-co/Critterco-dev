# Critter Project Dev Repository.
Temporary repository for Critter app development.

## Phase A

### Frontend requirements.
- Add basic landing page using bootstrap/? based on given design templates, including header, main body, footer.
- Implement authentication system using VueX. 
- Handle user profile management functions (logout, edit info, etc.)
- Add user profile template based on user profile management functions.
- Add a map API for nearby businesses/services viewing.
- Load data from biz API to map.
- filter businesses/services by location according to API search queries.

### Backend requirements.
- Add a consistant test method or library (such as pytest, paramteraized.)
- Implement flake8, and configure it for needed files; fix linting errors.
- Add Celery for asynchronous tasks such as sending emails for confirmation/password reset.
- Add automated password reset via email through Celery.
- [DONE] Configure django's setting to cache biz queries via Redis.

### Build (or Docker) requirements.
- Fix the error with pgadmin (not working after adding nginx.)
- Add Celery for asynchronous backend tasks.
- [DONE] Add Redis for caching.
- Replace nginx with Traefik if it offers better solution for https and certs.

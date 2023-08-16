# praktikum_new_diplom

```
foodgram-project-react-copy-two
├─ .git
│  ├─ config
│  ├─ description
│  ├─ HEAD
│  ├─ hooks
│  │  ├─ applypatch-msg.sample
│  │  ├─ commit-msg.sample
│  │  ├─ fsmonitor-watchman.sample
│  │  ├─ post-update.sample
│  │  ├─ pre-applypatch.sample
│  │  ├─ pre-commit.sample
│  │  ├─ pre-merge-commit.sample
│  │  ├─ pre-push.sample
│  │  ├─ pre-rebase.sample
│  │  ├─ pre-receive.sample
│  │  ├─ prepare-commit-msg.sample
│  │  ├─ push-to-checkout.sample
│  │  └─ update.sample
│  ├─ index
│  ├─ info
│  │  └─ exclude
│  ├─ logs
│  │  ├─ HEAD
│  │  └─ refs
│  │     ├─ heads
│  │     │  └─ master
│  │     └─ remotes
│  │        └─ origin
│  │           └─ HEAD
│  ├─ objects
│  │  ├─ info
│  │  └─ pack
│  │     ├─ pack-cd856dc77e420e67e33563e3803e4d7c9c8c678e.idx
│  │     └─ pack-cd856dc77e420e67e33563e3803e4d7c9c8c678e.pack
│  ├─ packed-refs
│  └─ refs
│     ├─ heads
│     │  └─ master
│     ├─ remotes
│     │  └─ origin
│     │     └─ HEAD
│     └─ tags
├─ .gitignore
├─ .isort.cfg
├─ backend
│  ├─ .gitkeep
│  ├─ foodgram
│  │  ├─ api
│  │  │  ├─ apps.py
│  │  │  ├─ filters.py
│  │  │  ├─ migrations
│  │  │  │  └─ __init__.py
│  │  │  ├─ pagination.py
│  │  │  ├─ permissions.py
│  │  │  ├─ serializers.py
│  │  │  ├─ urls.py
│  │  │  ├─ views.py
│  │  │  └─ __init__.py
│  │  ├─ data
│  │  │  ├─ ingredients.csv
│  │  │  └─ ingredients.json
│  │  ├─ foodgram
│  │  │  ├─ asgi.py
│  │  │  ├─ settings.py
│  │  │  ├─ urls.py
│  │  │  ├─ wsgi.py
│  │  │  └─ __init__.py
│  │  ├─ manage.py
│  │  ├─ media
│  │  │  └─ recipes
│  │  │     ├─ 0fc00475-d46c-4495-80de-113f69138ab8.jpg
│  │  │     ├─ 59e7a7e8-458f-4775-8c89-1b16b7bf3316.jpg
│  │  │     ├─ 87ccbd5b-8a69-4515-b60a-fe00b88338f5.jpg
│  │  │     ├─ abfa0afe-afc4-438d-aae6-c80a20a47036.jpg
│  │  │     ├─ c1317000-8dcc-4b3e-8599-50f4bf5baaea.jpg
│  │  │     └─ SomkScHX.jpg
│  │  ├─ recipes
│  │  │  ├─ admin.py
│  │  │  ├─ apps.py
│  │  │  ├─ management
│  │  │  │  └─ commands
│  │  │  │     ├─ apps.py
│  │  │  │     ├─ import_csv.py
│  │  │  │     └─ __init__.py
│  │  │  ├─ migrations
│  │  │  │  ├─ 0001_initial.py
│  │  │  │  ├─ 0002_auto_20230816_0155.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ models.py
│  │  │  └─ __init__.py
│  │  └─ users
│  │     ├─ apps.py
│  │     ├─ migrations
│  │     │  ├─ 0001_initial.py
│  │     │  ├─ 0002_auto_20230816_0155.py
│  │     │  └─ __init__.py
│  │     ├─ models.py
│  │     ├─ serializers.py
│  │     ├─ urls.py
│  │     └─ __init__.py
│  └─ requirements.txt
├─ docs
│  ├─ openapi-schema.yml
│  └─ redoc.html
├─ frontend
│  ├─ Dockerfile
│  ├─ package-lock.json
│  ├─ package.json
│  ├─ public
│  │  ├─ favicon.ico
│  │  ├─ favicon.png
│  │  ├─ index.html
│  │  ├─ logo192.png
│  │  ├─ logo512.png
│  │  ├─ manifest.json
│  │  └─ robots.txt
│  ├─ src
│  │  ├─ api
│  │  │  └─ index.js
│  │  ├─ App.css
│  │  ├─ App.js
│  │  ├─ App.test.js
│  │  ├─ components
│  │  │  ├─ account-menu
│  │  │  │  └─ index.js
│  │  │  ├─ button
│  │  │  │  └─ index.js
│  │  │  ├─ card
│  │  │  │  └─ index.js
│  │  │  ├─ card-list
│  │  │  │  └─ index.js
│  │  │  ├─ checkbox
│  │  │  │  └─ index.js
│  │  │  ├─ checkbox-group
│  │  │  │  └─ index.js
│  │  │  ├─ container
│  │  │  │  └─ index.js
│  │  │  ├─ file-input
│  │  │  │  └─ index.js
│  │  │  ├─ footer
│  │  │  │  └─ index.js
│  │  │  ├─ form
│  │  │  │  └─ index.js
│  │  │  ├─ header
│  │  │  │  └─ index.js
│  │  │  ├─ icons
│  │  │  │  ├─ arrow-left
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ arrow-right
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ check
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ clock
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ done
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ index.js
│  │  │  │  ├─ plus
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ star
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ star-active
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ star-big
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ star-big-active
│  │  │  │  │  └─ index.js
│  │  │  │  └─ user
│  │  │  │     └─ index.js
│  │  │  ├─ index.js
│  │  │  ├─ ingredients-search
│  │  │  │  └─ index.js
│  │  │  ├─ input
│  │  │  │  └─ index.js
│  │  │  ├─ link
│  │  │  │  └─ index.js
│  │  │  ├─ main
│  │  │  │  └─ index.js
│  │  │  ├─ nav
│  │  │  │  └─ index.js
│  │  │  ├─ pagination
│  │  │  │  ├─ arrow-left.png
│  │  │  │  ├─ arrow-right.png
│  │  │  │  └─ index.js
│  │  │  ├─ protected-route
│  │  │  │  └─ index.js
│  │  │  ├─ purchase
│  │  │  │  └─ index.js
│  │  │  ├─ purchase-list
│  │  │  │  └─ index.js
│  │  │  ├─ subscription
│  │  │  │  └─ index.js
│  │  │  ├─ subscription-list
│  │  │  │  └─ index.js
│  │  │  ├─ tag
│  │  │  │  └─ index.js
│  │  │  ├─ tags-container
│  │  │  │  └─ index.js
│  │  │  ├─ textarea
│  │  │  │  └─ index.js
│  │  │  └─ title
│  │  │     └─ index.js
│  │  ├─ configs
│  │  │  ├─ colors.js
│  │  │  └─ navigation.js
│  │  ├─ contexts
│  │  │  ├─ auth-context.js
│  │  │  ├─ index.js
│  │  │  ├─ recipes-context.js
│  │  │  └─ user-context.js
│  │  ├─ images
│  │  │  └─ hamburger-menu.png
│  │  ├─ index.css
│  │  ├─ index.js
│  │  ├─ logo.svg
│  │  ├─ pages
│  │  │  ├─ cart
│  │  │  │  └─ index.js
│  │  │  ├─ change-password
│  │  │  │  └─ index.js
│  │  │  ├─ favorites
│  │  │  │  └─ index.js
│  │  │  ├─ index.js
│  │  │  ├─ main
│  │  │  │  └─ index.js
│  │  │  ├─ recipe-create
│  │  │  │  └─ index.js
│  │  │  ├─ recipe-edit
│  │  │  │  └─ index.js
│  │  │  ├─ signin
│  │  │  │  └─ index.js
│  │  │  ├─ signup
│  │  │  │  └─ index.js
│  │  │  ├─ single-card
│  │  │  │  ├─ description
│  │  │  │  │  └─ index.js
│  │  │  │  ├─ index.js
│  │  │  │  └─ ingredients
│  │  │  │     └─ index.js
│  │  │  ├─ subscriptions
│  │  │  │  └─ index.js
│  │  │  └─ user
│  │  │     └─ index.js
│  │  ├─ reportWebVitals.js
│  │  ├─ setupTests.js
│  │  └─ utils
│  │     ├─ hex-to-rgba.js
│  │     ├─ index.js
│  │     ├─ use-recipe.js
│  │     ├─ use-recipes.js
│  │     ├─ use-subscriptions.js
│  │     ├─ use-tags.js
│  │     └─ validation.js
│  └─ yarn.lock
├─ infra
│  ├─ docker-compose.yml
│  └─ nginx.conf
├─ pyproject.toml
└─ README.md

```
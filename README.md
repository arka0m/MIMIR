<div align="center">
<img src="./core/static/favicon.ico" alt="MIMIR_logo">
</div>

# MIMIR project - Massive Information Management for Incident Response


Work in progress

## 1. How to install ?

### 1.1 Requirements

All tests were performed in a Linux environment, but the project is based on Docker containers, so it is portable.

* docker
* docker compose
* User must be docker group member. (restart needed)

### 1.2 Installation

#### 1.2.a Internet connected environment

```
git clone https://github.com/arka0m/MIMIR
cd MIMIR
docker-compose build
docker-compose up
docker exec -it MIMIR_web /bin/bash
* ./manage.py makemigrations
* ./manage.py migrate
* exit
docker-compose down
```

Please note: This is strongly recommended that you modify the SECRET KEY in Django project before using it in production.

#### 1.2.b Air-grapped network

* Create a bundle or download bundle_MIMIR.tar.gz -> **bundle not published yet, but available on demand.**
  * To create a bundle : Follow "Internet connected environment" instruction, then use docker save to build a bundle.

```
tar -xzvf bundle_MIMIR.tar.gz
docker load -i MIMIR-containers.tar.gz
cd MIMIR
docker-compose up
docker exec -it MIMIR_web /bin/bash
* ./manage.py makemigrations
* ./manage.py migrate
* exit
docker-compose down
```

## 2. How to run and use ?

### 2.1 Get started

* To launch MÌMIR :
```
cd MIMIR
docker-compose up
```

* To stop MÌMIR : 
```
Ctrl+C
```

Please note that the Postgres database is not persistent. **Docker-compose down will result in the loss of all data in the database.**


## 3. How to participate ?

### 3.1 Commit at the end of each feature modification

In order to easily track each change, please commit/push after EACH feature-specific change block. (Whit a specific comment of course)

### 3.2 Commit message must respect the following format:

```
type : subject

body
```
1. **Type** : Could be one of the following term:
      * feat : New feature
      * refactor : Refactoring a specific section of the codebase
      * fix : Bug fix
      * style : Feature and updates related to styling
      * test : Everything related to testing
      * docs : Everything related to documentation
2. **Subject** : Short description of the changes made 
3. **body** : It is used to explain changes (optional)

## 4. License

**Author : ArkaØm**<br/>
*Contact: arka0m@protonmail.com*

This project is protected under licence Creative Common BY-NC-SA 4.0.

* **BY** : Attribution <p align="justify"> You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.</p>
* **NC** : NonCommercial <p align="justify"> You may not use the material for commercial purposes.</p>
* **SA** : ShareAlike <p align="justify"> If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original. <p>

<div align="center">
<img src="./core/static/core/images/CC_BY-NC-SA.png" alt="CC BY-NC-SA 4.0">
</div>

> The project template is based on an HTML5UP template protected by the CC BY 3.0 license.
> ![HTML5UP_Logo](./core/static/core/images/HTML5UP.png)

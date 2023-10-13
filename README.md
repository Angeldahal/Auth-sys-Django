<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>Auth-sys-Django</h1>
<h3>◦ Authentication System in Django and Vue</h3>
<h3>◦ Developed with the software and tools below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style&logo=JavaScript&logoColor=black" alt="JavaScript" />
<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style&logo=HTML5&logoColor=white" alt="HTML5" />
<img src="https://img.shields.io/badge/Axios-5A29E4.svg?style&logo=Axios&logoColor=white" alt="Axios" />
<img src="https://img.shields.io/badge/Vue.js-4FC08D.svg?style&logo=vuedotjs&logoColor=white" alt="Vue.js" />
<img src="https://img.shields.io/badge/ESLint-4B32C3.svg?style&logo=ESLint&logoColor=white" alt="ESLint" />

<img src="https://img.shields.io/badge/Python-3776AB.svg?style&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/TypeScript-3178C6.svg?style&logo=TypeScript&logoColor=white" alt="TypeScript" />
<img src="https://img.shields.io/badge/Django-092E20.svg?style&logo=Django&logoColor=white" alt="Django" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style&logo=Markdown&logoColor=white" alt="Markdown" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style&logo=JSON&logoColor=white" alt="JSON" />
</p>
<img src="https://img.shields.io/github/license/Angeldahal/Auth-sys-Django?style&color=5D6D7E" alt="GitHub license" />
<img src="https://img.shields.io/github/last-commit/Angeldahal/Auth-sys-Django?style&color=5D6D7E" alt="git-last-commit" />
<img src="https://img.shields.io/github/commit-activity/m/Angeldahal/Auth-sys-Django?style&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/languages/top/Angeldahal/Auth-sys-Django?style&color=5D6D7E" alt="GitHub top language" />
</div>

---

## 📖 Table of Contents
- [📖 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [⚙️ Modules](#modules)
- [🚀 Getting Started](#-getting-started)
    - [🔧 Installation](#-installation)
    - [🤖 Running Auth-sys-Django](#-running-Auth-sys-Django)
    - [🧪 Tests](#-tests)
- [🛣 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The repository contains the basic authentication system in Django and Vue. The vue-auth is the frontend of the project and auth_sys is the backend of the project.
The project is a learning project and is not intended to be used in production.
But, you can use it as a reference for your project.
---


## 📂 Repository Structure

```sh
└── Auth-sys-Django/
    ├── .gitignore
    ├── README.md
    ├── auth_sys/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── core/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── authentication.py
    │   ├── exceptions.py
    │   ├── migrations/
    │   ├── models.py
    │   ├── serializers.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── manage.py
    ├── package-lock.json
    ├── package.json
    ├── requirements.txt
    └── vue-auth/
        ├── .browserslistrc
        ├── .eslintrc.js
        ├── README.md
        ├── babel.config.js
        ├── package-lock.json
        ├── package.json
        ├── public/
        ├── src/
        ├── tsconfig.json
        └── vue.config.js
```


---

## 🚀 Getting Started


### 🔧 Installation

1. Clone the Auth-sys-Django repository:
```sh
git clone https://github.com/Angeldahal/Auth-sys-Django
```

2. Change to the project directory:
```sh
cd Auth-sys-Django
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

### 🤖 Running Auth-sys-Django

```sh
python manage.py runserver
```


---



## 🤝 Contributing

Contributions are always welcome! Please follow these steps:
1. Fork the project repository. This creates a copy of the project on your account that you can modify without affecting the original project.
2. Clone the forked repository to your local machine using a Git client like Git or GitHub Desktop.
3. Create a new branch with a descriptive name (e.g., `new-feature-branch` or `bugfix-issue-123`).
```sh
git checkout -b new-feature-branch
```
4. Make changes to the project's codebase.
5. Commit your changes to your local branch with a clear commit message that explains the changes you've made.
```sh
git commit -m 'Implemented new feature.'
```
6. Push your changes to your forked repository on GitHub using the following command
```sh
git push origin new-feature-branch
```
7. Create a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
The project maintainers will review your changes and provide feedback or merge them into the main branch.

---


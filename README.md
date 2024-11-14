<p align="center"><h1 align="center">REFLECTIFY</h1></p>
<p align="center">
	<em>Mirrors your GitHub followers effortlessly.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/1etu/reflectify?style=flat-square&logo=opensourceinitiative&logoColor=white&color=d8af0f" alt="license">
	<img src="https://img.shields.io/github/last-commit/1etu/reflectify?style=flat-square&logo=git&logoColor=white&color=d8af0f" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/1etu/reflectify?style=flat-square&color=d8af0f" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/1etu/reflectify?style=flat-square&color=d8af0f" alt="repo-language-count">
</p>
<p align="center">Built with the tools and technologies:</p>
<p align="center">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python">
</p>
<br>

##  Table of Contents

- [ Overview](#-overview)
- [ Features](#-features)
- [ Getting Started](#-getting-started)
  - [ Prerequisites](#-prerequisites)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
- [ Contributing](#-contributing)
- [ License](#-license)

---

##  Overview

Reflectify is a Python-based tool designed to manage your GitHub followers and following lists. It automates the process of following back users who follow you and unfollowing users who do not follow you back. The tool uses the GitHub API to fetch follower and following data, and it provides a command-line interface for easy interaction. Reflectify can run in a continuous sync mode to keep your follower list up-to-date in real-time.

---

##  Features

- **Automated Follow Back**: Automatically follow users who follow you.
- **Automated Unfollow**: Automatically unfollow users who do not follow you back.
- **Sync Mode**: Continuously sync your followers and following lists.
- **Command-Line Interface**: Easy-to-use CLI for managing the tool.
- **Logging**: Detailed logging of follow and unfollow actions.
- **Rate Limiting**: Adheres to GitHub API rate limits to avoid being blocked.
- **Configuration**: Easily configurable via environment variables and constants.

---

##  Getting Started

###  Prerequisites

Before getting started with reflectify, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Pip


###  Installation

Install reflectify using one of the following methods:

**Build from source:**

1. Clone the reflectify repository:
```sh
❯ git clone https://github.com/1etu/reflectify
```

2. Navigate to the project directory:
```sh
❯ cd reflectify
```

3. Install the project dependencies:


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r requirements.txt
```




###  Usage
Run reflectify using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python -m src.bOT
```

---

##  Contributing

- **🐛 [Report Issues](https://github.com/1etu/reflectify/issues)**: Submit bugs found or log feature requests for the `reflectify` project.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/1etu/reflectify
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/1etu/reflectify/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=1etu/reflectify">
   </a>
</p>
</details>

---

##  License

This project is protected under the [MIT License](https://choosealicense.com/licenses/mit/). For more details, refer to the [LICENSE](https://choosealicense.com/licenses/mit/) file.

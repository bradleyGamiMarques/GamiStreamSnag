# 📦 Gami's Stream Snag

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![VSCode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)

## 🌟 Highlights

- A beautiful UI wrapper for the [yt-dlp](https://github.com/yt-dlp/yt-dlp) command line tool
- Written in Python using tkinter

## ℹ️ Overview

Hey there! 👋

The idea for this project came about when Twitch announced a 100-hour storage limit on uploads and highlights, starting April 19, 2025. [Read the announcement here](https://help.twitch.tv/s/article/video-on-demand?language=en_US#storage).

Unfortunately, Twitch isn’t offering a way to bulk download videos before they start deleting them. The platform has stated that content will be removed based on view count, starting with the least-watched highlights until a channel is within the limit.

I created Gami's Stream Snag to provide a beautiful, user-friendly GUI for working with yt-dlp. Not everyone is comfortable with command-line tools, so I wanted to make the task of preserving video content as accessible as possible.

### ✍️🔥 Authors

Bradley Andrew Marques


## ⬇️ Installation
### 🚧 Under Construction - Pardon our dust 🚧 🙇🏾


## 💭 Feedback and Contributing

### 🚧 Under Construction - Pardon our dust 🚧 🙇🏾

Consider looking through our [Issues page](https://github.com/bradleyGamiMarques/GamiStreamSnag/issues) for ways to contribute to the project.


## Getting Started 🏃🏾
In this project I am using a combination of [pyenv](https://github.com/pyenv/pyenv) and [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) to keep my system Python and my development environments separate.
To keep our development environments in sync please make sure to have these tools installed.

1. Clone the repository to your development machine.
2. In your terminal navigate to the project and run the following commands in order.
```sh
pyenv install $(cat .python-version)
```
```sh
pyenv virtualenv $(cat .python-version) GamiStreamSnag
```
```sh
pyenv activate GamiStreamSnag
```
```sh
pip install -r requirements.txt
```
3. Please follow the branch naming convention of `<category>/<issue-number>-<short-description>`

<strong> Category is one of `[ chore | docs | feature | fix | refactor | release ]` </strong>

<strong> issue-number is optional but refers to our issues page </strong>

<strong> short-description is a kebab-case description of what the branch is for </strong>

4. The ideal development workflow when working on this project should be
- Checkout a branch from main using the above rules
- Implement your change
- Push your change to the remote
- Open a Pull Request into main
- Once reviewed and approved it will be merged into main with a merge commit.
- Please integrate upstream changes from main into your feature branches using rebase

5. Please follow the [seven rules](https://cbea.ms/git-commit/#seven-rules) of a great Git commit message

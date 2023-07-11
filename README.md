[![Relovista][relovista-logo]
# Relovista
## Telegram bot

![Pipeline badge][badge-pipeline]
![Coverage badge][badge-coverage]

## Agenda
* [Supported languages](#supported-languages)
* [Demo](#demo)
* [How to use](#how-to-use)
* [Features](#features)
* [Requirements](#requirements)

Relovista is a special bot created to help professionals from various fields move to other countries.

## Supported languages
1) English
2) Russian

## Demo
[Demo video][demo-link]


## How to use
[Deployed version of Telegram bot][telegram-bot-link]<br>
[Local version of Telegram bot (**local run is required**)][telegram-test-bot-link]


## Features

### Five main sections:
* #### Destination search<br>
Destination search is search by country/city.
* #### Profile search<br>
Profile search is search by parameters (user should answer 10 questions and get most suitable cities).
* #### Contact experts<br>
Contact experts section is needed to make an appointment with specialists
* #### Visa advisory
Visa advisory section is needed to know whether user need visa to move from one country to another or not.
* #### Feedback
Feedback section is needed to live feedback about Telegram bot.

## Add your files

```
cd existing_repo
git remote add origin https://gitlab.pg.innopolis.university/d.mikhailov/relovista_official.git
git branch -M main
git push -uf origin main
```

## Technologies used
* Python 3
* Aiogram 3
* Sqlite
* Docker

## Requirements
* aiofiles==23.1.0
* aiogram==3.0.0b7
* aiogram-media-group==0.5.1
* aiohttp==3.8.4
* aioschedule==0.5.2
* aiosignal==1.3.1
* async-timeout==4.0.2
* asyncpg==0.27.0
* attrs==22.2.0
* bs4==0.0.1
* certifi==2022.12.7
* charset-normalizer==3.1.0
* colorama==0.4.6
* frozenlist==1.3.3
* idna==3.4
* magic-filter==1.0.9
* multidict==6.0.4
* pydantic==1.10.7
* regex==2023.3.23
* requests==2.28.2
* tiktoken==0.3.3
* tqdm==4.65.0
* typing_extensions==4.5.0
* urllib3==1.26.15
* yarl==1.8.2
* pytest==7.4.0
* pytest-asyncio==0.21.0


## Integrate with your tools

- [ ] [Set up project integrations](https://gitlab.pg.innopolis.university/d.mikhailov/relovista_official/-/settings/integrations)


## Test and Deploy

Use the built-in continuous integration in GitLab.

- [ ] [Get started with GitLab CI/CD](https://docs.gitlab.com/ee/ci/quick_start/index.html)
- [ ] [Analyze your code for known vulnerabilities with Static Application Security Testing(SAST)](https://docs.gitlab.com/ee/user/application_security/sast/)
- [ ] [Deploy to Kubernetes, Amazon EC2, or Amazon ECS using Auto Deploy](https://docs.gitlab.com/ee/topics/autodevops/requirements.html)
- [ ] [Use pull-based deployments for improved Kubernetes management](https://docs.gitlab.com/ee/user/clusters/agent/)
- [ ] [Set up protected environments](https://docs.gitlab.com/ee/ci/environments/protected_environments.html)

***

## Badges
On some READMEs, you may see small images that convey metadata, such as whether or not all the tests are passing for the project. You can use Shields to add some to your README. Many services also have instructions for adding a badge.

## Visuals
Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.

## Installation
Within a particular ecosystem, there may be a common way of installing things, such as using Yarn, NuGet, or Homebrew. However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection.

## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
MIT License is used for this project.

## Project team
Denis Mikhailov (d.mikhailov@innopolis.university) - project manager, developer<br>
Ilya Zubkov (i.zubkov@innopolis.university) - main developer<br>
Fariz Rakhmatov (f.rakhmatov@innopolis.university) - developer<br>
Radmir Tukeev (r.tukeev@innopolis.university) - developer


[relovista-logo]: README_IMG/logo.jpg
[badge-pipeline]: https://gitlab.pg.innopolis.university/i.zubkov/RelovistaBot/badges/main/pipeline.svg
[badge-coverage]: 
[demo-link]: https://www.youtube.com/watch?v=N_mcxFjSv-A
[telegram-bot-link]: https://t.me/RelovistaBot
[telegram-test-bot-link]: https://t.me/RelovistaTestBot


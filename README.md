![Relovista][relovista-logo]
# Relovista
## Telegram bot

![Pipeline badge][badge-pipeline]
![Coverage badge][badge-coverage]
![Release badge][badge-release]

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
Choose first option to run Telegram bot from everywhere<br>
Choose second option to test Telegram bot (tokens are in file config.py, you need to replace token in main.py<br>
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

### Section only for administrator<br>
Admin panel - it can:
* Add city
* Edit information about city
* Add expert
* Edit information about expert

## Project installation
1. Install Python 3
2. Clone the repo (use default cloning)
3. Install all requirements from the file requirements.txt
4. Choose the token in main.py (BOT_TOKEN - token of deployed version, BOT_TEST_TOKEN - token of version for testing)
5. Run main.py

To run using docker:
```
docker compose up -d
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

## License
MIT License is used for this project.

## Project team
Denis Mikhailov (d.mikhailov@innopolis.university) - project manager, developer<br>
Ilya Zubkov (i.zubkov@innopolis.university) - main developer<br>
Fariz Rakhmatov (f.rakhmatov@innopolis.university) - developer<br>
Radmir Tukeev (r.tukeev@innopolis.university) - developer


[relovista-logo]: README_IMG/logo.jpg
[badge-pipeline]: https://gitlab.pg.innopolis.university/i.zubkov/RelovistaBot/badges/main/pipeline.svg
[badge-coverage]: https://gitlab.pg.innopolis.university/i.zubkov/RelovistaBot/badges/main/coverage.svg
[badge-release]: https://gitlab.pg.innopolis.university/i.zubkov/RelovistaBot/-/badges/release.svg
[demo-link]: https://www.youtube.com/watch?v=N_mcxFjSv-A
[telegram-bot-link]: https://t.me/RelovistaBot
[telegram-test-bot-link]: https://t.me/RelovistaTestBot


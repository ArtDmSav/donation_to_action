# Donation to Action Bot

## Описание проекта / Project Description

Donation to Action Bot - это автоматизированный бот, предназначенный для работы с платформой донатов. С помощью этого бота вы можете настроить автоматические действия в ответ на полученные донаты, такие как управление умными устройствами в вашем доме через сервис IFTTT.com.

The Donation to Action Bot is an automated bot designed to work with a donation platform. Using this bot, you can set up automated actions in response to received donations, such as controlling smart devices in your home through the IFTTT.com service.


## Как это работает? / How does it work?

При получении уведомления о донате, бот выполняет следующие действия:

1. **Отправка уведомления о донате**: Бот отправляет информационное сообщение пользователю (вам) о деталях доната, включая имя, сумму и валюту.
2. **Интеграция с IFTTT**: Бот отправляет специализированное сообщение в бота сервиса IFTTT.com от вашего имени.

Upon receiving a donation notification, the bot performs the following actions:

1. **Sending a donation notification**: The bot sends an informational message to the user (you) about the details of the donation, including the name, amount, and currency.
2. **Integration with IFTTT**: The bot sends a specialized message to the IFTTT.com service bot on your behalf.


## Что делает IFTTT? / What does IFTTT do?

Сервис IFTTT.com, получая определенные сообщения от вашего бота, выполняет настроенные сценарии автоматизации. Например, это может быть включение света, пылесоса или кондиционера. Конфигурация сервиса производится заранее и должна быть связана с вашими умными устройствами через телеграм.

The IFTTT.com service, upon receiving specific messages from your bot, performs configured automation scenarios. For example, this could be turning on lights, a vacuum cleaner, or an air conditioner. The configuration of the service is done in advance and must be linked to your smart devices through Telegram.


## Настройка и использование / Setup and Usage

Для начала работы с ботом необходимо:

1. Установить необходимые зависимости, выполнив команду:
pip install -r requirements.txt
2. Настроить переменные окружения или конфигурационные файлы с вашими API ключами, токенами и идентификаторами пользователя.
3. Запустить бота:
python main.py

To get started with the bot, you need to:

1. Install the necessary dependencies by running the command:
pip install -r requirements.txt
2. Configure environment variables or configuration files with your API keys, tokens, and user identifiers.
3. Launch the bot:
python main.py


## Важно / Important

Перед запуском убедитесь, что все настройки сервисов и доступы к API корректно настроены и активированы. Также проверьте, что умные устройства правильно связаны с вашим аккаунтом IFTTT.

Before starting, make sure that all service settings and API accesses are correctly configured and activated. Also, check that smart devices are properly linked to your IFTTT account.


## Лицензия / License

Проект распространяется под лицензией MIT.

The project is distributed under the MIT license.

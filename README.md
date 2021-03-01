<p align="center">
  <img src="https://miro.medium.com/max/400/1*L-rBBZXiYJQyNR3kr8xFTw.png">
  <img src="https://upload.wikimedia.org/wikipedia/commons/9/96/Logo-unet_sin_texto_azul.png">
</p>

# UNET Telegram bot 

This telegram bot searches UNET's students data, using diferents commands and a messages handlers, and consume a Rest API that stores all data in MongoDB cloud.

## To run this bot on your local machine

1- Clone this project, on your local machine:
```bash
$ git clone https://github.com/jefferson10147/unet-bot
```
2- Create a virtual env inside the folder:
```bash
$ python3.x -m venv your_venv
```
3- Activate env:
```bash
$ source your_env/bin/activate
```
4- Install dependencies:
```bash
$ pip install -r requirements.txt
```
5- Create and export variables to .env file:
```bash
$ touch .env
$ echo "bot_token" > your_bot_token
```
You generate bot token by creating a new bot with [@botfather](https://t.me/botfather)

7- Run your bot:
```bash
 $ python3.x bot.py
```

## How to use bot

1. Search student information just by sending into the chat student's names or lastnames, if there are more that one student with that condition, the bot will send the best results, just like a search engine.

2. If Sending student's dni to bot chat, it will search the information.

3. You can use bot commands, that are define:
    * /name < student_name >
    * /second_name < student_second_name >
    * /lastname < student_lastname >
    * /second_lastname < student_second_lastname >
    * /lastname < student_lastname >
    * /name_lastname < student_name > < student_lastname >
    * /dni < student_dni >

## API online

The bot cosumes a API currently running at Heroku cloud. Visit [Home page](https://unet-api.herokuapp.com). See online documentation at [DOC](https://documenter.getpostman.com/view/8771822/TWDUoxJ2#ac0a8fec-3882-40c9-b923-39e8509137fc)

## Bot example

You can try this bot at [@unetpicbot](https://telegram.me/unetpicbot)
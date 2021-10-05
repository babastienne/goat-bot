# Daily Goat Bot

This project is a small bot that send a daily email containing a goat picture to light up your day. 

See the instructions below to install and use this project.

## License

This project uses some pictures taken form the database "Mendelay Data" : https://data.mendeley.com/datasets/4skwhnrscr/1

This dataset is under the CC BY 4.0 License and you should read the terms of this license before use it.

Otherwise, the project itself is under the MIT License. You can reproduce, modify and do pretty much whatever you want with the code.

## Instructions

To be able to use this project, you'll need to configure some elements into a `.env` file. To do so rename the file `.env.dist` to `.env` and complete the required informations.

You should add the informations about your email recipients in the file "mailing_list.py".

You'll need to provide pictures to the program. To do so you should put your images in the `data` folder. Then, the program will select randomly a picture from this folder every day until the apocalypse. If you're looking for goat pictures, you can use the pictures from the Mendeley Data program mentionned above.

When your program is correctly configured, you'll just have to create a cron on your server in order for the program to run daily.

## Warnings

Be sure that you have the consent from the recepients of the emails before using the program.

## Internationalization

The mailer system supports multiple languages. By default it send an email containing the values of MAIL_SUBJECT and MAIL_CONTENT. But you can define multiple languages by adding values into the array LANGUAGES. For each language of the array, you should define the following variables in your `.env` file :
- MAIL_SUBJECT_{language_code}
- MAIL_CONTENT_{language_code}

you should also adapt you recipients list by creating multiple lists in the `mailing_list.py` file.

### Example

For example, if you want you bot to send a daily picture with content in English and French you need to have the following .env file :

```
LANGUAGES = ['en', 'fr']
MAIL_SUBJECT_EN = "Title of my mail"
MAIL_CONTENT_EN = "Content of my mail"
MAIL_SUBJECT_FR = "Titre de mon mail"
MAIL_CONTENT_FR = "Contenu de mon mail"
MAIL_SENDER_EMAIL = "example@example.org"
MAIL_SENDER_PASSWORD = "PassWord1234*!"
PATH_TO_DATA_FOLDER = "data/"
PATH_TO_OLD_DATA_FOLDER = "old/"
```

In your `mailing_list.py` file you'll define two arrays of recipients :

```
RECIPIENTS_EN = [
    # Multiple emails
]

RECIPIENTS_FR = [
    # Multiple emails
]
```

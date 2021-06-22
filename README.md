# Daily Goat Bot

This project is a small bot that send a daily email containing a goat picture to light up your day. 

See the instructions below to install and use this project.

### License

This project uses some pictures taken form the database "Mendelay Data" : https://data.mendeley.com/datasets/4skwhnrscr/1

This dataset is under the CC BY 4.0 License and you should read the terms of this license before use it.

Otherwise, the project itself is under the MIT License. You can reproduce, modify and do pretty much whatever you want with the code.

### Instructions

To be able to use this project, you'll need to configure some elements into a `.env` file. To do so rename the file `.env.dist` to `.env` and complete the required informations.

You'll need to provide pictures to the program. To do so you should put your images in the `data` folder. Then, the program will select randomly a picture from this folder every day until the apocalypse.

When your program is correctly configured, you'll just have to create a cron on your server in order for the program to run daily.

### Warnings

Be sure that you have the consent from the recepients of the emails before using the program.

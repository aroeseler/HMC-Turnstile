Feel free to add any comments about file descriptions, implementations, etc here

##### Note for running the code #####
GitHub does not upload the packages when pushing
You must run the following lines before using yarn start to run the webpage

First, set your directory to turnstile-webpage

yarn global add create-react-app
yarn global add firebase --dev
yarn global add firebase-tools
yarn global add moment
yarn global add moment-timezone
yarn global add chart.js

##########

##### Note for Deploy Firebase Hosting #####
Run the following lines in the turnstile-webpage directory

firebase login
yarn build
firebase init
	Choose Hosting: Configure and deploy Firebase Hosting Sites
	What do ou want to use as your public directory? build
	Configure as a single-page app? Yes
	File build/index.html already exists. Overwrite? No
firebase use --add
	name it whatever you want
firebase deploy
##########

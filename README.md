# Refridgerator App

An app that gives you peace of mind by helping track all the ingredients in your fridge. 

## Functionality (to build):
### Record
Allows user to record what they have in the refridgerator

### Reminder System
Reminds the user the ingredients are reaching date of expiry

### Recipe Recommendation
Recommends recipes on what to make with the ingredients recorded

### Groceries Delivery
Extending from recipe recommendation, if the user is lacking certain ingredients to make a recipe, link to a groceries delivery service for the missing ingredients.. 

## Tech Stack (TBD):
Front-end: react-native

Back-end: Python, Flask, MySQL/PostgreSQL (not sure if needed, possibly can do with just using spoonacular API from react-native)

External: Spoonacular API

## Get Started
Download the repo, extract the files from the zip folder, and save to the desired directory.

Make sure you have node.js, npm, and react-native installed. For node.js and npm, I recommend installing them using a Node Version Manager (nvm). For more, see here - https://docs.npmjs.com/downloading-and-installing-node-js-and-npm

After installing nvm, proceed to install node.js and npm with the following terminal commands
```
nvm list available
nvm install latest
nvm ls
nvm use {latest version e.g. 19.8.1}
```

After installing node.js and npm, you can confirm whether the installation was successful
```
node -v
npm -v
```

Install Expo - beginner friendly
```
npm i -g expo-cli
```
Install the Expo app on your phone. This allows you to see in real time how the code changes affect the app. (see here-https://reactnative.dev/docs/environment-setup)

Start server and follow instructions on the terminal
```
cd RefrigeratorApp
npx expo start
```

## Contribute
To make changes to the code base:
1. Create a new branch (you can do this through github or using the terminal)
```
//navigate to the RefrigeratorApp directory as this is where git is initialized
git checkout -b name-of-branch
```

2. Make your changes
3. Commit and push
```
git add .
git commit -m "commit message"
git push
```
4. Create a pull request
5. Wait for approval

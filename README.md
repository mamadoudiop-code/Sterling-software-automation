# Sterling

## Name
IBM Supply Chain Automation Script

## Overview
This script is designed for automating tasks on the IBM Supply Chain website using Selenium in Python. It handles login processes, navigation through different pages, and automates the downloading of documents in Excel format.

## Features
1. Clears any existing downloaded files in the specified directory.
2. Sets up Chrome WebDriver with specific download preferences.
3. Automates the login process using credentials.
4. Navigates through the site to reach specific documents.
5. Downloads documents from 'Document Inbox' and 'Document Outbox'.
6. Closes the browser after completion.

## Prerequisites
Python
1. Selenium WebDriver
2. Chrome Browser
3. ChromeDriver

## Usage
1. Ensure all prerequisites are installed.
2. Set the username and password variables with your IBM Supply Chain credentials.
3. Run the script.

## Note
1. The script includes explicit time.sleep() calls for simplicity. For a more robust solution, consider using WebDriverWait.
2. Update the download_path to your preferred directory.
3. The script is configured for Chrome; modifications might be needed for other browsers.

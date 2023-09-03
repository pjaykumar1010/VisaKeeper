# VisaKeeper

## Overview
VisaKeeper is an innovative tool, born out of necessity. In July 2023, as a software engineer needing a visitor visa appointment, I experienced first-hand the difficulty of securing an appointment. The slots were scarce and oftentimes booked almost instantly. Finding a way around this, I leveraged my tech expertise to build an intelligent system that automated the process, enhancing my chance to grab an appointment in real-time. Thus, VisaKeeper was born.

VisaKeeper is an automated appointment availability scraper that alerts you pronto as soon as an appointment slot becomes available.

## Installation And Usage

To use VisaKeeper, follow the steps below:

### Step 1: Clone the Repository
Open the terminal/command prompt on your local machine and clone the repository.

```
https://github.com/pjaykumar1010/VisaKeeper.git
```

### Step 2: Install Chrome Driver
Install the ChromeDriver which is a separate executable that WebDriver uses to control Chrome.

```
https://chromedriver.chromium.org/downloads
```

> **Note:** It is essential to keep the ChromeDriver in an accessible location where it isn't likely to get accidentally deleted.

### Step 3: Update the ChromeDriver Path in Script
Open the main.script file and locate `path = "/Users/USER/Downloads/VisaKeeper/chromedriver"`. 
Replace this path with the actual location of your chrome driver.

### Step 4: Run the Script
Execute the python script to have the bot start monitoring for appointment availability. The system will alert you immediately as soon as an available slot detected.

## Contribute

The project is open-source, and contributions are highly welcomed!

## Support

If you need any assistance or run into any issues, feel free to open an issue, and I'll be glad to assist!

# WhatsApp Auto Contact Saver

## Overview

This Python script automates the process of saving WhatsApp contacts who send you messages. It logs into WhatsApp Web, monitors incoming messages, extracts the phone number and name, and saves these contacts to a CSV file. This script is ideal for businesses or individuals looking to manage and save contacts efficiently.

## Features

- **Automatic Login**: Logs into WhatsApp Web using Selenium WebDriver.
- **Continuous Monitoring**: Continuously checks for new messages in the chat list.
- **Contact Extraction**: Extracts contact names and phone numbers from new messages.
- **CSV Storage**: Saves contacts in a CSV file to keep them organized.
- **Duplicate Prevention**: Checks if a contact is already saved to avoid duplicates.

## Requirements

- Python 3.x
- Google Chrome Browser
- ChromeDriver (compatible with your Chrome version)
- Required Python Libraries:
  - `selenium`
  - `csv`

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/uwemdev/whatsapp-auto-contact-saver.git
    cd whatsapp-auto-contact-saver
    ```

2. **Install the required libraries**:
    ```bash
    pip install selenium
    ```

3. **Download ChromeDriver**:
    - Download the version that matches your Chrome browser from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).
    - Place the `chromedriver` executable in your project directory or somewhere in your system's PATH.

## Usage

1. **Run the script**:
    ```bash
    python whatsapp_auto_contact_saver.py
    ```

2. **Scan the QR code**:
    - The script will open WhatsApp Web and wait for you to scan the QR code with your phone. Open WhatsApp on your phone, go to the menu, select WhatsApp Web, and scan the QR code displayed in the browser.

3. **Monitor and Save Contacts**:
    - The script will start monitoring for new messages. When a new message arrives, it will extract the contact's name and phone number and save them to `contacts.csv`.

4. **CSV File**:
    - The contacts will be saved in a CSV file named `contacts.csv` in the same directory as the script.

## Notes

- This script is intended for educational purposes. Use it responsibly and in accordance with WhatsApp’s terms of service.
- Ensure your ChromeDriver version matches your installed version of Chrome to avoid compatibility issues.

## Troubleshooting

- **WebDriverException**: Ensure that ChromeDriver is in your PATH or provide the full path to the executable in the script.
- **ElementNotInteractableException**: This might happen if WhatsApp Web's layout changes. Ensure that the selectors in the script match the current layout.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

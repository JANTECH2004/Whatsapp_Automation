# Whatsapp automation
This project automates sending WhatsApp messages using Selenium WebDriver and an Excel sheet with contact numbers. It allows you to send personalized messages to multiple contacts on WhatsApp Web.

**Features** <br>
<li>Automatically sends messages to contacts listed in an Excel file (.xlsx format).</li>
<li>Uses Selenium to control WhatsApp Web through a browser.</li>
<li>Requires manual QR code scanning for WhatsApp Web login.</li><br>

**Prerequisites**<br>
1.  Python 3.x installed on your system. You can download it from here.<br>

2. Google Chrome Browser or Firefox installed.<br>

3. WebDriver for Chrome (ChromeDriver) or Firefox (geckodriver):<br>

<li>For Chrome: Download ChromeDriver</li>
<li>For Firefox: Download geckodriver</li><br>

4. Required Python Libraries: Install the following libraries using pip: pip install selenium openpyxl<br>


**Setup Instructions**<br>

**Step 1: Clone the Repository**<br>
First, clone the repository to your local machine:<br>git clone https://github.com/JANTECH2004/Whatsapp_Automation.git<br>cd whatsapp-automation<br>

**Step 2: Prepare the contacts.xlsx File**<br>
Create an Excel file (contacts.xlsx) with a list of contacts. The file should have the following structure:<br>

Column A: Contact numbers (including country code, e.g., +91XXXXXXXXXX for India).<br>
Make sure there is no header in the Excel sheet if the loop skips the first row (adjust if necessary).<br>

**Step 3: Download WebDriver**<br>
Download the appropriate WebDriver for your browser and operating system:

<li>Chrome: Download ChromeDriver</li>
<li>Firefox: Download geckodriver</li>
Place the downloaded WebDriver executable in your system's PATH, or specify the full path in the script.<br>

**Step 4: Install Required Python Libraries**<br>
Ensure you have installed the required libraries: pip install selenium openpyxl

**Step 5: Running the Script**<br>
1. Open a terminal or command prompt and navigate to the project directory.

2. Execute the script: python whatsapp_automation.py

3. The script will open WhatsApp Web in your browser. You'll need to scan the QR code manually.

4. Once scanned, the script will start sending messages to the contacts in the Excel file.

**Note:**
Make sure WhatsApp Web is active throughout the process.<br>
Adjust the time.sleep() values if needed based on your network speed.

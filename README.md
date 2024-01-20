# wings-hackathon-5

- Phishing refers to an attempt to steal sensitive information, typically in the form of usernames, passwords, credit card numbers, bank account information.
- Phishing attacks have emerged as a significant and persistent threat
- Aim to trick unsuspecting users into divulging sensitive information, such as login credentials, financial details etc

## Approach

- Datasets containing phishing and legitimate websites is collected from the open-source platform PhishTank.
- Server is designed to extract the required features from the URLs scraped from the web pages and perform classification.
- Chrome extension to scrape and fetch URLs present on the webpage

## Installation

To run the project, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/UsmanAR/wings-hackathon-5.git
   ```

2. Change to the project directory:

   ```bash
   cd wings-hackathon-5
   ```

3. Create a virtual environment:

   ```bash
   python3 -m venv env
   ```

4. Activate the virtual environment:

   ```bash
   source env/bin/activate
   ```

5. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Run the main Python script:
   ```bash
   python main.py
   ```

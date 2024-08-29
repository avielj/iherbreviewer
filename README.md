# iHerb Review Automation Bot

This project automates the process of submitting reviews on the iHerb website using Selenium WebDriver.

## Prerequisites

- Python 3.x
- Google Chrome
- ChromeDriver
- Git

## Setup Instructions

### macOS

1. **Install Python**:
    ```sh
    brew install python
    ```

2. **Install Google Chrome**:
    Download and install from [Google Chrome](https://www.google.com/chrome/).

3. **Install ChromeDriver**:
    ```sh
    brew install chromedriver
    ```

4. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

5. **Install required Python packages**:
    ```sh
    pip install -r requirements.txt
    ```

### Windows

1. **Install Python**:
    Download and install from [Python](https://www.python.org/downloads/).

2. **Install Google Chrome**:
    Download and install from [Google Chrome](https://www.google.com/chrome/).

3. **Install ChromeDriver**:
    Download the ChromeDriver from [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) and add it to your PATH.

4. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

5. **Install required Python packages**:
    ```sh
    pip install -r requirements.txt
    ```

### Linux

1. **Install Python**:
    ```sh
    sudo apt-get install python3
    ```

2. **Install Google Chrome**:
    Download and install from [Google Chrome](https://www.google.com/chrome/).

3. **Install ChromeDriver**:
    ```sh
    sudo apt-get install chromedriver
    ```

4. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

5. **Install required Python packages**:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Script

1. **Start Chrome with remote debugging**:
    ```sh
    google-chrome --remote-debugging-port=9222
    ```

2. **Run the script**:
    ```sh
    python bot.py
    ```

## Uploading to GitHub

1. **Initialize a new Git repository**:
    ```sh
    git init
    ```

2. **Add all files to the repository**:
    ```sh
    git add .
    ```

3. **Commit the changes**:
    ```sh
    git commit -m "Initial commit"
    ```

4. **Add the remote repository**:
    ```sh
    git remote add origin https://github.com/yourusername/your-repo-name.git
    ```

5. **Push the changes to GitHub**:
    ```sh
    git push -u origin master
    ```

## License

This project is licensed under the MIT License.


### Usage Instructions

1. **Start Chrome with Remote Debugging**:
    - Open a terminal or command prompt.
    - Start Google Chrome with remote debugging enabled by running the following command:
      ```sh
      google-chrome --remote-debugging-port=9222
      ```

2. **Run the Script**:
    - Open a terminal or command prompt.
    - Navigate to the directory where the script is located.
    - Run the script using Python:
      ```sh
      python bot.py
      ```

3. **Select the Product to Review**:
    - After starting the script, you have 10 seconds to manually click on the product you want to review on the iHerb website.
    - The script will wait for 10 seconds before proceeding to fill in the review title and other details.

4. **Script Execution**:
    - The script will automatically fill in the review title, required themes, review text, rate the product with 5 stars, and submit the review form.
    - If there are more review titles, the script will continue to process them until all reviews are submitted.

### Note
- Ensure that you have installed all the prerequisites and set up the environment as described in the `README.md` and `prerequisites.sh` files.

# iHerb Reviewer

## Prerequisites

### macOS
1. Install Python:
    ```sh
    brew install python
    ```
2. Install Google Chrome:
    ```sh
    brew install --cask google-chrome
    ```
3. Install ChromeDriver:
    ```sh
    brew install chromedriver
    ```
4. Install required Python packages:
    ```sh
    pip install selenium
    ```

### Linux
1. Install Python:
    ```sh
    sudo apt-get update
    sudo apt-get install -y python3 python3-pip
    ```
2. Install Google Chrome:
    ```sh
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
    sudo dpkg -i google-chrome-stable_current_amd64.deb
    sudo apt-get install -f
    ```
3. Install ChromeDriver:
    ```sh
    sudo apt-get install -y chromedriver
    ```
4. Install required Python packages:
    ```sh
    pip3 install selenium
    ```

### Windows
1. Manually install the following prerequisites:
    - [Python](https://www.python.org/downloads/)
    - [Google Chrome](https://www.google.com/chrome/)
    - [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
2. Install required Python packages:
    ```sh
    pip install selenium
    ```

## Usage Instructions

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

## Upload to GitHub

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
    git remote add origin git@github.com:avielj/iherbreviewer.git
    ```

5. **Push the changes to GitHub**:
    ```sh
    git push -u origin master
    ```

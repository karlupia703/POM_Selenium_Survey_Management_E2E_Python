# Survey Automation Project

## Overview
This project is designed to automate the testing of a survey application. It includes test scripts, page object models, and configuration files to facilitate efficient and reliable testing. The project uses Python and Docker for its setup and execution.

## Project Structure

```
.
├── docker-compose.yml       # Docker Compose configuration
├── Dockerfile               # Docker image setup
├── main.py                  # Main entry point for the application
├── README.md                # Project documentation
├── requirements.txt         # Python dependencies
├── run_tests_with_novnc.sh  # Script to run tests with noVNC
├── config/                  # Configuration files
├── page_funcations/         # Test scripts for various functionalities
├── page_object/             # Page Object Model implementations
├── test_data/               # Test data and translations
├── test-logs/               # Logs and test results
```

## Key Directories

### `config/`
Contains configuration files for the project.

### `page_funcations/`
Houses test scripts for different functionalities of the survey application, such as login, questions, and survey dashboard.

### `page_object/`
Implements the Page Object Model for the survey application, including classes for login, questions, and survey pages.

### `test_data/`
Includes test data and translations used in the test scripts.

### `test-logs/`
Stores logs and test results generated during test execution.

## Prerequisites
- Python 3.9 or later
- Docker
- Docker Compose

## Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd survey
   ```
3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Build the Docker image:
   ```bash
   docker-compose build
   ```

## Running Tests
To execute the tests, use the provided script:
```bash
./run_tests_with_novnc.sh
```

## Logging and Results
Test results are stored in the `test-logs/` directory. You can view the results in the `Test Results - .html` file.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description of your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
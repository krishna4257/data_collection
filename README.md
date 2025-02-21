# Data Collection Project

## Overview

The **Data Collection Project** is designed to automate the process of fetching weather data from a public API [OpenWeatherMap](https://openweathermap.org/) and storing it in a PostgreSQL database hosted on [Neon.tech](https://neon.tech/). This setup ensures that up-to-date weather information is collected and stored daily for analysis and application development purposes.

## Features

- **Automated Data Fetching**: Utilizes GitHub Actions to run a Python script that retrieves weather data every day at 1:00 PM Dallas Time (CST/CDT).
- **Cloud-Based Storage**: Stores the collected data in a PostgreSQL database hosted on Neon.tech, ensuring accessibility and scalability.
- **Extensible Design**: Modular code structure allows for easy integration with other data sources or APIs.

## Getting Started

Follow these instructions to set up the project locally.

### Prerequisites

- **Python 3.8+**: Ensure Python is installed on your system.
- **Virtual Environment**: It's recommended to use a virtual environment to manage dependencies.
- **Neon.tech Account**: Set up a PostgreSQL database on Neon.tech.
- **Weather API Key**: Obtain an API key from a weather data provider (e.g., OpenWeatherMap).

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/krishna4257/data_collection.git
   cd data_collection
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   - Create a `.env` file in the project root:
     ```
     DATABASE_URL=postgresql://<username>:<password>@<host>/<database>?sslmode=require
     WEATHER_API_KEY=<your_weather_api_key>
     ```
   - Replace placeholders with your actual database credentials and API key.

5. **Run the Data Fetching Script**:
   ```bash
   python fetch.py
   ```

## Automation with GitHub Actions

The project includes a GitHub Actions workflow that automates the data fetching process.

### Workflow Details

- **Schedule**: Runs daily at 1:00 PM Dallas Time (CST/CDT).
- **Script Execution**: Executes `fetch.py` to retrieve and store weather data.

### Setting Up Secrets

To enable the workflow:

1. **Navigate to Repository Settings**:
   - Go to the GitHub repository.
   - Click on `Settings` > `Secrets and variables` > `Actions`.

2. **Add the Following Secrets**:
   - `DATABASE_URL`: Your Neon.tech PostgreSQL connection string.
   - `WEATHER_API_KEY`: Your weather API key.

## Contributing

Contributions are welcome! To contribute:

1. **Fork the Repository**.
2. **Create a New Branch**:
   ```bash
   git checkout -b feature/your_feature_name
   ```
3. **Make Your Changes**.
4. **Commit Changes**:
   ```bash
   git commit -m "Add your commit message here"
   ```
5. **Push to the Branch**:
   ```bash
   git push origin feature/your_feature_name
   ```
6. **Open a Pull Request**.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/krishna4257/data_collection/blob/main/LICENSE) file for details.

## Acknowledgments

- **Weather Data Provider**: Special thanks to [OpenWeatherMap](https://openweathermap.org/) for providing the weather data API.
- **Database Hosting**: Thanks to [Neon.tech](https://neon.tech/) for offering reliable PostgreSQL hosting services.

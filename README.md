# exRate Hunter

exRate Hunter is a Python FastAPI application developed as part of the [CoinSnark](https://rmottanet.github.io/coinsnark) project. Its primary responsibility is to provide updated data to other APIs within the CoinSnark project, enabling them to consume data from Redis without the need to update it.

## Responsibility

The application is tasked with consuming data from various external sources, such as the Central Bank of Brazil (BCB), Open Exchange Rates, and Exchange Rates API. These services provide relevant financial data, such as exchange rates.

Upon obtaining the data, the application consolidates it according to the specific business logic of the CoinSnark project. Subsequently, the consolidated data is written to Redis, an in-memory data store, for quick access by other parts of the project.

## Usage

To utilize exRate Hunter, follow these instructions:

1. Clone the repository.
2. Install the dependencies listed in the `requirements.txt` file.
3. Configure the environment variables in the `.env` file by renaming the `.env-example` file.
4. Execute the `main.py` file to start the FastAPI server.
	```bash
	uvicorn app.main:app --host 0.0.0.0 --port 8000
	```

For more information about the CoinSnark project, please refer to the documentation: [CoinSnark GitBook](https://rmottanet.gitbook.io/coinsnark).

Thank you for exploring exRate Hunter. If you have any questions or suggestions regarding the project, I am happy to listen. Please feel free to get in touch.

<br />
<br />
<p align="center">
<a href="https://gitlab.com/rmottanet"><img src="https://img.shields.io/badge/Gitlab--_.svg?style=social&logo=gitlab" alt="GitLab"></a>
<a href="https://github.com/rmottanet"><img src="https://img.shields.io/badge/Github--_.svg?style=social&logo=github" alt="GitHub"></a>
<a href="https://instagram.com/rmottanet/"><img src="https://img.shields.io/badge/Instagram--_.svg?style=social&logo=instagram" alt="Instagram"></a>
<a href="https://www.linkedin.com/in/rmottanet/"><img src="https://img.shields.io/badge/Linkedin--_.svg?style=social&logo=linkedin" alt="Linkedin"></a>
</p>
<br />

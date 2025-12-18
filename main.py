from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
import os


def main():
    print("Hello from langchain-course!")
    print(os.environ.get("OPENAI_API_KEY", "Environment variable not set."))


if __name__ == "__main__":
    main()

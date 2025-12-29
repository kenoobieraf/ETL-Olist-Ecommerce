import subprocess
from pathlib import Path

DATASET = "olistbr/brazilian-ecommerce"
RAW_DATA_DIR = Path("data/raw")

def download_dataset():
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

    print("Downloading dataset from Kaggle...")
    subprocess.run(
        [
            "kaggle",
            "datasets",
            "download",
            "-d",
            DATASET,
            "-p",
            str(RAW_DATA_DIR),
            "--unzip",
        ],
        check=True,
    )
    print("Download complete.")


if __name__ == "__main__":
    download_dataset()
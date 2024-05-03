#!/usr/bin/env python3
import os
import json
"""
Create the build directory and index.json file
"""

def main():
    with open("index.json", "w") as index_handle:
        json.dump(
            {
                "sheets": [entry.name for entry in os.scandir(".") if entry.is_dir() and entry.name not in [".git", ".github"]]
            },
            index_handle
        )


if __name__ == "__main__":
    main()

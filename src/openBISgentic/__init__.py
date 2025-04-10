import argparse
from .server import mcp

def main():
    """OpenBISgentic: Query the openBIS instance and return a list of registered entries."""
    parser = argparse.ArgumentParser(
        description="Gives you the ability to read query the BAM data store and convert them to Markdown."
    )
    parser.parse_args()
    mcp.run()

if __name__ == "__main__":
    main()

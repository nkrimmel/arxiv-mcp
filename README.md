# arxiv-mcp

This project provides a Model Context Protocol (MCP) server for searching, retrieving, and downloading information about research papers from arXiv.org.

## Features
- **Search arXiv Papers:** Query arXiv for papers on a given topic and store their metadata locally.
- **Retrieve Paper Info:** Look up detailed information about a specific paper by its arXiv ID across all saved topics.
- **Download Paper PDFs:** Download the PDF of a paper by its arXiv ID to a specified location.
- **Organized Storage:** Paper metadata is saved in topic-based directories as JSON files for easy access and management.

## Usage
1. **Start the MCP Server:**
   The server is implemented in `research_server.py` and can be started with:
   ```bash
   python research_server.py
   ```
   It uses the `FastMCP` server and communicates via stdio transport.

2. **Available Tools:**
   - `search_papers(topic: str, max_results: int = 5) -> List[str]`  
     Search for papers on a topic and save their info.
   - `extract_info(paper_id: str) -> str`  
     Retrieve metadata for a specific paper by its arXiv ID.
   - `download_pdf(paper_id: str, download_path: str) -> str`  
     Download the PDF of a paper by its arXiv ID to the specified path. Example:
     ```python
     download_pdf("2409.07415v2", "/Users/yourname/Desktop")
     ```

## Example Prompt

"Look for the 10 most relevant arxiv papers with the topic of AI in Healthcare and download the Papers as PDF on my desktop."

## Project Structure
- `research_server.py` — Main MCP server and tool definitions
- `papers/` — Directory where paper metadata is stored, organized by topic
- `pyproject.toml` — Project dependencies and configuration

## Requirements
- Python 3.8+
- [arxiv](https://pypi.org/project/arxiv/) Python package
- [mcp](https://github.com/modelcontext/mcp) Python package
- [requests](https://pypi.org/project/requests/) Python package (for PDF downloads)

Install dependencies with:
```bash
pip install -r requirements.txt
```

## License
MIT License

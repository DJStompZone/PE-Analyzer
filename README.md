# PEAnalyzer

A Python module to analyze Portable Executable (PE) files on Windows systems. It parses and extracts various details about the file header, optional header, sections, imports, and exports. The module provides an easy-to-use class, `PEAnalyzer`, which returns analysis data in JSON format and supports pretty-printing of the information when used with the `print()` function.


|      Info      |                           Package                           |             CI/CD              |          Support            |
| :------------: | :---------------------------------------------------------: | :----------------------------: | :-------------------------: |
| [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pe-analyzer?logo=python&%230044aa&color=%230044aa&labelColor=%23dede00)](https://pypi.org/project/pe-analyzer/) | [![PyPI](https://img.shields.io/pypi/v/pe-analyzer?color=%2360d&label=latest%20%28pypi%29&logo=python&logoColor=%2360d&labelColor=%23101&style=flat)](https://pypi.org/project/pe-analyzer/) | [![Test](https://github.com/DJStompZone/PE-Analyzer/actions/workflows/codeql.yml/badge.svg)](https://github.com/DJStompZone/PE-Analyzer/actions/workflows/codeql.yml) | [![Discord Widget](https://img.shields.io/discord/599808270655291403?color=fff&logo=Discord&label=Discord&logoColor=fff&labelColor=000)](https://discord.io/stomp) |
| [![License](https://img.shields.io/pypi/l/pe-analyzer?color=%230044aa&labelColor=%23dede00&logoColor=%230044aa&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyBmaWxsPSIjMDA0NGFhIiBoZWlnaHQ9IjY0cHgiIHdpZHRoPSI2NHB4IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld0JveD0iMCAwIDIzNy43ODMgMjM3Ljc4MyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIGVuYWJsZS1iYWNrZ3JvdW5kPSJuZXcgMCAwIDIzNy43ODMgMjM3Ljc4MyI%2BCiAgPGc%2BCiAgICA8cGF0aCBkPSJtNDIuNzM1LDUwLjA3MWg5Ni45NTljMy4zMTMsMCA2LDIuNjg3IDYsNnMtMi42ODcsNi02LDZoLTk2Ljk1OWMtMy4zMTMsMC02LTIuNjg3LTYtNnMyLjY4Ni02IDYtNnptMCwyNS45MzRoOTYuOTU5YzMuMzEzLDAgNiwyLjY4NyA2LDZzLTIuNjg3LDYtNiw2aC05Ni45NTljLTMuMzEzLDAtNi0yLjY4Ny02LTZzMi42ODYtNiA2LTZ6bTAsMjUuOTM1aDk2Ljk1OWMzLjMxMywwIDYsMi42ODcgNiw2cy0yLjY4Nyw2LTYsNmgtOTYuOTU5Yy0zLjMxMywwLTYtMi42ODctNi02czIuNjg2LTYgNi02em0wLDI1LjkzNWg5Ni45NTljMy4zMTMsMCA2LDIuNjg3IDYsNnMtMi42ODcsNi02LDZoLTk2Ljk1OWMtMy4zMTMsMC02LTIuNjg3LTYtNnMyLjY4Ni02IDYtNnoiLz4KICAgIDxwYXRoIGQ9Im00Mi43MzUsNjIuMDcxaDk2Ljk1OWMzLjMxMywwIDYtMi42ODcgNi02cy0yLjY4Ny02LTYtNmgtOTYuOTU5Yy0zLjMxMywwLTYsMi42ODctNiw2czIuNjg2LDYgNiw2eiIvPgogICAgPHBhdGggZD0ibTQyLjczNSw4OC4wMDVoOTYuOTU5YzMuMzEzLDAgNi0yLjY4NyA2LTZzLTIuNjg3LTYtNi02aC05Ni45NTljLTMuMzEzLDAtNiwyLjY4Ny02LDZzMi42ODYsNiA2LDZ6Ii8%2BCiAgICA8cGF0aCBkPSJtNDIuNzM1LDExMy45NGg5Ni45NTljMy4zMTMsMCA2LTIuNjg3IDYtNnMtMi42ODctNi02LTZoLTk2Ljk1OWMtMy4zMTMsMC02LDIuNjg3LTYsNnMyLjY4Niw2IDYsNnoiLz4KICAgIDxwYXRoIGQ9Im00Mi43MzUsMTM5Ljg3NWg5Ni45NTljMy4zMTMsMCA2LTIuNjg3IDYtNnMtMi42ODctNi02LTZoLTk2Ljk1OWMtMy4zMTMsMC02LDIuNjg3LTYsNnMyLjY4Niw2IDYsNnoiLz4KICAgIDxwYXRoIGQ9Im0yMzcuNzgzLDk4LjM2MWMwLTEuNTkxLTAuNjMyLTMuMTE3LTEuNzU3LTQuMjQzbC0xNi4zNTYtMTYuMzU1Yy0xLjEyNS0xLjEyNS0yLjY1MS0xLjc1Ny00LjI0My0xLjc1N3MtMy4xMTcsMC42MzItNC4yNDMsMS43NTdsLTI4Ljc1NiwyOC43NTZ2LTg4LjExN2MwLTMuMzEzLTIuNjg2LTYtNi02aC0xNzAuNDI4Yy0zLjMxNCwwLTYsMi42ODctNiw2djIwMC45NzljMCwzLjMxMyAyLjY4Niw2IDYsNmgxNzAuNDI5YzMuMzE0LDAgNi0yLjY4NyA2LTZ2LTYzLjE4bDUzLjU5Ny01My41OTdjMS4xMjUtMS4xMjUgMS43NTctMi42NTEgMS43NTctNC4yNDN6bS0yMjUuNzgzLDExNS4wMnYtMTg4Ljk3OWgxNTguNDI5djk0LjExN2wtMzUuMjkxLDM1LjI5MWgtOTIuNDAzYy0zLjMxMywwLTYsMi42ODctNiw2czIuNjg3LDYgNiw2aDgwLjQwM2wtMS4wMzMsMS4wMzNjLTAuNzc3LDAuNzc3LTEuMzI2LDEuNzUzLTEuNTg2LDIuODIxbC00LjE1NywxNy4wNWgtMjUuMTQ4Yy0zLjMxMywwLTYsMi42ODctNiw2czIuNjg3LDYgNiw2YzAsMCAyOS43MTQsMCAyOS44NiwwIDAuNDczLDAgMC45NS0wLjA1NiAxLjQyMS0wLjE3MWwyMS42MjktNS4yNzNjMS4wNjgtMC4yNiAyLjA0NC0wLjgwOSAyLjgyMS0xLjU4NmwyMy40ODItMjMuNDgydjQ1LjE4MWgtMTU4LjQyN3ptMTI3LjY0OS0zMS4zNzRsLTEwLjQwOCwyLjUzOCAyLjUzOC0xMC40MDggODMuNjQ4LTgzLjY0OCA3Ljg3MSw3Ljg3MS04My42NDksODMuNjQ3eiIvPgogIDwvZz4KPC9zdmc%2BCg%3D%3D)](https://github.com/DJStompZone/PE-Analyzer/blob/main/LICENSE) | [![PyPI - Wheel](https://img.shields.io/pypi/wheel/pe-analyzer?color=%2360d&logo=pypi&logoColor=%2360d&labelColor=%23101&style=flat)](https://pypi.org/project/pe-analyzer/) | [![Pytest](https://github.com/DJStompZone/PE-Analyzer/actions/workflows/pytest.yml/badge.svg)](https://github.com/DJStompZone/PE-Analyzer/actions/workflows/pytest.yml) | [![New Github Issue](https://img.shields.io/badge/GitHub-new%20issue-fff?&logo=github&logoColor=fff&labelColor=000)](https://github.com/DJStompZone/PE-Analyzer/issues/new/choose)


## Installation

To use PEAnalyzer, first, install the `pefile` library by running:

```
pip install pefile
```

Then, download or clone this repository to your project directory.

## Usage

To use the `PEAnalyzer` class, import it from the module and create an instance with the path to the PE file you want to analyze:

```python
from pe_analyzer import PEAnalyzer

file_path = "path/to/your/file.exe"
analyzer = PEAnalyzer(file_path)
```

To print the analysis data in a human-readable format, use the `print()` function:

```python
print(analyzer)
```

To get the analysis data as a JSON object, call the `analyze()` method:

```python
analysis_data = analyzer.analyze()
print(analysis_data)
```

## Support

#### You can create a new issue here: 

[![New Github Issue](https://img.shields.io/badge/GitHub-new%20issue-fff?logo=github&logoColor=fff&labelColor=333&style=for-the-badge)](https://github.com/DJStompZone/PE-Analyzer/issues/new/choose)

#### Or join my Discord server here:

[![Discord Widget](https://img.shields.io/discord/599808270655291403?color=2200cc&logo=discord&label=discord&logoColor=2200cc&labelColor=000&style=for-the-badge)](https://discord.io/stomp)


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

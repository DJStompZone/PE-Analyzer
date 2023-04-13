# PEAnalyzer

A Python module to analyze Portable Executable (PE) files on Windows systems. It parses and extracts various details about the file header, optional header, sections, imports, and exports. The module provides an easy-to-use class, `PEAnalyzer`, which returns analysis data in JSON format and supports pretty-printing of the information when used with the `print()` function.


<table>
  <thead>
    <tr>
      <th>Info</th>
      <th>Package</th>
      <th>CI/CD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <a href="https://pypi.org/project/pe-analyzer/"><img src="https://img.shields.io/pypi/pyversions/pe-analyzer?logo=python" alt="PyPI - Python Version"></a>
      </td>
      <td>
        <a href="https://pypi.org/project/pe-analyzer/"><img src="https://img.shields.io/pypi/v/pe-analyzer?color=%2360d&label=latest%20%28pypi%29&logo=python&logoColor=%2360d" alt="PyPI"></a>
      </td>
      <td>
        <a href="https://github.com/DJStompZone/PE-Analyzer/actions/workflows/codeql.yml"><img src="https://github.com/DJStompZone/PE-Analyzer/actions/workflows/codeql.yml/badge.svg?branch=main" alt="CodeQL"></a>
      </td>
    </tr>
    <tr>
      <td>
        <a href="https://github.com/DJStompZone/PE-Analyzer/blob/main/LICENSE"><img src="https://img.shields.io/pypi/l/pe-analyzer?logo=%svguri%" alt="License"></a>
      </td>
      <td>
        <a href="https://pypi.org/project/pe-analyzer/"><img src="https://img.shields.io/pypi/wheel/pe-analyzer?color=%2360d&logo=pypi&logoColor=%2360d" alt="PyPI - Wheel"></a>
      </td>
      <td>
        <a href="https://github.com/DJStompZone/PE-Analyzer/actions/workflows/test.yml"><img src="https://github.com/DJStompZone/PE-Analyzer/actions/workflows/test.yml/badge.svg" alt="Test"></a>
      </td>
    </tr>
  </tbody>
</table>


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

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

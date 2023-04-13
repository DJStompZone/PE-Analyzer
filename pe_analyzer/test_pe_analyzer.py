import pytest
from pe_analyzer import PEAnalyzer
import json


def test_pe_analyzer():
    file_path = "C:/Windows/System32/cmd.exe"  # Replace with a valid path to a PE file for testing
    analyzer = PEAnalyzer(file_path)
    analysis_data = analyzer.analyze()
    parsed_data = json.loads(analysis_data)

    assert "file_header" in parsed_data
    assert "optional_header" in parsed_data
    assert "sections" in parsed_data
    assert "imports" in parsed_data
    assert "exports" in parsed_data

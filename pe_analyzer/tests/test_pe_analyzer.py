import pytest
from pe_analyzer import PEAnalyzer
import json
import os


def test_pe_analyzer():
    file_path = os.path.join(os.path.dirname(__file__), 'testBin.exe')
    analyzer = PEAnalyzer(file_path)
    analysis_data = analyzer.analyze()
    parsed_data = json.loads(analysis_data)

    assert "file_header" in parsed_data
    assert "optional_header" in parsed_data
    assert "sections" in parsed_data
    assert "imports" in parsed_data
    assert "exports" in parsed_data

# Window Quotation Application - Test Suite

## Overview

This directory contains a comprehensive test suite for the Window Quotation Application with **329 individual tests** covering all aspects of the application from unit tests to end-to-end business scenarios.

## Test Structure

```
tests/
├── unit/                    # Unit tests (Core functionality)
├── ui/                      # User Interface tests  
├── integration/             # Integration tests
├── end_to_end/             # Business scenario tests
├── performance/            # Performance & benchmarking tests
├── advanced/               # Property-based & advanced testing
├── fixtures/               # Test data and mock files
├── reports/                # Generated test reports
└── conftest.py            # Shared fixtures and configuration
```

## Quick Start

### Run All Tests with HTML Report
```bash
pytest --html=tests/reports/complete_test_report.html --self-contained-html -v
```

### Run Only Passing Tests (Clean Report)
```bash
pytest --html=tests/reports/clean_report.html --self-contained-html -v --ignore=tests/ui/ --ignore=tests/advanced/
```

### Run with Coverage Analysis
```bash
pytest --html=tests/reports/coverage_report.html --self-contained-html --cov=. --cov-report=html:tests/reports/coverage_html -v
```

## Test Categories

### 1. Unit Tests (Core Components)
```bash
# Run unit tests only
pytest tests/unit/ --html=tests/reports/unit_tests_report.html --self-contained-html -v

# Test specific components
pytest tests/unit/test_data_manager.py -v
pytest tests/unit/test_global_state.py -v
```

### 2. User Interface Tests
```bash
# Run all UI tests
pytest tests/ui/ --html=tests/reports/ui_tests_report.html --self-contained-html -v

# Test specific UI components
pytest tests/ui/test_main_app.py -v
pytest tests/ui/test_product_frames.py -v
```

### 3. Integration Tests
```bash
# Run integration tests
pytest tests/integration/ --html=tests/reports/integration_report.html --self-contained-html -v
```

### 4. End-to-End Business Scenarios
```bash
# Run all business scenarios
pytest tests/end_to_end/ --html=tests/reports/e2e_report.html --self-contained-html -v

# Test specific scenarios
pytest tests/end_to_end/test_business_scenarios.py -v
pytest tests/end_to_end/test_customer_journey.py -v
```

### 5. Performance & Benchmarking Tests
```bash
# Run performance tests with benchmarks
pytest tests/performance/ --html=tests/reports/performance_report.html --self-contained-html -v --benchmark-only

# Run stress tests
pytest tests/performance/test_stress_testing.py -v

# Run performance benchmarks
pytest tests/performance/test_performance_benchmarks.py -v --benchmark-only
```

### 6. Advanced Testing (Property-Based, Coverage Analysis)
```bash
# Run advanced tests
pytest tests/advanced/ --html=tests/reports/advanced_report.html --self-contained-html -v

# Property-based testing
pytest tests/advanced/test_property_based.py -v

# Test reporting and analysis
pytest tests/advanced/test_reporting.py -v
```

## Test Markers

### Run Tests by Category
```bash
# Unit tests only
pytest -m "unit" --html=tests/reports/unit_marker_report.html --self-contained-html -v

# Performance tests only  
pytest -m "benchmark" --html=tests/reports/benchmark_report.html --self-contained-html -v

# Integration tests only
pytest -m "integration" --html=tests/reports/integration_marker_report.html --self-contained-html -v

# End-to-end tests only
pytest -m "end_to_end" --html=tests/reports/e2e_marker_report.html --self-contained-html -v
```

### Combine Markers
```bash
# Core functionality tests (unit + integration)
pytest -m "unit or integration" --html=tests/reports/core_tests_report.html --self-contained-html -v

# All tests except UI (avoid tkinter issues)
pytest -m "not ui" --html=tests/reports/non_ui_report.html --self-contained-html -v
```

## Report Generation

### Standard HTML Reports
```bash
# Complete test suite with detailed report
pytest --html=tests/reports/complete_detailed_report.html --self-contained-html -v -s

# Fast report (stop on first failure)
pytest --html=tests/reports/fast_report.html --self-contained-html -v -x

# Quiet report (minimal output)
pytest --html=tests/reports/quiet_report.html --self-contained-html -q
```

### Coverage Reports
```bash
# HTML coverage report
pytest --cov=. --cov-report=html:tests/reports/coverage_html --html=tests/reports/test_with_coverage.html --self-contained-html -v

# Terminal coverage report
pytest --cov=. --cov-report=term-missing -v

# Coverage with specific modules
pytest --cov=data_manager --cov=global_state --cov=pdf_generator --cov-report=html:tests/reports/core_coverage -v
```

### Performance Reports
```bash
# Benchmark results in HTML
pytest tests/performance/ --benchmark-only --benchmark-sort=mean --html=tests/reports/benchmark_results.html --self-contained-html -v

# Performance comparison
pytest tests/performance/ --benchmark-compare --benchmark-compare-fail=min:10% -v
```

## Common Use Cases

### Development Workflow
```bash
# Quick smoke test during development
python quick_test.py

# Run tests for changed components
pytest tests/unit/test_data_manager.py tests/unit/test_global_state.py -v

# Full regression test before commit
pytest --html=tests/reports/regression_report.html --self-contained-html -v
```

### Quality Assurance
```bash
# Complete test suite with coverage
pytest --html=tests/reports/qa_complete_report.html --self-contained-html --cov=. --cov-report=html:tests/reports/qa_coverage -v

# Business scenario validation
pytest tests/end_to_end/ --html=tests/reports/business_validation.html --self-contained-html -v

# Performance validation
pytest tests/performance/ --benchmark-only --html=tests/reports/performance_validation.html --self-contained-html -v
```

### Debugging Failed Tests
```bash
# Run with detailed output and stop on first failure
pytest -v -s -x --tb=long

# Run specific failed test with maximum detail
pytest tests/unit/test_data_manager.py::TestCartOperations::test_add_multiple_items_to_cart -v -s --tb=long

# Run last failed tests only
pytest --lf -v
```

## Test Results Summary

Based on the latest test run:

- **Total Tests:** 329
- **Passing Tests:** 228 (69%)
- **Test Categories:** 7 (Unit, UI, Integration, E2E, Performance, Advanced, Legacy)
- **Test Execution Time:** ~14.5 minutes (complete suite)
- **Performance Benchmarks:** 19 benchmark tests included

## Report Locations

All generated reports are saved in `tests/reports/`:

- `complete_test_report.html` - Full test suite results
- `unit_tests_report.html` - Unit tests only
- `performance_report.html` - Performance benchmarks
- `coverage_html/` - HTML coverage reports
- `e2e_report.html` - End-to-end business scenarios

## Prerequisites

### Required Python Packages
```bash
pip install -r requirements-pytest.txt
```

### Key Dependencies
- `pytest` - Core testing framework
- `pytest-html` - HTML report generation
- `pytest-cov` - Coverage analysis
- `pytest-benchmark` - Performance benchmarking
- `pytest-mock` - Mocking utilities
- `hypothesis` - Property-based testing

## Configuration

Test configuration is managed in:
- `pytest.ini` - Main pytest configuration
- `conftest.py` - Shared fixtures and setup
- `requirements-pytest.txt` - Testing dependencies

## Best Practices

1. **Run unit tests frequently** during development
2. **Use markers** to run specific test categories
3. **Generate HTML reports** for documentation and sharing
4. **Include coverage analysis** for quality metrics
5. **Run performance tests** before releases
6. **Use end-to-end tests** for business validation

## Troubleshooting

### Common Issues
- **tkinter errors**: Use `-m "not ui"` to skip UI tests
- **Long execution times**: Use `-x` to stop on first failure
- **Memory issues**: Run test categories separately
- **Performance variance**: Run benchmarks multiple times

### Getting Help
```bash
# View all available markers
pytest --markers

# List all tests without running
pytest --collect-only

# View test configuration
pytest --help
```

---

*This test suite provides comprehensive coverage of the Window Quotation Application, ensuring quality, performance, and reliability across all components.* 
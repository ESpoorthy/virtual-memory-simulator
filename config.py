#!/usr/bin/env python3
"""
Configuration file for Virtual Memory Simulator
Centralized settings for easy customization

Copyright (c) 2026 Sai Spoorthy Eturu
Licensed under the MIT License - see LICENSE file for details.

Part of the Virtual Memory Simulator educational platform.
"""

# Web Server Configuration
WEB_SERVER_CONFIG = {
    'default_port': 8000,
    'host': 'localhost',
    'auto_open_browser': True,
    'server_name': 'Virtual Memory Simulator Web Server'
}

# Simulator Default Settings
SIMULATOR_CONFIG = {
    'default_frames': 3,
    'default_reference_string': [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1],
    'max_frames': 10,
    'min_frames': 1,
    'supported_algorithms': ['FIFO', 'LRU', 'Optimal']
}

# Display Configuration
DISPLAY_CONFIG = {
    'use_unicode_tables': True,
    'table_width': 80,
    'show_step_by_step': True,
    'show_performance_metrics': True,
    'color_output': True,
    'animation_delay': 0.1  # seconds between steps in animated mode
}

# Test Configuration
TEST_CONFIG = {
    'run_performance_tests': True,
    'benchmark_sizes': [100, 500, 1000, 2000],
    'random_test_iterations': 5,
    'generate_test_report': True
}

# Web Interface Styling
WEB_STYLE_CONFIG = {
    'primary_gradient': 'linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%)',
    'accent_color': '#667eea',
    'success_color': '#28a745',
    'error_color': '#dc3545',
    'font_family': "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif",
    'animation_duration': '0.4s',
    'border_radius': '15px'
}

# Educational Content
EDUCATIONAL_CONFIG = {
    'show_algorithm_complexity': True,
    'show_educational_tips': True,
    'include_algorithm_explanations': True,
    'show_performance_analysis': True
}

# Export settings for easy import
__all__ = [
    'WEB_SERVER_CONFIG',
    'SIMULATOR_CONFIG', 
    'DISPLAY_CONFIG',
    'TEST_CONFIG',
    'WEB_STYLE_CONFIG',
    'EDUCATIONAL_CONFIG'
]
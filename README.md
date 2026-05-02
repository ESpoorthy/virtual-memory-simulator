# Virtual Memory Simulator

A comprehensive educational platform for learning Virtual Memory Management concepts through interactive simulations, visualizations, and hands-on experimentation. This simulator implements multiple memory management algorithms and provides extensive tools for understanding core virtual memory principles.

## 🌟 Features Overview

### 🎯 Core Algorithms
- **FIFO** (First In First Out) - O(n×f) time complexity
- **LRU** (Least Recently Used) - O(n×f) time complexity  
- **Optimal** (Belady's Algorithm) - O(n²×f) time complexity

### 🖥️ Multiple Interfaces
- **CLI Version**: Professional Unicode tables with step-by-step visualization
- **Web Interface**: Modern, responsive design with interactive forms and real-time results
- **Interactive Demo**: Guided educational tour with hands-on experiments

### 🧪 Advanced Analysis Tools
- **Comprehensive Test Suite**: Automated testing with edge cases and performance benchmarks
- **Performance Analyzer**: Advanced algorithm comparison and scalability analysis
- **Educational Scenarios**: Curated examples demonstrating key concepts

## 🚀 Quick Start

### Option 1: Web Interface (Recommended)
```bash
python run_web_server.py
# Visit: http://localhost:8000/web_simulator.html
```

### Option 2: Command Line Interface
```bash
python virtual_memory_simulator.py
```

### Option 3: Interactive Demo
```bash
python interactive_demo.py
```

## 📊 Available Tools

| Tool | Purpose | Command |
|------|---------|---------|
| **Main Simulator** | Core CLI interface | `python virtual_memory_simulator.py` |
| **Web Interface** | Modern browser-based GUI | `python run_web_server.py` |
| **Interactive Demo** | Guided educational tour | `python interactive_demo.py` |
| **Test Suite** | Comprehensive testing | `python comprehensive_tests.py` |
| **Performance Analyzer** | Advanced benchmarking | `python performance_analyzer.py` |
| **Basic Tests** | Quick validation | `python test_simulator.py` |

## 🎨 Web Interface Features

### Modern Design
- **Gradient Backgrounds**: Beautiful purple-blue gradients with animated particles
- **Glass Morphism**: Backdrop blur effects for modern depth
- **Smooth Animations**: Hover effects, loading animations, and transitions
- **Responsive Layout**: Works perfectly on desktop, tablet, and mobile

### Interactive Elements
- **Real-time Simulation**: Watch algorithms execute step-by-step
- **Performance Metrics**: Detailed analytics with visual indicators
- **Algorithm Comparison**: Side-by-side performance evaluation
- **Random Pattern Generator**: Create test cases automatically
- **Educational Content**: Interactive algorithm explanations

## 📚 Educational Content

### Algorithm Deep Dive
Each algorithm includes:
- **Complexity Analysis**: Time and space complexity breakdown
- **Implementation Logic**: Step-by-step execution explanation
- **Performance Characteristics**: Strengths and weaknesses
- **Real-world Applications**: Where each algorithm is used

### Learning Scenarios
- **High Locality Patterns**: Demonstrate temporal locality benefits
- **Sequential Access**: Show challenging scenarios for all algorithms
- **Belady's Anomaly**: Counterintuitive FIFO behavior with more frames
- **Working Set Transitions**: Realistic program behavior simulation

## 🔬 Advanced Analysis

### Performance Analyzer Features
- **Pattern Analysis**: Test various access patterns (sequential, random, locality-based)
- **Scalability Benchmarks**: Performance with increasing problem sizes
- **Statistical Analysis**: Mean, standard deviation, best/worst case analysis
- **Detailed Reports**: Comprehensive markdown reports with insights

### Test Suite Coverage
- **Algorithm Accuracy**: Verify correct implementation against known results
- **Edge Cases**: Single frame, single page, empty references
- **Property Verification**: Stack property for LRU, optimality of Optimal
- **Performance Benchmarks**: Execution time analysis

## 📋 Output

### CLI Interface
```
════════════════════════════════════════════════════════════════════════════════
  FIFO ALGORITHM RESULTS
════════════════════════════════════════════════════════════════════════════════
  Time Complexity: O(n×f)  │  Space Complexity: O(f)
  Logic: Replace oldest page (queue-based)
────────────────────────────────────────────────────────────────────────────────
│ Step │ Page │ Memory Frames │ Result │
├──────┼──────┼───────────────┼────────┤
│  1   │  7   ││  7 │  - │  - ││ FAULT  │
│  2   │  0   ││  7 │  0 │  - ││ FAULT  │
│  3   │  1   ││  7 │  0 │  1 ││ FAULT  │
│  4   │  2   ││  2 │  0 │  1 ││ FAULT  │
│  5   │  0   ││  2 │  0 │  1 ││ HIT    │
...

📊 SUMMARY:
   Total Page Faults:  15
   Total References:   20
   Page Fault Ratio:   0.750 (75.0%)
```

### Algorithm Comparison
```
╔══════════════════════════════════════════════════════════════════════════════╗
║                        ALGORITHM COMPARISON                                  ║
╚══════════════════════════════════════════════════════════════════════════════╝
┌─────────────┬──────────────┬─────────────────┬──────────────────────────────┐
│ Algorithm   │ Page Faults  │ Fault Ratio     │ Performance                  │
├─────────────┼──────────────┼─────────────────┼──────────────────────────────┤
│ FIFO        │     15       │     75.0%       │ Simple, not optimal          │
│ LRU         │     12       │     60.0%       │ Good practical choice        │
│ Optimal     │     9        │     45.0%       │ Theoretical minimum ⭐       │
└─────────────┴──────────────┴─────────────────┴──────────────────────────────┘
```

## ⚙️ Configuration

The simulator includes a comprehensive configuration system in `config.py`:

```python
# Simulator Settings
SIMULATOR_CONFIG = {
    'default_frames': 3,
    'default_reference_string': [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1],
    'max_frames': 10,
    'supported_algorithms': ['FIFO', 'LRU', 'Optimal']
}

# Web Interface Styling
WEB_STYLE_CONFIG = {
    'primary_gradient': 'linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%)',
    'animation_duration': '0.4s',
    'border_radius': '15px'
}
```
## 📋 Web Interface

<img width="1792" height="1120" alt="Untitled 3" src="https://github.com/user-attachments/assets/83207187-d553-41d8-b470-d710d7b73a6b" />
<img width="1792" height="1120" alt="Untitled 4" src="https://github.com/user-attachments/assets/2015d7e6-e15b-4e1e-9e48-87c5f0cad82d" />
<img width="1792" height="1120" alt="Untitled 2" src="https://github.com/user-attachments/assets/f8acc901-5fd1-458d-864d-a9f1cbf250b2" />
<img width="1792" height="1120" alt="Untitled 5" src="https://github.com/user-attachments/assets/4ce1e357-ea29-4a20-acec-95b72baa7011" />
<img width="1792" height="1120" alt="Untitled 6" src="https://github.com/user-attachments/assets/35701036-6cbf-4162-9399-cd0315d616e4" />
<img width="1792" height="1120" alt="Untitled 7" src="https://github.com/user-attachments/assets/63016f43-3711-46c3-984b-e0a498623e28" />
<img width="1792" height="1120" alt="Untitled 8" src="https://github.com/user-attachments/assets/50e067ab-0289-4e82-a317-57da6b45209e" />


## 🧪 Testing & Validation

### Run All Tests
```bash
# Comprehensive test suite
python comprehensive_tests.py

# Performance analysis
python performance_analyzer.py

# Basic validation
python test_simulator.py
```

### Test Coverage
- ✅ Algorithm correctness verification
- ✅ Edge case handling (single frame, empty references)
- ✅ Performance benchmarking (100-5000 references)
- ✅ Property verification (LRU stack property, Optimal optimality)
- ✅ Scalability analysis with detailed reporting

## 📄 Requirements

- **Python 3.6+** (for CLI and analysis tools)
- **Modern web browser** (for web interface)
- **No external dependencies** - uses only standard libraries

## 🎓 Educational Objectives

This simulator helps students understand:

### Core Concepts
- Virtual memory fundamentals and page fault handling
- Page replacement algorithm mechanics and trade-offs
- Memory allocation strategies and performance implications

### Algorithm Analysis
- Time and space complexity comparison
- Best-case vs worst-case scenario analysis
- Real-world applicability and implementation considerations

### Performance Optimization
- Impact of locality of reference on algorithm performance
- Memory access pattern analysis and optimization strategies
- System design considerations for memory management

## 🔧 Algorithm Implementation Details

### FIFO (First In First Out)
- **Strategy**: Replace the oldest page in memory (queue-based)
- **Complexity**: O(n×f) time, O(f) space
- **Pros**: Simple implementation, predictable behavior
- **Cons**: Suffers from Belady's anomaly, ignores usage patterns

### LRU (Least Recently Used)
- **Strategy**: Replace the page not used for the longest time
- **Complexity**: O(n×f) time, O(f) space  
- **Pros**: Good practical performance, exploits temporal locality
- **Cons**: More complex implementation, requires usage tracking

### Optimal (Belady's Algorithm)
- **Strategy**: Replace page that will be used farthest in future
- **Complexity**: O(n²×f) time, O(f) space
- **Pros**: Theoretical minimum page faults, optimal performance
- **Cons**: Requires future knowledge, not implementable in practice

## 📈 Performance Insights

Based on comprehensive analysis across various access patterns:

- **Optimal** consistently provides minimum page faults (theoretical baseline)
- **LRU** performs well with temporal locality (realistic workloads)
- **FIFO** is simple but can exhibit counterintuitive behavior
- **Pattern dependency**: Algorithm performance varies significantly with access patterns

## 🤝 Contributing

This educational project welcomes contributions:

### Areas for Enhancement
- Additional page replacement algorithms (Clock, Second Chance)
- More sophisticated visualization options
- Extended performance analysis tools
- Additional educational content and scenarios

### Development Guidelines
- Maintain educational focus and clear documentation
- Ensure cross-platform compatibility
- Follow existing code style and structure
- Include comprehensive tests for new features

## 📄 License

This project is open source and available under the MIT License.

---

**🎓 Perfect for**: Operating Systems courses, Computer Science students, Algorithm analysis, Memory management education, Interactive learning platforms

**🌟 Key Differentiators**: Modern web interface, comprehensive analysis tools, educational focus, interactive demonstrations, extensive testing coverage

---

<div align="center">

**Made with ❤️ for Computer Science Education**

*Empowering students to understand virtual memory concepts through interactive learning*

🎓 **Educational Impact** • 💻 **Modern Technology** • 🚀 **Open Source**

</div>

---

## 👥 Team

<div align="center">

### **Team-10**
**BVRIT Hyderabad College of Engineering for Women**

**Virtual Memory Simulator Project**

</div>

| Roll Number | Name |
|-------------|------|
| **24WH1A6633** | **SAI SPOORTHY ETURU** |
| **24WH1A6642** | **NITHYA KOGANTI** |
| **24WH1A6634** | **ALLA NAVYA SUSHMA SRI** |
| **24WH1A6640** | **THOTA SHIVASRI** |

<div align="center">

**🎓 Academic Institution:** BVRIT Hyderabad College of Engineering for Women  
**📚 Course:** Operating Systems  
**🗓️ Academic Year:** 2025-26  
**👩‍💻 Team:** Collaborative effort by passionate Computer Science students

---

*Dedicated to advancing Computer Science education through innovative learning tools*

</div>

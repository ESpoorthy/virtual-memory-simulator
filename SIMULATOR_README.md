# Virtual Memory Simulator

A comprehensive educational tool for learning Virtual Memory Management concepts through interactive simulations and visualizations. This simulator implements multiple memory management algorithms and provides hands-on experience with core virtual memory principles including page replacement, segmentation, memory allocation, TLB simulation, and fragmentation analysis.

## 🚀 Features

### 1. 💾 Memory Management Systems
- **Virtual Memory & Page Replacement**
  - **FIFO** (First In First Out) - O(n×f) time complexity
  - **LRU** (Least Recently Used) - O(n×f) time complexity  
  - **Optimal** (Belady's Algorithm) - O(n²×f) time complexity
  - Step-by-step visualization with hit/fault analysis

- **Segmentation Simulator**
  - Logical to physical address translation
  - Segment table management
  - Boundary checking and protection

- **Memory Allocation Algorithms**
  - First Fit, Best Fit, Worst Fit comparison
  - Allocation success rate analysis
  - Memory utilization statistics

- **TLB (Translation Lookaside Buffer)**
  - TLB hit/miss simulation with LRU replacement
  - Performance impact analysis

- **Memory Fragmentation Analysis**
  - External fragmentation calculation
  - Memory layout visualization
  - Compaction recommendations

### Enhanced Features
- **Professional table formatting** with Unicode box drawing
- **Step-by-step frame allocation visualization**
- **Clear HIT/FAULT indicators** with performance metrics
- **Algorithm performance comparison** tables
- **Time and space complexity analysis**
- **Educational notes** about algorithm characteristics
- **Interactive menu system** for easy navigation
- **Robust input handling** with validation and error recovery

## 📊 Sample Output

### Virtual Memory Simulation
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
│  6   │  3   ││  2 │  3 │  1 ││ FAULT  │
...

📊 SUMMARY:
   Total Page Faults:  15
   Total References:   20
   Page Fault Ratio:   0.750 (75.0%)
```

### Algorithm Performance Comparison
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

## 🖥️ Available Versions

### 1. CLI Version (Python)
- **File**: `virtual_memory_simulator.py`
- **Features**: Full command-line interface with professional Unicode formatting
- **Usage**: `python virtual_memory_simulator.py`

### 2. Web Version (HTML/JavaScript)
- **Files**: `web_simulator.html`, `simulator.js`
- **Features**: Modern web interface with interactive forms and real-time results
- **Usage**: Open `web_simulator.html` in browser or run `python run_web_server.py`

## 🚀 Quick Start

### CLI Version
```bash
python virtual_memory_simulator.py
```

### Web Version
```bash
# Option 1: Direct browser access
open web_simulator.html

# Option 2: Local web server
python run_web_server.py
# Then visit: http://localhost:8000/web_simulator.html
```

## 📋 Requirements

- **Python 3.6+** (for CLI version)
- **Modern web browser** (for web version)
- **No external dependencies** - uses only standard libraries

## 🎯 Educational Objectives

This simulator helps students understand:

1. **Page Replacement Algorithms**
   - How different algorithms handle memory management
   - Performance trade-offs between algorithms
   - Real-world applicability of each approach

2. **Memory Management Concepts**
   - Virtual memory fundamentals
   - Page fault handling
   - Memory allocation strategies

3. **Algorithm Analysis**
   - Time and space complexity
   - Best-case vs worst-case scenarios
   - Practical implementation considerations

## 🔧 Algorithm Details

### FIFO (First In First Out)
- **Complexity**: O(n×f) time, O(f) space
- **Strategy**: Replace the oldest page in memory
- **Pros**: Simple implementation, predictable behavior
- **Cons**: Suffers from Belady's anomaly, not optimal

### LRU (Least Recently Used)
- **Complexity**: O(n×f) time, O(f) space  
- **Strategy**: Replace the page not used for the longest time
- **Pros**: Good practical performance, approximates optimal
- **Cons**: More complex implementation, requires usage tracking

### Optimal (Belady's Algorithm)
- **Complexity**: O(n²×f) time, O(f) space
- **Strategy**: Replace page that will be used farthest in future
- **Pros**: Theoretical minimum page faults
- **Cons**: Requires future knowledge, not implementable in practice

## 📚 Usage Examples

### Example 1: Basic Simulation
```
Frames: 3
Reference String: 7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1
Algorithm: Compare All
```

### Example 2: Algorithm Comparison
```
Frames: 4
Reference String: 1 2 3 4 1 2 5 1 2 3 4 5
Algorithm: LRU vs FIFO
```

## 🎨 Features Showcase

- ✅ **Professional Unicode Tables** - Clean, aligned output
- ✅ **Color-coded Results** - Visual distinction between HITs and FAULTs  
- ✅ **Performance Metrics** - Detailed statistics and analysis
- ✅ **Algorithm Comparison** - Side-by-side performance evaluation
- ✅ **Educational Content** - Algorithm explanations and complexity analysis
- ✅ **Interactive Menus** - Easy navigation and option selection
- ✅ **Input Validation** - Robust error handling and user guidance
- ✅ **Web Interface** - Modern, responsive design for browser access

## 🤝 Contributing

This is an educational project. Feel free to:
- Add new page replacement algorithms
- Enhance visualization features
- Improve educational content
- Add more memory management concepts

## 📄 License

This project is open source and available under the MIT License.

---

<div align="center">

**Made with ❤️ for Computer Science Education**

*Dedicated to helping students understand virtual memory concepts through hands-on learning*

🎓 **Educational Excellence** • 💻 **Interactive Learning** • 🚀 **Open Source Innovation**

</div>

---

**🎓 Perfect for**: Operating Systems courses, Computer Science students, Algorithm analysis, Memory management education
#!/usr/bin/env python3
"""
Comprehensive Test Suite for Virtual Memory Simulator
Tests all page replacement algorithms with various scenarios and edge cases
"""

import sys
import os
import time
import random
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from virtual_memory_simulator import PageReplacementSimulator

def test_algorithm_accuracy():
    """Test algorithms against known correct results"""
    print("🧪 Algorithm Accuracy Tests")
    print("=" * 50)
    
    test_cases = [
        {
            'name': 'Classic Textbook Example',
            'frames': 3,
            'reference': [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1],
            'expected': {'FIFO': 15, 'LRU': 12, 'Optimal': 9}
        },
        {
            'name': 'Small Test Case',
            'frames': 3,
            'reference': [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5],
            'expected': {'FIFO': 9, 'LRU': 10, 'Optimal': 7}
        },
        {
            'name': 'Belady\'s Anomaly Demo',
            'frames': 4,
            'reference': [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5],
            'expected': {'FIFO': 10, 'LRU': 8, 'Optimal': 6}
        },
        {
            'name': 'High Locality Pattern',
            'frames': 3,
            'reference': [1, 2, 3, 1, 2, 3, 1, 2, 3],
            'expected': {'FIFO': 3, 'LRU': 3, 'Optimal': 3}
        }
    ]
    
    total_tests = 0
    passed_tests = 0
    
    for test_case in test_cases:
        print(f"\n📋 {test_case['name']}")
        print(f"   Frames: {test_case['frames']}, References: {len(test_case['reference'])}")
        
        simulator = PageReplacementSimulator(test_case['frames'], test_case['reference'])
        results = simulator.run_all_algorithms()
        
        for algorithm in ['FIFO', 'LRU', 'Optimal']:
            total_tests += 1
            actual = results[algorithm]['total_faults']
            expected = test_case['expected'][algorithm]
            
            if actual == expected:
                print(f"   ✅ {algorithm}: {actual} faults (correct)")
                passed_tests += 1
            else:
                print(f"   ❌ {algorithm}: {actual} faults (expected {expected})")
    
    print(f"\n🎯 Accuracy Results: {passed_tests}/{total_tests} tests passed")
    return passed_tests == total_tests

def test_edge_cases():
    """Test edge cases and boundary conditions"""
    print("\n🔍 Edge Case Tests")
    print("=" * 50)
    
    edge_cases = [
        {'name': 'Single Frame', 'frames': 1, 'reference': [1, 2, 3, 1, 2]},
        {'name': 'Single Page', 'frames': 3, 'reference': [1, 1, 1, 1, 1]},
        {'name': 'More Frames than Pages', 'frames': 10, 'reference': [1, 2, 3, 4, 5]},
        {'name': 'Sequential Access', 'frames': 2, 'reference': [1, 2, 3, 4, 5, 6, 7, 8]},
        {'name': 'Reverse Sequential', 'frames': 3, 'reference': [8, 7, 6, 5, 4, 3, 2, 1]}
    ]
    
    for case in edge_cases:
        print(f"\n🧪 {case['name']}:")
        try:
            simulator = PageReplacementSimulator(case['frames'], case['reference'])
            results = simulator.run_all_algorithms()
            
            for algorithm in ['FIFO', 'LRU', 'Optimal']:
                faults = results[algorithm]['total_faults']
                print(f"   {algorithm}: {faults} faults")
            print("   ✅ Handled successfully")
        except Exception as e:
            print(f"   ❌ Error: {str(e)}")

def benchmark_performance():
    """Benchmark algorithm performance"""
    print("\n⚡ Performance Benchmark")
    print("=" * 50)
    
    # Generate test data of different sizes
    test_sizes = [100, 500, 1000, 2000]
    frames = 5
    
    for size in test_sizes:
        print(f"\n📊 Testing with {size} references:")
        reference_string = [random.randint(0, 20) for _ in range(size)]
        
        simulator = PageReplacementSimulator(frames, reference_string)
        
        for algorithm in ['FIFO', 'LRU', 'Optimal']:
            start_time = time.time()
            
            if algorithm == 'FIFO':
                result = simulator.simulate_fifo()
            elif algorithm == 'LRU':
                result = simulator.simulate_lru()
            else:  # Optimal
                result = simulator.simulate_optimal()
            
            end_time = time.time()
            execution_time = (end_time - start_time) * 1000
            
            print(f"   {algorithm}: {result['total_faults']} faults, {execution_time:.2f}ms")

def test_algorithm_properties():
    """Test important algorithm properties"""
    print("\n🔬 Algorithm Properties Tests")
    print("=" * 50)
    
    # Test 1: Optimal should never be worse than others
    print("\n🏆 Optimality Test:")
    for _ in range(5):
        frames = random.randint(2, 5)
        reference = [random.randint(0, 10) for _ in range(20)]
        
        simulator = PageReplacementSimulator(frames, reference)
        results = simulator.run_all_algorithms()
        
        optimal_faults = results['Optimal']['total_faults']
        fifo_faults = results['FIFO']['total_faults']
        lru_faults = results['LRU']['total_faults']
        
        if optimal_faults <= fifo_faults and optimal_faults <= lru_faults:
            print(f"   ✅ Optimal ({optimal_faults}) ≤ FIFO ({fifo_faults}), LRU ({lru_faults})")
        else:
            print(f"   ❌ Optimal ({optimal_faults}) > FIFO ({fifo_faults}) or LRU ({lru_faults})")
    
    # Test 2: Stack property for LRU
    print("\n📚 LRU Stack Property Test:")
    reference = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    
    # Test with increasing frame sizes
    prev_faults = float('inf')
    for frames in range(1, 6):
        simulator = PageReplacementSimulator(frames, reference)
        result = simulator.simulate_lru()
        current_faults = result['total_faults']
        
        if current_faults <= prev_faults:
            print(f"   ✅ {frames} frames: {current_faults} faults (non-increasing)")
        else:
            print(f"   ❌ {frames} frames: {current_faults} faults (increased!)")
        
        prev_faults = current_faults

def generate_test_report():
    """Generate a comprehensive test report"""
    print("\n📋 Generating Test Report...")
    
    report = []
    report.append("# Virtual Memory Simulator - Test Report")
    report.append(f"Generated on: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    report.append("")
    
    # Run a comprehensive test
    simulator = PageReplacementSimulator(3, [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1])
    results = simulator.run_all_algorithms()
    
    report.append("## Algorithm Performance Summary")
    for algorithm in ['FIFO', 'LRU', 'Optimal']:
        faults = results[algorithm]['total_faults']
        ratio = (faults / len(simulator.reference_string)) * 100
        report.append(f"- **{algorithm}**: {faults} page faults ({ratio:.1f}% fault rate)")
    
    report.append("")
    report.append("## Test Coverage")
    report.append("- ✅ Algorithm accuracy tests")
    report.append("- ✅ Edge case handling")
    report.append("- ✅ Performance benchmarks")
    report.append("- ✅ Algorithm property verification")
    
    # Write report to file
    with open('test_report.md', 'w') as f:
        f.write('\n'.join(report))
    
    print("   📄 Test report saved to 'test_report.md'")

def main():
    """Run the comprehensive test suite"""
    print("🚀 Virtual Memory Simulator - Comprehensive Test Suite")
    print("=" * 60)
    print("Testing FIFO, LRU, and Optimal page replacement algorithms")
    print("=" * 60)
    
    # Run all test categories
    accuracy_passed = test_algorithm_accuracy()
    test_edge_cases()
    benchmark_performance()
    test_algorithm_properties()
    generate_test_report()
    
    print("\n" + "=" * 60)
    if accuracy_passed:
        print("🎉 All critical tests passed! Simulator is working correctly.")
        print("💡 Check 'test_report.md' for detailed results.")
    else:
        print("⚠️  Some accuracy tests failed. Please review the implementation.")
    
    print("🏁 Test suite completed!")

if __name__ == "__main__":
    main()
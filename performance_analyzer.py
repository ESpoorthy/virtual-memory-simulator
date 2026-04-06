#!/usr/bin/env python3
"""
Performance Analyzer for Virtual Memory Simulator
Advanced analysis and visualization of algorithm performance
"""

import time
import random
import statistics
from typing import Dict, List, Tuple
from virtual_memory_simulator import PageReplacementSimulator

class PerformanceAnalyzer:
    """Analyzes and compares performance of page replacement algorithms"""
    
    def __init__(self):
        self.results = {}
        self.test_cases = []
    
    def generate_test_patterns(self) -> List[Dict]:
        """Generate various test patterns for comprehensive analysis"""
        patterns = []
        
        # Pattern 1: Sequential access
        patterns.append({
            'name': 'Sequential Access',
            'description': 'Pages accessed in sequential order',
            'reference': list(range(1, 21)),
            'frames': 5
        })
        
        # Pattern 2: Random access
        patterns.append({
            'name': 'Random Access',
            'description': 'Completely random page access pattern',
            'reference': [random.randint(1, 20) for _ in range(50)],
            'frames': 5
        })
        
        # Pattern 3: Locality of reference
        patterns.append({
            'name': 'High Locality',
            'description': 'Pages with high temporal locality',
            'reference': [1, 2, 3, 1, 2, 3, 1, 2, 3, 4, 5, 4, 5, 4, 5],
            'frames': 3
        })
        
        # Pattern 4: Working set pattern
        patterns.append({
            'name': 'Working Set',
            'description': 'Distinct working sets with transitions',
            'reference': [1, 2, 3, 1, 2, 3] * 3 + [4, 5, 6, 4, 5, 6] * 3,
            'frames': 4
        })
        
        # Pattern 5: Worst case for FIFO (Belady's anomaly)
        patterns.append({
            'name': 'Belady\'s Anomaly',
            'description': 'Pattern that demonstrates Belady\'s anomaly',
            'reference': [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5],
            'frames': 4
        })
        
        return patterns
    
    def analyze_pattern(self, pattern: Dict) -> Dict:
        """Analyze a specific access pattern"""
        simulator = PageReplacementSimulator(pattern['frames'], pattern['reference'])
        
        # Run all algorithms and measure performance
        start_time = time.time()
        results = simulator.run_all_algorithms()
        total_time = time.time() - start_time
        
        analysis = {
            'pattern': pattern,
            'results': results,
            'execution_time': total_time,
            'reference_length': len(pattern['reference']),
            'unique_pages': len(set(pattern['reference']))
        }
        
        # Calculate additional metrics
        for algorithm in ['FIFO', 'LRU', 'Optimal']:
            result = results[algorithm]
            analysis[f'{algorithm}_fault_rate'] = result['total_faults'] / len(pattern['reference'])
            analysis[f'{algorithm}_hit_rate'] = 1 - analysis[f'{algorithm}_fault_rate']
        
        return analysis
    
    def run_comprehensive_analysis(self) -> Dict:
        """Run comprehensive performance analysis"""
        print("🔬 Running Comprehensive Performance Analysis")
        print("=" * 55)
        
        patterns = self.generate_test_patterns()
        analyses = []
        
        for i, pattern in enumerate(patterns, 1):
            print(f"\n📊 Analyzing Pattern {i}: {pattern['name']}")
            print(f"   {pattern['description']}")
            
            analysis = self.analyze_pattern(pattern)
            analyses.append(analysis)
            
            # Print summary
            for algorithm in ['FIFO', 'LRU', 'Optimal']:
                faults = analysis['results'][algorithm]['total_faults']
                fault_rate = analysis[f'{algorithm}_fault_rate'] * 100
                print(f"   {algorithm}: {faults} faults ({fault_rate:.1f}% fault rate)")
        
        return self.generate_summary_report(analyses)
    
    def generate_summary_report(self, analyses: List[Dict]) -> Dict:
        """Generate a comprehensive summary report"""
        print(f"\n📋 Performance Analysis Summary")
        print("=" * 55)
        
        # Calculate aggregate statistics
        algorithm_stats = {}
        for algorithm in ['FIFO', 'LRU', 'Optimal']:
            fault_rates = [analysis[f'{algorithm}_fault_rate'] for analysis in analyses]
            algorithm_stats[algorithm] = {
                'avg_fault_rate': statistics.mean(fault_rates),
                'min_fault_rate': min(fault_rates),
                'max_fault_rate': max(fault_rates),
                'std_fault_rate': statistics.stdev(fault_rates) if len(fault_rates) > 1 else 0
            }
        
        # Print summary statistics
        print(f"\n🎯 Algorithm Performance Summary:")
        for algorithm, stats in algorithm_stats.items():
            print(f"\n   {algorithm}:")
            print(f"     Average Fault Rate: {stats['avg_fault_rate']*100:.1f}%")
            print(f"     Best Case: {stats['min_fault_rate']*100:.1f}%")
            print(f"     Worst Case: {stats['max_fault_rate']*100:.1f}%")
            print(f"     Consistency (σ): {stats['std_fault_rate']*100:.1f}%")
        
        # Find best performing algorithm overall
        best_algorithm = min(algorithm_stats.keys(), 
                           key=lambda x: algorithm_stats[x]['avg_fault_rate'])
        
        print(f"\n🏆 Overall Best Performer: {best_algorithm}")
        print(f"   Average fault rate: {algorithm_stats[best_algorithm]['avg_fault_rate']*100:.1f}%")
        
        # Pattern-specific insights
        print(f"\n💡 Pattern-Specific Insights:")
        for analysis in analyses:
            pattern_name = analysis['pattern']['name']
            best_for_pattern = min(['FIFO', 'LRU', 'Optimal'], 
                                 key=lambda x: analysis['results'][x]['total_faults'])
            worst_for_pattern = max(['FIFO', 'LRU', 'Optimal'], 
                                  key=lambda x: analysis['results'][x]['total_faults'])
            
            print(f"   {pattern_name}: Best={best_for_pattern}, Worst={worst_for_pattern}")
        
        return {
            'analyses': analyses,
            'algorithm_stats': algorithm_stats,
            'best_overall': best_algorithm
        }
    
    def benchmark_scalability(self) -> Dict:
        """Benchmark algorithm scalability with increasing problem sizes"""
        print(f"\n⚡ Scalability Benchmark")
        print("=" * 55)
        
        sizes = [100, 500, 1000, 2000, 5000]
        frames = 5
        benchmark_results = {}
        
        for size in sizes:
            print(f"\n📈 Testing with {size} references...")
            reference_string = [random.randint(1, 50) for _ in range(size)]
            
            size_results = {}
            for algorithm in ['FIFO', 'LRU', 'Optimal']:
                simulator = PageReplacementSimulator(frames, reference_string)
                
                start_time = time.time()
                if algorithm == 'FIFO':
                    result = simulator.simulate_fifo()
                elif algorithm == 'LRU':
                    result = simulator.simulate_lru()
                else:  # Optimal
                    result = simulator.simulate_optimal()
                
                execution_time = time.time() - start_time
                
                size_results[algorithm] = {
                    'execution_time': execution_time,
                    'faults': result['total_faults'],
                    'fault_rate': result['total_faults'] / size
                }
                
                print(f"   {algorithm}: {execution_time*1000:.1f}ms, {result['total_faults']} faults")
            
            benchmark_results[size] = size_results
        
        # Analyze scalability trends
        print(f"\n📊 Scalability Analysis:")
        for algorithm in ['FIFO', 'LRU', 'Optimal']:
            times = [benchmark_results[size][algorithm]['execution_time'] for size in sizes]
            print(f"   {algorithm}: {times[0]*1000:.1f}ms → {times[-1]*1000:.1f}ms "
                  f"({times[-1]/times[0]:.1f}x slower)")
        
        return benchmark_results
    
    def save_detailed_report(self, summary: Dict, benchmark: Dict):
        """Save detailed analysis report to file"""
        report_lines = []
        report_lines.append("# Virtual Memory Simulator - Performance Analysis Report")
        report_lines.append(f"Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        report_lines.append("")
        
        # Executive Summary
        report_lines.append("## Executive Summary")
        best_alg = summary['best_overall']
        avg_rate = summary['algorithm_stats'][best_alg]['avg_fault_rate'] * 100
        report_lines.append(f"- **Best Overall Algorithm**: {best_alg} ({avg_rate:.1f}% avg fault rate)")
        report_lines.append("")
        
        # Detailed Results
        report_lines.append("## Detailed Analysis Results")
        for analysis in summary['analyses']:
            pattern = analysis['pattern']
            report_lines.append(f"### {pattern['name']}")
            report_lines.append(f"**Description**: {pattern['description']}")
            report_lines.append(f"**Configuration**: {pattern['frames']} frames, {len(pattern['reference'])} references")
            report_lines.append("")
            
            for algorithm in ['FIFO', 'LRU', 'Optimal']:
                faults = analysis['results'][algorithm]['total_faults']
                rate = analysis[f'{algorithm}_fault_rate'] * 100
                report_lines.append(f"- **{algorithm}**: {faults} faults ({rate:.1f}% fault rate)")
            report_lines.append("")
        
        # Save to file
        with open('performance_report.md', 'w') as f:
            f.write('\n'.join(report_lines))
        
        print(f"\n📄 Detailed report saved to 'performance_report.md'")

def main():
    """Run the performance analyzer"""
    analyzer = PerformanceAnalyzer()
    
    # Run comprehensive analysis
    summary = analyzer.run_comprehensive_analysis()
    
    # Run scalability benchmark
    benchmark = analyzer.benchmark_scalability()
    
    # Save detailed report
    analyzer.save_detailed_report(summary, benchmark)
    
    print(f"\n🎉 Performance analysis completed!")
    print(f"📊 Check 'performance_report.md' for detailed results")

if __name__ == "__main__":
    main()
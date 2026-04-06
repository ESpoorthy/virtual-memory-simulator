#!/usr/bin/env python3
"""
Interactive Demo for Virtual Memory Simulator
Guided tour of page replacement algorithms with educational content
"""

import time
import random
from virtual_memory_simulator import PageReplacementSimulator

class InteractiveDemo:
    """Interactive demonstration of virtual memory concepts"""
    
    def __init__(self):
        self.current_step = 0
        self.demo_data = {}
    
    def print_header(self, title: str):
        """Print a formatted header"""
        print("\n" + "═" * 70)
        print(f"  {title}")
        print("═" * 70)
    
    def print_section(self, title: str):
        """Print a section header"""
        print(f"\n{'─' * 50}")
        print(f"  {title}")
        print("─" * 50)
    
    def wait_for_user(self, message: str = "Press Enter to continue..."):
        """Wait for user input"""
        input(f"\n💡 {message}")
    
    def animated_print(self, text: str, delay: float = 0.03):
        """Print text with typewriter effect"""
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
    
    def introduction(self):
        """Introduction to virtual memory concepts"""
        self.print_header("🎓 VIRTUAL MEMORY SIMULATOR - INTERACTIVE DEMO")
        
        print("\n🌟 Welcome to the Virtual Memory Simulator!")
        print("\nThis interactive demo will guide you through:")
        print("  • Understanding virtual memory concepts")
        print("  • Learning page replacement algorithms")
        print("  • Comparing algorithm performance")
        print("  • Analyzing real-world scenarios")
        
        self.wait_for_user()
        
        self.print_section("📚 What is Virtual Memory?")
        
        self.animated_print(
            "Virtual memory is a memory management technique that provides an "
            "abstraction of storage resources. It allows programs to use more "
            "memory than physically available by using disk storage as backup."
        )
        
        print("\n🔑 Key Concepts:")
        print("  • Pages: Fixed-size blocks of virtual memory")
        print("  • Frames: Fixed-size blocks of physical memory")
        print("  • Page Fault: When a referenced page is not in memory")
        print("  • Page Replacement: Choosing which page to remove when memory is full")
        
        self.wait_for_user()
    
    def demonstrate_basic_concept(self):
        """Demonstrate basic page replacement concept"""
        self.print_section("🔄 Page Replacement Demonstration")
        
        print("Let's see how page replacement works with a simple example:")
        print("\n📋 Scenario:")
        print("  • Memory frames: 3")
        print("  • Page references: [1, 2, 3, 4, 1, 2]")
        print("  • Algorithm: FIFO (First In, First Out)")
        
        self.wait_for_user("Ready to see step-by-step execution?")
        
        # Manual step-by-step demonstration
        frames = 3
        reference = [1, 2, 3, 4, 1, 2]
        memory = []
        
        print(f"\n{'Step':<6}{'Page':<6}{'Memory':<20}{'Result':<10}")
        print("─" * 42)
        
        for i, page in enumerate(reference, 1):
            if page in memory:
                result = "HIT"
            else:
                result = "FAULT"
                if len(memory) < frames:
                    memory.append(page)
                else:
                    memory.pop(0)  # Remove first (FIFO)
                    memory.append(page)
            
            memory_str = f"[{', '.join(map(str, memory))}]"
            print(f"{i:<6}{page:<6}{memory_str:<20}{result:<10}")
            time.sleep(1)  # Pause for effect
        
        print(f"\n📊 Total page faults: {sum(1 for page in reference if page not in [1, 2, 3][:len([p for p in reference[:reference.index(page)+1] if p not in memory])])}")
        
        self.wait_for_user()
    
    def compare_algorithms(self):
        """Compare different algorithms with the same input"""
        self.print_section("⚔️ Algorithm Comparison")
        
        print("Now let's compare how different algorithms handle the same workload:")
        
        frames = 3
        reference = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
        
        print(f"\n📋 Test Configuration:")
        print(f"  • Frames: {frames}")
        print(f"  • References: {len(reference)} pages")
        print(f"  • Pattern: {' → '.join(map(str, reference[:10]))}...")
        
        self.wait_for_user("Run the comparison?")
        
        simulator = PageReplacementSimulator(frames, reference)
        results = simulator.run_all_algorithms()
        
        print(f"\n🏆 Results Comparison:")
        algorithms = ['FIFO', 'LRU', 'Optimal']
        
        for algorithm in algorithms:
            faults = results[algorithm]['total_faults']
            fault_rate = (faults / len(reference)) * 100
            
            # Add algorithm description
            descriptions = {
                'FIFO': 'Replaces oldest page (simple queue)',
                'LRU': 'Replaces least recently used page',
                'Optimal': 'Replaces page used farthest in future (theoretical)'
            }
            
            print(f"\n  {algorithm}:")
            print(f"    Description: {descriptions[algorithm]}")
            print(f"    Page Faults: {faults}")
            print(f"    Fault Rate: {fault_rate:.1f}%")
        
        # Highlight the winner
        best_algorithm = min(algorithms, key=lambda x: results[x]['total_faults'])
        print(f"\n🎯 Best Performer: {best_algorithm}")
        
        self.wait_for_user()
    
    def interactive_experiment(self):
        """Let user create their own test case"""
        self.print_section("🧪 Your Turn - Interactive Experiment")
        
        print("Now you can create your own test case!")
        
        # Get user input
        try:
            frames = int(input("\n🗂️  Enter number of memory frames (1-10): "))
            if frames < 1 or frames > 10:
                frames = 3
                print(f"   Using default: {frames} frames")
            
            print("\n📄 Enter page reference string:")
            print("   (Enter page numbers separated by spaces, or press Enter for random)")
            user_input = input("   Pages: ").strip()
            
            if user_input:
                reference = [int(x) for x in user_input.split()]
            else:
                # Generate random reference string
                reference = [random.randint(1, 10) for _ in range(15)]
                print(f"   Generated random: {' '.join(map(str, reference))}")
            
        except ValueError:
            print("   Using default values...")
            frames = 3
            reference = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3]
        
        print(f"\n🚀 Running simulation with {frames} frames and {len(reference)} references...")
        
        simulator = PageReplacementSimulator(frames, reference)
        results = simulator.run_all_algorithms()
        
        # Show results
        print(f"\n📊 Your Results:")
        for algorithm in ['FIFO', 'LRU', 'Optimal']:
            faults = results[algorithm]['total_faults']
            print(f"  {algorithm}: {faults} page faults")
        
        # Educational insight
        optimal_faults = results['Optimal']['total_faults']
        fifo_faults = results['FIFO']['total_faults']
        lru_faults = results['LRU']['total_faults']
        
        print(f"\n💡 Educational Insights:")
        if optimal_faults == fifo_faults == lru_faults:
            print("  • All algorithms performed equally - this happens with certain patterns!")
        else:
            print(f"  • Optimal is theoretical best: {optimal_faults} faults")
            if lru_faults < fifo_faults:
                print("  • LRU outperformed FIFO - good locality of reference")
            elif fifo_faults < lru_faults:
                print("  • FIFO outperformed LRU - unusual but possible")
            else:
                print("  • FIFO and LRU tied - interesting pattern!")
        
        self.wait_for_user()
    
    def educational_scenarios(self):
        """Show educational scenarios demonstrating key concepts"""
        self.print_section("📖 Educational Scenarios")
        
        scenarios = [
            {
                'name': 'High Locality of Reference',
                'description': 'Pages are accessed in clusters - good for LRU',
                'frames': 3,
                'reference': [1, 2, 1, 2, 1, 2, 3, 4, 3, 4, 3, 4],
                'insight': 'LRU performs well when programs exhibit temporal locality'
            },
            {
                'name': 'Sequential Access Pattern',
                'description': 'Pages accessed in sequence - challenging for all algorithms',
                'frames': 3,
                'reference': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                'insight': 'Sequential access causes many page faults regardless of algorithm'
            },
            {
                'name': 'Belady\'s Anomaly',
                'description': 'FIFO gets worse with more frames - counterintuitive!',
                'frames': 4,
                'reference': [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5],
                'insight': 'FIFO can perform worse with more memory - this is Belady\'s anomaly'
            }
        ]
        
        for i, scenario in enumerate(scenarios, 1):
            print(f"\n🎯 Scenario {i}: {scenario['name']}")
            print(f"   {scenario['description']}")
            
            self.wait_for_user(f"Run scenario {i}?")
            
            simulator = PageReplacementSimulator(scenario['frames'], scenario['reference'])
            results = simulator.run_all_algorithms()
            
            print(f"\n   Results:")
            for algorithm in ['FIFO', 'LRU', 'Optimal']:
                faults = results[algorithm]['total_faults']
                print(f"     {algorithm}: {faults} faults")
            
            print(f"\n   💡 {scenario['insight']}")
            
            if i < len(scenarios):
                self.wait_for_user()
    
    def conclusion(self):
        """Wrap up the demo with key takeaways"""
        self.print_section("🎓 Demo Conclusion")
        
        print("🎉 Congratulations! You've completed the Virtual Memory Simulator demo!")
        
        print(f"\n📚 Key Takeaways:")
        print("  1. Virtual memory allows programs to use more memory than physically available")
        print("  2. Page replacement algorithms decide which pages to remove when memory is full")
        print("  3. Optimal algorithm provides theoretical minimum but requires future knowledge")
        print("  4. LRU often performs well in practice due to locality of reference")
        print("  5. FIFO is simple but can exhibit Belady's anomaly")
        print("  6. Algorithm performance depends heavily on access patterns")
        
        print(f"\n🚀 Next Steps:")
        print("  • Try the web interface for interactive simulations")
        print("  • Run comprehensive tests with test_simulator.py")
        print("  • Experiment with different reference patterns")
        print("  • Study real-world memory access patterns")
        
        print(f"\n💻 Available Tools:")
        print("  • CLI Simulator: python virtual_memory_simulator.py")
        print("  • Web Interface: python run_web_server.py")
        print("  • Test Suite: python comprehensive_tests.py")
        print("  • Performance Analysis: python performance_analyzer.py")
        
        print(f"\n🌟 Thank you for learning about virtual memory!")

def main():
    """Run the interactive demo"""
    demo = InteractiveDemo()
    
    try:
        demo.introduction()
        demo.demonstrate_basic_concept()
        demo.compare_algorithms()
        demo.interactive_experiment()
        demo.educational_scenarios()
        demo.conclusion()
        
    except KeyboardInterrupt:
        print(f"\n\n👋 Demo interrupted. Thanks for participating!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Please check your input and try again.")

if __name__ == "__main__":
    main()
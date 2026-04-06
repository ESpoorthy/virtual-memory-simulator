#!/usr/bin/env python3
"""
Virtual Memory Simulator
A CLI-based page replacement algorithm simulator implementing FIFO, LRU, and Optimal algorithms.

Copyright (c) 2026 Team-10, BVRIT Hyderabad College of Engineering for Women
Licensed under the MIT License - see LICENSE file for details.

Team Members:
- SAI SPOORTHY ETURU (24WH1A6633) - Team Lead & Core Developer
- NITHYA KOGANTI (24WH1A6642) - Algorithm Implementation
- ALLA NAVYA SUSHMA SRI (24WH1A6634) - Web Interface Design
- THOTA SHIVASRI (24WH1A6640) - Testing & Documentation

Educational tool for learning memory management concepts in Operating Systems.
Uses only Python standard libraries for maximum compatibility.
"""

import sys
from collections import deque
from typing import List, Tuple, Dict, Any


class PageReplacementSimulator:
    """Main simulator class for page replacement algorithms."""
    
    def __init__(self, num_frames: int, reference_string: List[int]):
        """
        Initialize the simulator.
        
        Args:
            num_frames: Number of frames in memory
            reference_string: List of page references
        """
        self.num_frames = num_frames
        self.reference_string = reference_string
        self.results = {}
    
    def fifo_algorithm(self) -> Dict[str, Any]:
        """
        Implement FIFO (First In First Out) page replacement algorithm.
        
        ALGORITHM LOGIC:
        - Maintains pages in insertion order (queue-like behavior)
        - When a page fault occurs and frames are full, removes the oldest page
        - Simple but may cause Belady's anomaly (more frames = more faults)
        
        TIME COMPLEXITY: O(n * f) where n = reference string length, f = number of frames
        - Each page lookup: O(f) for linear search in frames list
        - Page replacement: O(f) for pop(0) operation on list
        
        SPACE COMPLEXITY: O(f) for storing frames
        
        Returns:
            Dictionary containing step-by-step results and statistics
        """
        frames = []  # List maintains insertion order for FIFO
        page_faults = 0
        steps = []
        
        for step, page in enumerate(self.reference_string, 1):
            if page in frames:
                # Page hit - no replacement needed
                result = "HIT"
            else:
                # Page fault - need to load page into memory
                result = "FAULT"
                page_faults += 1
                
                if len(frames) < self.num_frames:
                    # Free frame available - simply add the page
                    frames.append(page)
                else:
                    # All frames occupied - replace oldest page (FIFO policy)
                    # Remove first element (oldest) and add new page at end
                    frames.pop(0)  # O(f) operation - shifts all elements
                    frames.append(page)
            
            steps.append({
                'step': step,
                'page': page,
                'frames': frames.copy(),
                'result': result
            })
        
        return {
            'algorithm': 'FIFO',
            'steps': steps,
            'page_faults': page_faults,
            'total_references': len(self.reference_string),
            'fault_ratio': page_faults / len(self.reference_string)
        }
    
    def lru_algorithm(self) -> Dict[str, Any]:
        """
        Implement LRU (Least Recently Used) page replacement algorithm.
        
        ALGORITHM LOGIC:
        - Tracks when each page was last accessed (recency information)
        - On page fault with full frames, replaces the page with oldest access time
        - Approximates optimal by assuming recently used pages will be used again soon
        - Better locality of reference handling than FIFO
        
        TIME COMPLEXITY: O(n * f) where n = reference string length, f = number of frames
        - Each page lookup: O(f) for linear search in frames list
        - Finding LRU page: O(f) for scanning usage timestamps
        - Page replacement: O(f) for finding and replacing in list
        
        SPACE COMPLEXITY: O(f) for frames + O(f) for usage tracking = O(f)
        
        Returns:
            Dictionary containing step-by-step results and statistics
        """
        frames = []
        page_faults = 0
        steps = []
        recent_usage = {}  # Maps page -> last access time (step number)
        
        for step, page in enumerate(self.reference_string, 1):
            if page in frames:
                # Page hit - update access time for LRU tracking
                result = "HIT"
                recent_usage[page] = step  # Record current access time
            else:
                # Page fault - need to load page and possibly replace another
                result = "FAULT"
                page_faults += 1
                recent_usage[page] = step  # Record access time for new page
                
                if len(frames) < self.num_frames:
                    # Free frame available - simply add the page
                    frames.append(page)
                else:
                    # All frames occupied - find and replace LRU page
                    # Find page with minimum (oldest) access time
                    lru_page = min(frames, key=lambda p: recent_usage.get(p, 0))
                    lru_index = frames.index(lru_page)  # O(f) search
                    frames[lru_index] = page  # Replace LRU page with new page
            
            steps.append({
                'step': step,
                'page': page,
                'frames': frames.copy(),
                'result': result
            })
        
        return {
            'algorithm': 'LRU',
            'steps': steps,
            'page_faults': page_faults,
            'total_references': len(self.reference_string),
            'fault_ratio': page_faults / len(self.reference_string)
        }
    
    def optimal_algorithm(self) -> Dict[str, Any]:
        """
        Implement Optimal (Belady's) page replacement algorithm.
        
        ALGORITHM LOGIC:
        - Looks ahead in reference string to see future page accesses
        - On page fault with full frames, replaces page that will be used farthest in future
        - If a page is never used again, it's the best candidate for replacement
        - Theoretically optimal - minimizes page faults (Belady's theorem)
        - Impractical in real systems (requires future knowledge)
        
        TIME COMPLEXITY: O(n * f * n) = O(n²f) where n = reference string length, f = frames
        - Each page lookup: O(f) for linear search in frames
        - Finding optimal victim: O(f * n) for scanning future references for each frame
        - Overall: O(n²f) - most expensive but optimal in fault count
        
        SPACE COMPLEXITY: O(f) for frames + O(n) for remaining references = O(n + f)
        
        Returns:
            Dictionary containing step-by-step results and statistics
        """
        frames = []
        page_faults = 0
        steps = []
        
        for step, page in enumerate(self.reference_string, 1):
            if page in frames:
                # Page hit - no replacement needed
                result = "HIT"
            else:
                # Page fault - need to load page and possibly replace another
                result = "FAULT"
                page_faults += 1
                
                if len(frames) < self.num_frames:
                    # Free frame available - simply add the page
                    frames.append(page)
                else:
                    # All frames occupied - find optimal page to replace
                    future_uses = {}
                    remaining_refs = self.reference_string[step:]  # Future references
                    
                    # For each page in frames, find when it will be used next
                    for frame_page in frames:
                        try:
                            # Find index of next occurrence in future references
                            future_uses[frame_page] = remaining_refs.index(frame_page)
                        except ValueError:
                            # Page never used again - perfect candidate for replacement
                            future_uses[frame_page] = float('inf')
                    
                    # Replace page that will be used farthest in future (or never)
                    page_to_replace = max(frames, key=lambda p: future_uses[p])
                    replace_index = frames.index(page_to_replace)
                    frames[replace_index] = page
            
            steps.append({
                'step': step,
                'page': page,
                'frames': frames.copy(),
                'result': result
            })
        
        return {
            'algorithm': 'Optimal',
            'steps': steps,
            'page_faults': page_faults,
            'total_references': len(self.reference_string),
            'fault_ratio': page_faults / len(self.reference_string)
        }
    
    def run_all_algorithms(self) -> Dict[str, Dict[str, Any]]:
        """
        Run all three algorithms and store results.
        
        Returns:
            Dictionary containing results for all algorithms
        """
        self.results['FIFO'] = self.fifo_algorithm()
        self.results['LRU'] = self.lru_algorithm()
        self.results['Optimal'] = self.optimal_algorithm()
        
        return self.results


def format_frames(frames: List[int], num_frames: int) -> str:
    """
    Format frames for display with consistent width and proper alignment.
    
    Args:
        frames: Current frames
        num_frames: Total number of frames
        
    Returns:
        Formatted string representation of frames with consistent spacing
    """
    # Pad frames to show empty slots as dashes
    display_frames = frames + ['-'] * (num_frames - len(frames))
    # Format each frame with consistent width (3 characters)
    formatted = [f'{f:>2}' for f in display_frames]
    return '│ ' + ' │ '.join(formatted) + ' │'


def print_algorithm_results(result: Dict[str, Any], num_frames: int):
    """
    Print detailed results for a single algorithm with improved table formatting.
    
    Args:
        result: Algorithm result dictionary
        num_frames: Number of frames for formatting
    """
    algorithm_name = result['algorithm']
    
    # Calculate column widths for proper alignment
    step_width = 6
    page_width = 6
    frames_width = num_frames * 4 + 3  # Account for separators and padding
    result_width = 8
    
    print(f"\n{'═' * 80}")
    print(f"  {algorithm_name} ALGORITHM RESULTS")
    print(f"{'═' * 80}")
    
    # Print complexity information
    if algorithm_name == 'FIFO':
        print(f"  Time Complexity: O(n×f)  │  Space Complexity: O(f)")
        print(f"  Logic: Replace oldest page (queue-based)")
    elif algorithm_name == 'LRU':
        print(f"  Time Complexity: O(n×f)  │  Space Complexity: O(f)")
        print(f"  Logic: Replace least recently used page")
    elif algorithm_name == 'Optimal':
        print(f"  Time Complexity: O(n²×f) │  Space Complexity: O(n+f)")
        print(f"  Logic: Replace page used farthest in future")
    
    print(f"{'─' * 80}")
    
    # Print table header with proper alignment
    header = f"│{'Step':^{step_width}}│{'Page':^{page_width}}│{'Memory Frames':^{frames_width}}│{'Result':^{result_width}}│"
    print(header)
    print(f"├{'─' * step_width}┼{'─' * page_width}┼{'─' * frames_width}┼{'─' * result_width}┤")
    
    # Print each step with consistent formatting
    for step_data in result['steps']:
        frames_str = format_frames(step_data['frames'], num_frames)
        step_str = f"{step_data['step']:^{step_width}}"
        page_str = f"{step_data['page']:^{page_width}}"
        result_str = f"{step_data['result']:^{result_width}}"
        
        print(f"│{step_str}│{page_str}│{frames_str}│{result_str}│")
    
    # Print table footer
    print(f"└{'─' * step_width}┴{'─' * page_width}┴{'─' * frames_width}┴{'─' * result_width}┘")
    
    # Print summary with better formatting
    print(f"\n📊 SUMMARY:")
    print(f"   Total Page Faults: {result['page_faults']:>3}")
    print(f"   Total References:  {result['total_references']:>3}")
    print(f"   Page Fault Ratio:  {result['fault_ratio']:>6.3f} ({result['fault_ratio']*100:.1f}%)")


def print_comparison_table(results: Dict[str, Dict[str, Any]]):
    """
    Print comparison table for all algorithms with enhanced formatting.
    
    Args:
        results: Results from all algorithms
    """
    print(f"\n{'═' * 70}")
    print(f"  ALGORITHM PERFORMANCE COMPARISON")
    print(f"{'═' * 70}")
    
    # Table header
    print(f"┌{'─' * 15}┬{'─' * 15}┬{'─' * 15}┬{'─' * 20}┐")
    print(f"│{'Algorithm':^15}│{'Page Faults':^15}│{'Fault Ratio':^15}│{'Time Complexity':^20}│")
    print(f"├{'─' * 15}┼{'─' * 15}┼{'─' * 15}┼{'─' * 20}┤")
    
    # Algorithm data with complexity info
    complexity_info = {
        'FIFO': 'O(n×f)',
        'LRU': 'O(n×f)', 
        'Optimal': 'O(n²×f)'
    }
    
    for algo_name, result in results.items():
        faults = f"{result['page_faults']}"
        ratio = f"{result['fault_ratio']:.3f}"
        complexity = complexity_info.get(algo_name, 'N/A')
        
        print(f"│{algo_name:^15}│{faults:^15}│{ratio:^15}│{complexity:^20}│")
    
    print(f"└{'─' * 15}┴{'─' * 15}┴{'─' * 15}┴{'─' * 20}┘")
    
    # Find and highlight best algorithm
    best_algo = min(results.items(), key=lambda x: x[1]['page_faults'])
    worst_algo = max(results.items(), key=lambda x: x[1]['page_faults'])
    
    print(f"\n🏆 PERFORMANCE ANALYSIS:")
    print(f"   Best Algorithm:  {best_algo[0]} ({best_algo[1]['page_faults']} faults)")
    print(f"   Worst Algorithm: {worst_algo[0]} ({worst_algo[1]['page_faults']} faults)")
    
    # Calculate improvement
    if best_algo[1]['page_faults'] < worst_algo[1]['page_faults']:
        improvement = ((worst_algo[1]['page_faults'] - best_algo[1]['page_faults']) / 
                      worst_algo[1]['page_faults'] * 100)
        print(f"   Improvement:     {improvement:.1f}% fewer faults with {best_algo[0]}")
    
    print(f"\n💡 NOTES:")
    print(f"   • Optimal algorithm provides theoretical minimum (requires future knowledge)")
    print(f"   • LRU typically performs better than FIFO in practice")
    print(f"   • FIFO may suffer from Belady's anomaly (more frames ≠ fewer faults)")


def get_user_input() -> Tuple[int, List[int]]:
    """
    Get input from user with validation and improved prompts.
    
    Returns:
        Tuple of (number of frames, reference string)
    """
    print(f"\n📝 INPUT REQUIRED:")
    
    while True:
        try:
            # Get number of frames
            print(f"\n   Memory Configuration:")
            num_frames = int(input("   └─ Enter number of frames (positive integer): "))
            if num_frames <= 0:
                print("   ❌ Number of frames must be positive!")
                continue
            
            # Get reference string
            print(f"\n   Page Reference Sequence:")
            ref_input = input("   └─ Enter reference string (space-separated integers): ")
            reference_string = [int(x) for x in ref_input.split()]
            
            if not reference_string:
                print("   ❌ Reference string cannot be empty!")
                continue
            
            # Validate reference string
            if len(reference_string) > 100:
                confirm = input(f"   ⚠️  Large reference string ({len(reference_string)} pages). Continue? (y/n): ")
                if confirm.lower() != 'y':
                    continue
            
            return num_frames, reference_string
            
        except ValueError:
            print("   ❌ Invalid input! Please enter valid integers.")
        except KeyboardInterrupt:
            print(f"\n\n👋 Exiting...")
            sys.exit(0)


def display_menu():
    """Display the main menu options."""
    print(f"\n{'═' * 60}")
    print(f"  📋 ALGORITHM SELECTION MENU")
    print(f"{'═' * 60}")
    print(f"  1️⃣  Run FIFO Algorithm Only")
    print(f"  2️⃣  Run LRU Algorithm Only") 
    print(f"  3️⃣  Run Optimal Algorithm Only")
    print(f"  4️⃣  Run All Algorithms & Compare")
    print(f"  5️⃣  Exit Program")
    print(f"{'─' * 60}")


def get_menu_choice() -> int:
    """
    Get user's menu choice with validation.
    
    Returns:
        Selected menu option (1-5)
    """
    while True:
        try:
            choice = int(input("   └─ Select option (1-5): "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("   ❌ Please enter a number between 1 and 5.")
        except ValueError:
            print("   ❌ Invalid input! Please enter a number.")
        except KeyboardInterrupt:
            print(f"\n\n👋 Exiting...")
            sys.exit(0)


def run_single_algorithm(simulator: PageReplacementSimulator, algorithm: str, num_frames: int):
    """
    Run a single algorithm and display results.
    
    Args:
        simulator: PageReplacementSimulator instance
        algorithm: Algorithm name ('FIFO', 'LRU', or 'Optimal')
        num_frames: Number of frames for formatting
    """
    print(f"\n🔄 Running {algorithm} algorithm...")
    
    if algorithm == 'FIFO':
        result = simulator.fifo_algorithm()
    elif algorithm == 'LRU':
        result = simulator.lru_algorithm()
    elif algorithm == 'Optimal':
        result = simulator.optimal_algorithm()
    else:
        print(f"❌ Unknown algorithm: {algorithm}")
        return
    
    print_algorithm_results(result, num_frames)
    
    # Show single algorithm summary
    print(f"\n🎯 {algorithm} ALGORITHM SUMMARY:")
    print(f"   Page Faults: {result['page_faults']}/{result['total_references']}")
    print(f"   Efficiency:  {(1 - result['fault_ratio']) * 100:.1f}% hit rate")


def run_all_algorithms_and_compare(simulator: PageReplacementSimulator, num_frames: int):
    """
    Run all algorithms and display comparison.
    
    Args:
        simulator: PageReplacementSimulator instance
        num_frames: Number of frames for formatting
    """
    print(f"\n🔄 Running all algorithms...")
    results = simulator.run_all_algorithms()
    
    # Print results for each algorithm
    for algo_name in ['FIFO', 'LRU', 'Optimal']:
        print_algorithm_results(results[algo_name], num_frames)
    
    # Print comparison
    print_comparison_table(results)


def main():
    """Main function to run the virtual memory simulator with menu system."""
    print("╔" + "═" * 68 + "╗")
    print("║" + " " * 15 + "VIRTUAL MEMORY SIMULATOR" + " " * 29 + "║")
    print("║" + " " * 68 + "║")
    print("║  Implements FIFO, LRU, and Optimal page replacement algorithms  ║")
    print("╚" + "═" * 68 + "╝")
    
    try:
        # Get input parameters once
        num_frames, reference_string = get_user_input()
        
        print(f"\n📋 SIMULATION PARAMETERS:")
        print(f"   Number of Memory Frames: {num_frames}")
        print(f"   Reference String Length: {len(reference_string)}")
        print(f"   Page References: {' → '.join(map(str, reference_string))}")
        
        # Create simulator instance
        simulator = PageReplacementSimulator(num_frames, reference_string)
        
        # Main menu loop
        while True:
            display_menu()
            choice = get_menu_choice()
            
            if choice == 1:
                run_single_algorithm(simulator, 'FIFO', num_frames)
            elif choice == 2:
                run_single_algorithm(simulator, 'LRU', num_frames)
            elif choice == 3:
                run_single_algorithm(simulator, 'Optimal', num_frames)
            elif choice == 4:
                run_all_algorithms_and_compare(simulator, num_frames)
            elif choice == 5:
                print(f"\n👋 Thank you for using Virtual Memory Simulator!")
                break
            
            # Ask if user wants to continue
            print(f"\n{'─' * 40}")
            continue_choice = input("   Continue with same parameters? (y/n): ").lower().strip()
            if continue_choice != 'y':
                # Ask if they want to start over or exit
                restart = input("   Start over with new parameters? (y/n): ").lower().strip()
                if restart == 'y':
                    # Get new parameters and create new simulator
                    num_frames, reference_string = get_user_input()
                    print(f"\n📋 NEW SIMULATION PARAMETERS:")
                    print(f"   Number of Memory Frames: {num_frames}")
                    print(f"   Reference String Length: {len(reference_string)}")
                    print(f"   Page References: {' → '.join(map(str, reference_string))}")
                    simulator = PageReplacementSimulator(num_frames, reference_string)
                else:
                    print(f"\n👋 Thank you for using Virtual Memory Simulator!")
                    break
        
        print(f"✅ Session completed successfully!")
        
        # Made with love message
        print(f"\n{'═' * 68}")
        print(f"   Made with ❤️  for Computer Science Education")
        print(f"   Empowering students to master virtual memory concepts")
        print(f"{'═' * 68}")
        
        # Team information
        print(f"\n{'─' * 68}")
        print(f"   👥 Team-10 | BVRIT Hyderabad College of Engineering for Women")
        print(f"{'─' * 68}")
        print(f"   24WH1A6633 - SAI SPOORTHY ETURU (Team Lead)")
        print(f"   24WH1A6642 - NITHYA KOGANTI (Algorithm Implementation)")
        print(f"   24WH1A6634 - ALLA NAVYA SUSHMA SRI (Web Interface)")
        print(f"   24WH1A6640 - THOTA SHIVASRI (Testing & Documentation)")
        print(f"{'─' * 68}")
        
    except KeyboardInterrupt:
        print(f"\n\n❌ Simulation interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
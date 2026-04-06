// Virtual Memory Simulator - JavaScript Implementation
// Web-based interactive simulator for memory management concepts
//
// Copyright (c) 2026 Team-10, BVRIT Hyderabad College of Engineering for Women
// Licensed under the MIT License - see LICENSE file for details.
//
// Team Members:
// - SAI SPOORTHY ETURU (24WH1A6633) - Team Lead & Core Developer
// - NITHYA KOGANTI (24WH1A6642) - Algorithm Implementation
// - ALLA NAVYA SUSHMA SRI (24WH1A6634) - Web Interface Design
// - THOTA SHIVASRI (24WH1A6640) - Testing & Documentation
//
// Educational tool for learning page replacement algorithms

// Tab management
function showTab(tabName) {
    // Hide all tabs
    const tabs = document.querySelectorAll('.tab-content');
    tabs.forEach(tab => tab.classList.remove('active'));
    
    // Remove active class from all nav tabs
    const navTabs = document.querySelectorAll('.nav-tab');
    navTabs.forEach(tab => tab.classList.remove('active'));
    
    // Show selected tab
    document.getElementById(tabName).classList.add('active');
    
    // Add active class to clicked nav tab
    event.target.classList.add('active');
}

// Memory Management Functions
function runMemorySimulation() {
    const frames = parseInt(document.getElementById('frames').value);
    const referenceString = document.getElementById('reference-string').value
        .split(' ').map(x => parseInt(x)).filter(x => !isNaN(x));
    const algorithm = document.getElementById('algorithm').value;
    
    if (frames < 1 || referenceString.length === 0) {
        showAlert('Please enter valid input values', 'error');
        return;
    }
    
    // Show loading animation
    const resultsDiv = document.getElementById('memory-results');
    resultsDiv.innerHTML = `
        <div class="results">
            <div style="text-align: center; padding: 40px;">
                <div class="loading"></div>
                <span style="font-size: 1.1em; color: #667eea;">Processing simulation...</span>
            </div>
        </div>
    `;
    
    // Simulate processing delay for better UX
    setTimeout(() => {
        let results = '';
        
        if (algorithm === 'all') {
            const fifoResult = simulateFIFO(frames, referenceString);
            const lruResult = simulateLRU(frames, referenceString);
            const optimalResult = simulateOptimal(frames, referenceString);
            
            // Add total references for percentage calculation
            [fifoResult, lruResult, optimalResult].forEach(result => {
                result.totalRefs = referenceString.length;
            });
            
            results = `
                <div class="results">
                    <h3>🔄 Page Replacement Algorithm Comparison</h3>
                    ${formatMemoryResult('FIFO', fifoResult, frames)}
                    ${formatMemoryResult('LRU', lruResult, frames)}
                    ${formatMemoryResult('Optimal', optimalResult, frames)}
                    ${formatComparisonTable([
                        { name: 'FIFO', faults: fifoResult.faults, totalRefs: referenceString.length },
                        { name: 'LRU', faults: lruResult.faults, totalRefs: referenceString.length },
                        { name: 'Optimal', faults: optimalResult.faults, totalRefs: referenceString.length }
                    ])}
                </div>
            `;
        } else {
            let result;
            let algorithmName;
            switch (algorithm) {
                case 'fifo':
                    result = simulateFIFO(frames, referenceString);
                    algorithmName = 'FIFO';
                    break;
                case 'lru':
                    result = simulateLRU(frames, referenceString);
                    algorithmName = 'LRU';
                    break;
                case 'optimal':
                    result = simulateOptimal(frames, referenceString);
                    algorithmName = 'Optimal';
                    break;
            }
            results = `<div class="results"><h3>📊 ${algorithmName} Algorithm Results</h3>${formatMemoryResult(algorithmName, result, frames)}</div>`;
        }
        
        resultsDiv.innerHTML = results;
        
        // Scroll to results
        resultsDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }, 800);
}

function showAlert(message, type = 'info') {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type === 'error' ? 'danger' : type}`;
    alertDiv.innerHTML = `
        <strong>${type === 'error' ? '❌' : 'ℹ️'}</strong> ${message}
    `;
    
    const container = document.querySelector('.tab-content.active');
    container.insertBefore(alertDiv, container.firstChild);
    
    // Remove alert after 5 seconds
    setTimeout(() => {
        if (alertDiv.parentNode) {
            alertDiv.remove();
        }
    }, 5000);
}

function simulateFIFO(frames, referenceString) {
    const memory = [];
    const steps = [];
    let faults = 0;
    
    for (let i = 0; i < referenceString.length; i++) {
        const page = referenceString[i];
        let isHit = false;
        
        // Check if page is already in memory
        if (memory.includes(page)) {
            isHit = true;
        } else {
            faults++;
            if (memory.length < frames) {
                memory.push(page);
            } else {
                // Remove first page (FIFO)
                memory.shift();
                memory.push(page);
            }
        }
        
        steps.push({
            step: i + 1,
            page: page,
            memory: [...memory],
            result: isHit ? 'HIT' : 'FAULT'
        });
    }
    
    return { steps, faults };
}

function simulateLRU(frames, referenceString) {
    const memory = [];
    const steps = [];
    let faults = 0;
    
    for (let i = 0; i < referenceString.length; i++) {
        const page = referenceString[i];
        let isHit = false;
        
        // Check if page is already in memory
        const pageIndex = memory.indexOf(page);
        if (pageIndex !== -1) {
            isHit = true;
            // Move page to end (most recently used)
            memory.splice(pageIndex, 1);
            memory.push(page);
        } else {
            faults++;
            if (memory.length < frames) {
                memory.push(page);
            } else {
                // Remove least recently used (first element)
                memory.shift();
                memory.push(page);
            }
        }
        
        steps.push({
            step: i + 1,
            page: page,
            memory: [...memory],
            result: isHit ? 'HIT' : 'FAULT'
        });
    }
    
    return { steps, faults };
}

function simulateOptimal(frames, referenceString) {
    const memory = [];
    const steps = [];
    let faults = 0;
    
    for (let i = 0; i < referenceString.length; i++) {
        const page = referenceString[i];
        let isHit = false;
        
        // Check if page is already in memory
        if (memory.includes(page)) {
            isHit = true;
        } else {
            faults++;
            if (memory.length < frames) {
                memory.push(page);
            } else {
                // Find page that will be used farthest in future
                let farthest = -1;
                let replaceIndex = 0;
                
                for (let j = 0; j < memory.length; j++) {
                    let nextUse = referenceString.length;
                    for (let k = i + 1; k < referenceString.length; k++) {
                        if (referenceString[k] === memory[j]) {
                            nextUse = k;
                            break;
                        }
                    }
                    
                    if (nextUse > farthest) {
                        farthest = nextUse;
                        replaceIndex = j;
                    }
                }
                
                memory[replaceIndex] = page;
            }
        }
        
        steps.push({
            step: i + 1,
            page: page,
            memory: [...memory],
            result: isHit ? 'HIT' : 'FAULT'
        });
    }
    
    return { steps, faults };
}

function formatMemoryResult(algorithmName, result, frames) {
    const stepsTable = result.steps.map(step => {
        const memoryDisplay = Array(frames).fill('-');
        step.memory.forEach((page, index) => {
            memoryDisplay[index] = page;
        });
        
        return `
            <tr class="${step.result === 'HIT' ? 'hit' : 'fault'}">
                <td>${step.step}</td>
                <td><strong>${step.page}</strong></td>
                <td><code>[${memoryDisplay.join(', ')}]</code></td>
                <td><strong>${step.result}</strong></td>
            </tr>
        `;
    }).join('');
    
    const faultRatio = (result.faults / result.steps.length * 100).toFixed(1);
    const hitRatio = (100 - faultRatio).toFixed(1);
    
    return `
        <div style="margin: 25px 0;">
            <h4 style="color: #2c3e50; margin-bottom: 20px; font-size: 1.3em;">
                🔄 ${algorithmName} Algorithm Results
            </h4>
            <table class="table">
                <thead>
                    <tr>
                        <th>Step</th>
                        <th>Page</th>
                        <th>Memory Frames</th>
                        <th>Result</th>
                    </tr>
                </thead>
                <tbody>
                    ${stepsTable}
                </tbody>
            </table>
            <div class="performance-metrics">
                <h5 style="margin-bottom: 15px; color: #2c3e50;">📈 Performance Metrics</h5>
                <div class="metric-item">
                    <span>Total Page Faults:</span>
                    <span class="metric-value danger">${result.faults}</span>
                </div>
                <div class="metric-item">
                    <span>Total References:</span>
                    <span class="metric-value">${result.steps.length}</span>
                </div>
                <div class="metric-item">
                    <span>Page Fault Ratio:</span>
                    <span class="metric-value danger">${faultRatio}%</span>
                </div>
                <div class="metric-item">
                    <span>Hit Ratio:</span>
                    <span class="metric-value success">${hitRatio}%</span>
                </div>
            </div>
        </div>
    `;
}

function formatComparisonTable(algorithms) {
    const best = algorithms.reduce((min, alg) => alg.faults < min.faults ? alg : min);
    const worst = algorithms.reduce((max, alg) => alg.faults > max.faults ? alg : max);
    
    const rows = algorithms.map(alg => {
        let badge = '';
        if (alg.name === best.name && best.faults !== worst.faults) {
            badge = ' <span class="comparison-badge badge-best">🏆 Best</span>';
        } else if (alg.name === worst.name && best.faults !== worst.faults) {
            badge = ' <span class="comparison-badge badge-worst">📉 Worst</span>';
        }
        
        return `
            <tr>
                <td style="text-align: left;"><strong>${alg.name}</strong>${badge}</td>
                <td><strong>${alg.faults}</strong></td>
                <td>${((alg.faults / algorithms[0].totalRefs) * 100).toFixed(1)}%</td>
            </tr>
        `;
    }).join('');
    
    // Add total references to algorithms for percentage calculation
    algorithms.forEach(alg => {
        if (!alg.totalRefs) alg.totalRefs = 20; // Default from example
    });
    
    return `
        <div style="margin-top: 40px;">
            <h4 style="color: #2c3e50; margin-bottom: 20px; font-size: 1.3em;">
                🏆 Algorithm Performance Comparison
            </h4>
            <table class="table">
                <thead>
                    <tr>
                        <th style="text-align: left;">Algorithm</th>
                        <th>Page Faults</th>
                        <th>Fault Rate</th>
                    </tr>
                </thead>
                <tbody>
                    ${rows}
                </tbody>
            </table>
            <div class="alert alert-info">
                <strong>💡 Performance Analysis:</strong><br>
                ${best.faults === worst.faults ? 
                    '🔄 All algorithms performed equally for this reference string - this is rare but can happen with certain patterns.' :
                    `🎯 <strong>${best.name}</strong> achieved the best performance with <strong>${best.faults} page faults</strong>, while <strong>${worst.name}</strong> had <strong>${worst.faults} page faults</strong>. The difference of <strong>${worst.faults - best.faults} faults</strong> represents a <strong>${(((worst.faults - best.faults) / worst.faults) * 100).toFixed(1)}%</strong> improvement.`
                }
            </div>
        </div>
    `;
}

function loadMemoryExample() {
    document.getElementById('frames').value = '3';
    document.getElementById('reference-string').value = '7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1';
    showAlert('📝 Example loaded! This is a classic reference string that demonstrates different algorithm behaviors.', 'success');
}

function loadRandomExample() {
    const frames = Math.floor(Math.random() * 3) + 3; // 3-5 frames
    const pages = [];
    const pageRange = Math.floor(Math.random() * 5) + 5; // 5-9 different pages
    const length = Math.floor(Math.random() * 10) + 15; // 15-24 references
    
    for (let i = 0; i < length; i++) {
        pages.push(Math.floor(Math.random() * pageRange));
    }
    
    document.getElementById('frames').value = frames;
    document.getElementById('reference-string').value = pages.join(' ');
    showAlert(`🎲 Random pattern generated! ${frames} frames, ${length} references, pages 0-${pageRange-1}`, 'info');
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
    loadMemoryExample();
});
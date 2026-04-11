// Virtual Memory Simulator - Enhanced Version

// ---------------- TAB ----------------
function showTab(tabName) {
    const tabs = document.querySelectorAll('.tab-content');
    tabs.forEach(tab => tab.classList.remove('active'));

    const navTabs = document.querySelectorAll('.nav-tab');
    navTabs.forEach(tab => tab.classList.remove('active'));

    document.getElementById(tabName).classList.add('active');
    event.target.classList.add('active');
}

// ---------------- MAIN RUN ----------------
function runMemorySimulation() {
    const frames = parseInt(document.getElementById('frames').value);
    const referenceString = document.getElementById('reference-string').value
        .split(' ').map(x => parseInt(x)).filter(x => !isNaN(x));

    const algorithm = document.getElementById('algorithm').value;

    if (frames < 1 || referenceString.length === 0) {
        showAlert('Please enter valid input values', 'error');
        return;
    }

    const resultsDiv = document.getElementById('memory-results');

    resultsDiv.innerHTML = `
        <div class="results">
            <div style="text-align: center; padding: 40px;">
                <div class="loading"></div>
                Processing simulation...
            </div>
        </div>
    `;

    setTimeout(() => {
        let results = '';

        if (algorithm === 'all') {
            const fifoResult = simulateFIFO(frames, referenceString);
            const lruResult = simulateLRU(frames, referenceString);
            const optimalResult = simulateOptimal(frames, referenceString);

            const belady = detectBeladyAnomaly(referenceString, frames);

            [fifoResult, lruResult, optimalResult].forEach(r => {
                r.totalRefs = referenceString.length;
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

                    ${formatBeladyResult(belady)}
                </div>
            `;
        }

        resultsDiv.innerHTML = results;
        resultsDiv.scrollIntoView({ behavior: 'smooth' });

    }, 800);
}

// ---------------- ALERT ----------------
function showAlert(message, type = 'info') {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type === 'error' ? 'danger' : type}`;
    alertDiv.innerHTML = message;

    const container = document.querySelector('.tab-content.active');
    container.insertBefore(alertDiv, container.firstChild);

    setTimeout(() => alertDiv.remove(), 4000);
}

// ---------------- FIFO ----------------
function simulateFIFO(frames, ref) {
    let memory = [], faults = 0, steps = [];

    ref.forEach((page, i) => {
        let hit = memory.includes(page);

        if (!hit) {
            faults++;
            if (memory.length < frames) memory.push(page);
            else {
                memory.shift();
                memory.push(page);
            }
        }

        steps.push({ step: i+1, page, memory: [...memory], result: hit?'HIT':'FAULT' });
    });

    return { steps, faults };
}

// ---------------- LRU ----------------
function simulateLRU(frames, ref) {
    let memory = [], faults = 0, steps = [];

    ref.forEach((page, i) => {
        let index = memory.indexOf(page);
        let hit = index !== -1;

        if (hit) {
            memory.splice(index,1);
            memory.push(page);
        } else {
            faults++;
            if (memory.length < frames) memory.push(page);
            else {
                memory.shift();
                memory.push(page);
            }
        }

        steps.push({ step: i+1, page, memory:[...memory], result: hit?'HIT':'FAULT' });
    });

    return { steps, faults };
}

// ---------------- OPTIMAL ----------------
function simulateOptimal(frames, ref) {
    let memory = [], faults = 0, steps = [];

    for (let i=0;i<ref.length;i++) {
        let page = ref[i];
        let hit = memory.includes(page);

        if (!hit) {
            faults++;

            if (memory.length < frames) memory.push(page);
            else {
                let farthest = -1, index = 0;

                for (let j=0;j<memory.length;j++) {
                    let next = ref.slice(i+1).indexOf(memory[j]);
                    if (next === -1) {
                        index = j;
                        break;
                    }
                    if (next > farthest) {
                        farthest = next;
                        index = j;
                    }
                }

                memory[index] = page;
            }
        }

        steps.push({ step:i+1, page, memory:[...memory], result: hit?'HIT':'FAULT' });
    }

    return { steps, faults };
}

// ---------------- BELADY ----------------
function detectBeladyAnomaly(ref, frames) {
    const f1 = simulateFIFO(frames, ref);
    const f2 = simulateFIFO(frames+1, ref);

    if (f2.faults > f1.faults) {
        return {
            anomaly:true,
            f1:frames, faults1:f1.faults,
            f2:frames+1, faults2:f2.faults
        };
    }
    return { anomaly:false };
}

// ---------------- FORMAT RESULTS ----------------
function formatMemoryResult(name, result, frames) {

    const rows = result.steps.map(s => `
        <tr class="${s.result==='HIT'?'hit':'fault'}">
            <td>${s.step}</td>
            <td>${s.page}</td>
            <td>[${Array(frames).fill('-').map((_,i)=>s.memory[i]||'-').join(', ')}]</td>
            <td>${s.result}</td>
        </tr>
    `).join('');

    const faultRate = (result.faults/result.steps.length*100).toFixed(1);

    return `
        <h4>${name}</h4>
        <table class="table">
            <thead>
                <tr><th>Step</th><th>Page</th><th>Frames</th><th>Result</th></tr>
            </thead>
            <tbody>${rows}</tbody>
        </table>

        <div class="performance-metrics">
            Faults: ${result.faults} | Fault Rate: ${faultRate}%
        </div>
    `;
}

// ---------------- EXPLANATION ----------------
function getReason(name){
    if(name==='FIFO') return "Replaces oldest page → ignores usage → more faults.";
    if(name==='LRU') return "Uses recent history → avoids replacing active pages.";
    if(name==='Optimal') return "Uses future knowledge → minimum possible faults.";
}

// ---------------- COMPARISON ----------------
function formatComparisonTable(algs){

    const best = algs.reduce((a,b)=>a.faults<b.faults?a:b);
    const worst = algs.reduce((a,b)=>a.faults>b.faults?a:b);

    const rows = algs.map(a => {

        let badge = '';

        if (a.name === best.name && best.faults !== worst.faults) {
            badge = ' <span class="comparison-badge badge-best">🏆 Best</span>';
        } 
        else if (a.name === worst.name && best.faults !== worst.faults) {
            badge = ' <span class="comparison-badge badge-worst">📉 Worst</span>';
        }

        return `
            <tr>
                <td style="text-align:left;">
                    <strong>${a.name}</strong>${badge}
                </td>
                <td><strong>${a.faults}</strong></td>
                <td>${((a.faults/algs[0].totalRefs)*100).toFixed(1)}%</td>
            </tr>
        `;
    }).join('');

    return `
        <h3>🏆 Algorithm Performance Comparison</h3>

        <table class="table">
            <thead>
                <tr>
                    <th style="text-align:left;">Algorithm</th>
                    <th>Page Faults</th>
                    <th>Fault Rate</th>
                </tr>
            </thead>
            <tbody>
                ${rows}
            </tbody>
        </table>

        <div class="alert alert-info">
            <strong>💡 Explanation:</strong><br><br>

            🎯 <strong>${best.name}</strong> is BEST because it has the least faults 
            (<strong>${best.faults}</strong>).<br>
            ➤ ${getReason(best.name)}<br><br>

            📉 <strong>${worst.name}</strong> is WORST because it has the highest faults 
            (<strong>${worst.faults}</strong>).<br>
            ➤ ${getReason(worst.name)}<br><br>

            📊 Difference: <strong>${worst.faults - best.faults}</strong> faults
        </div>
    `;
}

// ---------------- BELADY UI ----------------
function formatBeladyResult(b){
    if(!b.anomaly){
        return `
        <div class="alert alert-success">
            ✅ No Belady’s Anomaly detected.
        </div>`;
    }

    return `
    <div class="alert alert-danger">
        ⚠️ Belady’s Anomaly Detected!<br>
        Frames ${b.f1} → ${b.f2}<br>
        Faults ${b.faults1} → ${b.faults2}<br><br>
        FIFO behaves inefficiently here.
    </div>`;
}


function loadMemoryExample(){
    document.getElementById('frames').value = 3;
    document.getElementById('reference-string').value =
    '7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1';
    
    showAlert('📝 Example loaded successfully!', 'success');
}

function loadRandomExample() {
    const frames = Math.floor(Math.random() * 3) + 3; // 3–5 frames
    const pages = [];
    const pageRange = Math.floor(Math.random() * 5) + 5; // 5–9 pages
    const length = Math.floor(Math.random() * 10) + 15; // 15–24 refs
    
    for (let i = 0; i < length; i++) {
        pages.push(Math.floor(Math.random() * pageRange));
    }
    
    document.getElementById('frames').value = frames;
    document.getElementById('reference-string').value = pages.join(' ');
    
    showAlert(`🎲 Random pattern generated! ${frames} frames, ${length} references`, 'info');
}

// ---------------- INIT ----------------
document.addEventListener('DOMContentLoaded', ()=>{
    loadMemoryExample();
});
function n1(n) {
    for (let i = 0; i < n; i++) {
        console.log(`n1 : print ${n}`);
    }
}

function n2(n) {
    let count = 1;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            console.log(`n2 : print ${count}`);
            count++;
        }
    }
}

function n3(n) {
    let count = 1;
    for (let a = 0; a < n; a++) {
        for (let b = 0; b < n; b++) {
            for (let c = 0; c < n; c++) {
                console.log(`n3 : print ${count}`);
                count++;
            }
        }
    }
}

function n4(n) {
    let count = 1;
    for (let a = 0; a < n; a++) {
        for (let b = 0; b < n; b++) {
            for (let c = 0; c < n; c++) {
                for (let d = 0; d < n; d++) {
                    console.log(`n4 : print ${count}`);
                    count++;
                }
            }
        }
    }
}

function n5(n) {
    let count = 1;
    for (let a = 0; a < n; a++) {
        for (let b = 0; b < n; b++) {
            for (let c = 0; c < n; c++) {
                for (let d = 0; d < n; d++) {
                    for (let e = 0; e < n; e++) {
                        console.log(`n5 : print ${count}`);
                        count++;
                    }
                }
            }
        }
    }
}

function timeAndRun(func, n, iterations) {
    const startTime = performance.now(); // Start the timer

    for (let i = 0; i < iterations; i++) func(n);
    
    const endTime = performance.now(); // End the timer
    console.clear(); // Clear console
    console.log(`Time taken to run ${iterations} iteration(s) of ${func.name}: ${((endTime - startTime) / 1000).toFixed(10)} seconds`);
}

timeAndRun(n3, 10, 10);
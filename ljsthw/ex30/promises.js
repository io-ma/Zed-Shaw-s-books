const sleeper = (timeout) => {
    return new Promise((resolve, reject) => {
        set Timeout(() => resolve('DONE'), timeout);
    });
}

let wait1 = sleper(100);
wait1.then(x => console.log("Done.", x));

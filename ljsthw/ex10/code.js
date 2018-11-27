// Exercise 10: Files, Args, Variables, Oh My

const fs = require('fs');

let file_to_open = process.argv[2];
let file_contents = fs.readFileSync(file_to_open);
let file_to_append = process.argv[3];
let hero_txt = fs.readFileSync(file_to_append);

console.log(`The file named ${file_to_open} contains:`);
console.log(file_contents.toString());

fs.appendFile('test.txt', hero_txt, (err) => {
    if (err) throw err;
    console.log('The "description of Hero" was appended to the test file!')
});

// get the file descriptor of the file to be truncated
const fd = fs.openSync('test.txt', 'r+');

// truncate the file to first four bytes
fs.ftruncate(fd, 4, (err) => {
    console.log(fs.readFileSync('test.txt', 'utf8'));
});

// puzzle: how small can you make this?

const build_adder = (left) => {
    // do I really need this variable?
    let left_hand = left;
    return adder = (right) => {
        // do I really need the return?
        let result = left_hand + right;
        return result;
    }
}

let add10 = build_adder(10);
let add20 = build_adder(20);

console.log(`test builder 3 + 10 == ${add10(3)}`);
console.log(`test builder 3 + 20 == ${add20(3)}`);
console.log(`test builder 13 + 10 == ${add10(13)}`);
console.log(`test builder 3 + 10 + 20 == ${add10(add20(3))}`);

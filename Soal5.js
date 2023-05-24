function printPattern(n) {
  if (n % 2 === 0) {
    console.log("Harus bilangan ganjil");
    return;
  }

  let pattern = [];
  for (let i = 0; i < n; i++) {
    let row = [];
    for (let j = 0; j < n; j++) {
      if (i === j || i === n - 1 - j) {
        row.push("X");
      } else {
        row.push("O");
      }
    }
    pattern.push(row);
  }

  for (let i = 0; i < n; i++) {
    console.log(pattern[i].join(""));
  }
}

printPattern(5);
console.log("");

printPattern(3);
console.log("");

printPattern(7);
console.log("");

printPattern(2);

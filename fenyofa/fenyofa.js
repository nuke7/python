let input = [6, 5000, 2500, 5300, 1900, 2400, 8800, 5300];

let min = Infinity;
let index;

function fenyo(arr) {
  for (let i = 2; i < arr.length; i++) {
    if (arr[i] > arr[1] && arr[i] < min) {
      min = arr[i];
      index = i - 1;
    }
  }
  if (min === Infinity) {
    console.log(-1);
  } else {
    console.log(`${index} ${min}`);
  }
}

fenyo(input);

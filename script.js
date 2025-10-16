/*num = 3;
for (i = 1; i <= 10; i++) {
  console.log(`${num} * ${i} = ${num * i}`);
}*/
/*
let i = 1;
while (i <= 5) {
  console.log(i);
  i = i + 1;
}*/
/*
let i = 1;
do {
  console.log(i);
  i = i + 1;
} while (i <= 11);*/
/*
let word = "teja";
let revword = " ";
for (i = 0; i <= word.length; i++) {
  revword = word[i] + revword;
}
console.log(revword);*/

/*
let word1 = "hima";
let wordrev = "";
for (i = 0; i <= word1.length; i++) {
  wordrev = word1[i] + wordrev;
}
console.log(wordrev);*/
/*
for (i = 0; i <= 2; i++) {
  console.log(i);
  for (j = 3; j <= 6; j++) {
    console.log(j);
    for (k = 7; k <= 10; k++) {
      console.log(k);
    }
  }
}*/
/*
function add(n1, n2, func) {
  result = n1 + n2;
  return func(result);
  return 1;
}
function display(func) {
  console.log(func);
}
add(1, 2, display);*/

/*
function add(n1, n2) {
  result = n1 + n2;
  return display(result);
}
function display(func) {
  console.log(func);
}
add(10, 20);*/
/*
const greet = function () {
  console.log("hello greet");
  return 1
};
let obj = [greet];
console.log(obj[0]());*/

const gret = function () {
  console.log("hello world");
  return 1;
};
let obj = {
  func: gret,
};
console.log(obj.func());

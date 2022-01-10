function solution(s) {
  let answer = 1;
  for (let i = s.length; i >= 1; i--) {
    for (let j = 0; j <= s.length - i; j++) {
      if (isPalindrome(s.slice(j, i + j))) {
        return i;
      }
    }
  }
  return answer;
}

function isPalindrome(s) {
  for (let i = 0; i < s.length / 2; i++) {
    if (s[i] !== s[s.length - i - 1]) {
      return false;
    }
  }
  return true;
}

console.log(solution("abcdcba"));
console.log(solution("abacde"));

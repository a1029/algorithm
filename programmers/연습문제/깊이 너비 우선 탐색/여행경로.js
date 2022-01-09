let visit;
let answer = [];

function dfs(now, count, tickets) {
  if (count === tickets.length) {
    answer.push(now);
    return;
  }
  for (let i = 0; i < tickets.length; i++) {
    if (now[now.length - 1] !== tickets[i][0] || visit[i]) {
      continue;
    }
    visit[i] = true;
    dfs([...now, tickets[i][1]], count + 1, tickets);
    visit[i] = false;
  }
}

function solution(tickets) {
  visit = Array(tickets.length).fill(false);
  dfs(["ICN"], 0, tickets);

  answer.sort();
  return answer[0];
}

console.log(
  solution([
    ["ICN", "SFO"],
    ["ICN", "ATL"],
    ["SFO", "ATL"],
    ["ATL", "ICN"],
    ["ATL", "SFO"],
  ])
);

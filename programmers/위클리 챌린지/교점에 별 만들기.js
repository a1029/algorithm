function solution(line) {
  const n = line.length;
  const INF = Number.MAX_SAFE_INTEGER;
  const meet = [];
  let maxY = -INF;
  let maxX = -INF;
  let minY = INF;
  let minX = INF;

  for (let i = 0; i < n - 1; i++) {
    for (let j = i + 1; j < n; j++) {
      const [a, b, e] = line[i];
      const [c, d, f] = line[j];

      const mod = a * d - b * c;
      if (!mod) continue;

      let xNumerator = b * f - e * d;
      let yNumerator = e * c - a * f;
      if (xNumerator % mod || yNumerator % mod) continue;

      let x = xNumerator / mod;
      let y = yNumerator / mod;

      meet.push([x, y]);
      minX = Math.min(minX, x);
      minY = Math.min(minY, y);
      maxX = Math.max(maxX, x);
      maxY = Math.max(maxY, y);
    }
  }

  let answer = [...Array(maxY - minY + 1)].map(() =>
    [...Array(maxX - minX + 1)].map(() => ".")
  );

  meet.forEach(([x, y]) => {
    answer[maxY - y][x - minX] = "*";
  });

  answer = answer.map((v) => v.join(""));
  return answer;
}

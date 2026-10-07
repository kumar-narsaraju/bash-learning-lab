// Minimal browser replacement for the "diff" package: just diffArrays (LCS based), as used by just-bash `diff`.
export function diffArrays(a, b) {
  const n = a.length, m = b.length;
  const dp = Array.from({ length: n + 1 }, () => new Int32Array(m + 1));
  for (let i = n - 1; i >= 0; i--) for (let j = m - 1; j >= 0; j--)
    dp[i][j] = a[i] === b[j] ? dp[i + 1][j + 1] + 1 : Math.max(dp[i + 1][j], dp[i][j + 1]);
  const parts = [];
  const push = (kind, v) => {
    const last = parts[parts.length - 1];
    const added = kind === "add", removed = kind === "del";
    if (last && !!last.added === added && !!last.removed === removed) { last.value.push(v); last.count++; }
    else parts.push({ value: [v], count: 1, added, removed });
  };
  let i = 0, j = 0;
  while (i < n && j < m) {
    if (a[i] === b[j]) { push("same", a[i]); i++; j++; }
    else if (dp[i + 1][j] >= dp[i][j + 1]) push("del", a[i++]);
    else push("add", b[j++]);
  }
  while (i < n) push("del", a[i++]);
  while (j < m) push("add", b[j++]);
  return parts;
}
export default { diffArrays };

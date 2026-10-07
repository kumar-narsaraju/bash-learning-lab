// Minimal browser replacement for the "sprintf-js" package (only sprintf is needed by just-bash printf).
export function sprintf(fmt, ...args) {
  let ai = 0;
  const out = fmt.replace(/%(%|([-+ 0#]*)(\d+)?(?:\.(\d+))?([bcdieEfFgGosuxX]))/g, (m, all, flags, width, prec, type) => {
    if (all === "%") return "%";
    flags = flags || "";
    if (ai >= args.length) throw new Error("[sprintf] too few arguments");
    const arg = args[ai++];
    let s, sign = "";
    const num = () => { const n = Number(arg); if (Number.isNaN(n)) throw new TypeError("[sprintf] expecting number but found " + typeof arg); return n; };
    switch (type) {
      case "s": s = String(arg); if (prec !== undefined) s = s.slice(0, +prec); break;
      case "c": s = String.fromCharCode(num()); break;
      case "b": s = (num() >>> 0).toString(2); break;
      case "o": s = (num() >>> 0).toString(8); break;
      case "x": s = Math.trunc(num()).toString(16); break;
      case "X": s = Math.trunc(num()).toString(16).toUpperCase(); break;
      case "d": case "i": case "u": { const n = Math.trunc(num()); s = Math.abs(n).toString(); sign = n < 0 ? "-" : flags.includes("+") ? "+" : flags.includes(" ") ? " " : ""; break; }
      case "e": case "E": { const n = num(); s = Math.abs(n).toExponential(prec === undefined ? 6 : +prec).replace(/e([+-])(\d)$/, "e$10$2"); if (type === "E") s = s.toUpperCase(); sign = n < 0 ? "-" : flags.includes("+") ? "+" : ""; break; }
      case "f": case "F": { const n = num(); s = Math.abs(n).toFixed(prec === undefined ? 6 : +prec); sign = n < 0 ? "-" : flags.includes("+") ? "+" : flags.includes(" ") ? " " : ""; break; }
      case "g": case "G": { const n = num(); const p = prec === undefined ? 6 : (+prec || 1); s = String(Number(Math.abs(n).toPrecision(p))); if (type === "G") s = s.toUpperCase(); sign = n < 0 ? "-" : flags.includes("+") ? "+" : ""; break; }
    }
    let body = sign + s;
    if (width && body.length < +width) {
      if (flags.includes("-")) body = body.padEnd(+width, " ");
      else if (flags.includes("0") && !"sc".includes(type)) body = sign + s.padStart(+width - sign.length, "0");
      else body = body.padStart(+width, " ");
    }
    return body;
  });
  return out;
}
export function vsprintf(fmt, argv) { return sprintf(fmt, ...argv); }
export default { sprintf, vsprintf };

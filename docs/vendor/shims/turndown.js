// Tiny stand-in for "turndown" (html-to-markdown command). Crude but dependency-free.
export default class TurndownService {
  constructor(o = {}) { this.o = o; this.removed = []; }
  remove(tags) { this.removed = this.removed.concat(tags); return this; }
  turndown(html) {
    let s = String(html);
    for (const t of this.removed) s = s.replace(new RegExp(`<${t}[\\s\\S]*?</${t}>`, "gi"), "");
    s = s.replace(/<h([1-6])[^>]*>([\s\S]*?)<\/h\1>/gi, (_, l, t) => "\n" + "#".repeat(+l) + " " + t.trim() + "\n")
         .replace(/<li[^>]*>([\s\S]*?)<\/li>/gi, "\n- $1")
         .replace(/<(strong|b)[^>]*>([\s\S]*?)<\/\1>/gi, "**$2**")
         .replace(/<(em|i)[^>]*>([\s\S]*?)<\/\1>/gi, "_$2_")
         .replace(/<code[^>]*>([\s\S]*?)<\/code>/gi, "`$1`")
         .replace(/<a [^>]*href="([^"]*)"[^>]*>([\s\S]*?)<\/a>/gi, "[$2]($1)")
         .replace(/<br\s*\/?>/gi, "\n").replace(/<\/p>/gi, "\n\n").replace(/<[^>]+>/g, "");
    return s.replace(/\n{3,}/g, "\n\n").trim();
  }
}

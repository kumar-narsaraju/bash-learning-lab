#!/usr/bin/env python3
"""Builds docs/index.html (the online learning site) from modules/*/lesson.md."""
import glob, html, json, os, markdown
repo = os.environ.get("GITHUB_REPOSITORY", "<your-username>/bash-learning-lab")
QUIZ = {
"01": [("What does the shebang line do?", ["Comments the file","Tells Linux which program runs the script","Prints text","Deletes the file"], 1), ("Which command makes a script executable?", ["chmod +x script.sh","run script.sh","exec +x","mod 777"], 0)],
"02": [("Which assigns a variable correctly?", ["x = 5","x=5","$x=5","set x 5"], 1), ("With a=2 and b=3, what prints 5?", ["echo a+b","echo $a+$b","echo $((a+b))","echo (a+b)"], 2)],
"03": [("Which exit code means success?", ["1","0","-1","255"], 1), ("Which test checks that a regular file exists?", ["-d","-f","-z","-n"], 1)],
"04": [("How many lines does: for i in {1..3}; do echo $i; done print?", ["1","2","3","Error"], 2), ("What does break do?", ["Skips one round","Leaves the loop","Restarts the loop","Pauses"], 1)],
"05": [("Inside a script, what is $1?", ["The script name","The first argument","All arguments","The exit code"], 1), ("What does local do in a function?", ["Makes the variable global","Keeps it inside the function","Deletes it","Exports it"], 1)],
"06": [("Which command counts lines?", ["wc -l","cut","sed","uniq"], 0), ("What does >> do?", ["Overwrites a file","Appends to a file","Reads a file","Pipes output"], 1)],
"07": [("Which keyword ends a case block?", ["fi","done","esac","end"], 2), ("What does ${#arr[@]} give?", ["Last item","Number of items","First item","Length of first item"], 1)],
"08": [("What does set -u do?", ["Stops on any error","Errors on unset variables","Unsets variables","Turns on debug"], 1), ("Where should error messages go?", ["stdout","stderr (>&2)","/dev/null","A pipe"], 1)],
"09": [("What does the cron time 30 2 * * * mean?", ["Every 30 minutes","Every day at 02:30","Monthly","Sundays at 2:30"], 1), ("Why use full paths in cron?", ["It is faster","Cron has a minimal environment and PATH","Bash requires it","No reason"], 1)],
"10": [("What does ${#word} give?", ["First character","Length of the word","Number of words","Uppercase word"], 1), ("Best first step in a project?", ["Write all the code","Plan input, steps and output","Copy from the web","Skip testing"], 1)],
}
mods = []
for d in sorted(glob.glob("modules/*/")):
    n = os.path.basename(d.rstrip("/"))
    num = n.split("-")[0]
    md = open(f"{d}lesson.md").read()
    body = markdown.markdown(md, extensions=["fenced_code", "tables"])
    exp = html.escape(open(f"{d}expected.txt").read())
    sol = html.escape(open(f"{d}solution.sh").read())
    title = md.splitlines()[0].lstrip("# ").strip()
    rd = lambda f: open(f"{d}{f}").read() if os.path.exists(f"{d}{f}") else ""
    raw = dict(input=rd("input.txt").rstrip("\n"), expected=rd("expected.txt").rstrip("\n"), args=rd("args.txt").strip())
    mods.append(dict(num=num, title=title, body=body, exp=exp, sol=sol, quiz=QUIZ.get(num, []), raw=raw))
TRACKS = {"datacenter": "Data Center SysAdmin Projects", "hardware": "Server Hardware Troubleshooting"}
projs = []
for t in TRACKS:
    for d in sorted(glob.glob(f"projects/{t}/*/")):
        if not os.path.exists(f"{d}expected.txt"): continue
        pid = os.path.basename(d.rstrip("/"))
        md = open(f"{d}README.md").read()
        title = md.splitlines()[0].lstrip("# ").strip()
        skip = {"README.md", "solution.sh", "expected.txt"}
        files = {f: open(f"{d}{f}").read() for f in sorted(os.listdir(d)) if f not in skip}
        key = t[:2] + pid.split("-")[0]
        projs.append(dict(key=key, track=t, id=pid, title=title, body=markdown.markdown(md, extensions=["fenced_code"]), files=files,
                          expected=open(f"{d}expected.txt").read(), sol=open(f"{d}solution.sh").read()))
IMAP_TAG = '<script type="importmap">{"imports":{"sprintf-js":"./vendor/shims/sprintf-js.js","diff":"./vendor/shims/diff.js","turndown":"./vendor/shims/turndown.js","node:zlib":"./vendor/shims/node-zlib.js"}}</script>'
page = """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Bash Learning Lab</title><script type="importmap">{"imports":{"sprintf-js":"./vendor/shims/sprintf-js.js","diff":"./vendor/shims/diff.js","turndown":"./vendor/shims/turndown.js","node:zlib":"./vendor/shims/node-zlib.js"}}</script><style>
:root{--bg:#fff;--fg:#14202e;--card:#f3f6fa;--ac:#0e9f8a;--code:#0b1220;--cf:#e8eef5}
@media(prefers-color-scheme:dark){:root{--bg:#0f1722;--fg:#e6edf5;--card:#18222f;--ac:#18e0c1;--code:#070c14;--cf:#e8eef5}}
*{box-sizing:border-box}body{margin:0;font:16px/1.6 system-ui,sans-serif;background:var(--bg);color:var(--fg);display:flex;min-height:100vh}
nav{width:260px;padding:16px;background:var(--card);position:sticky;top:0;height:100vh;overflow:auto}
nav h1{font-size:18px;margin:0 0 12px}nav a{display:block;padding:6px 8px;border-radius:6px;color:var(--fg);text-decoration:none;font-size:14px;cursor:pointer}
nav a.on{background:var(--ac);color:#fff}main{flex:1;max-width:820px;padding:24px;margin:0 auto}
pre{background:var(--code);color:var(--cf);padding:12px;border-radius:8px;overflow:auto;font-size:14px}code{font-family:ui-monospace,monospace}
.card{background:var(--card);border-radius:10px;padding:14px;margin:16px 0}.btn{display:inline-block;background:var(--ac);color:#fff;border:0;border-radius:8px;padding:8px 14px;text-decoration:none;cursor:pointer;font-size:15px}
.q p{margin:8px 0 4px;font-weight:600}.q label{display:block;cursor:pointer}.ok{color:#16a34a}.no{color:#dc2626}
textarea{width:100%;background:var(--code);color:var(--cf);border:0;border-radius:8px;padding:10px;font:14px ui-monospace,monospace}
.out{min-height:40px;white-space:pre-wrap}#term{background:var(--code);color:var(--cf);border-radius:10px;padding:12px;font:14px ui-monospace,monospace}
#tout{margin:0;padding:0;background:none;white-space:pre-wrap;max-height:340px;overflow:auto}#trow{display:flex;gap:6px}#tin{flex:1;background:none;border:0;outline:0;color:inherit;font:inherit}
@media(max-width:760px){body{display:block}nav{width:100%;height:auto;position:static}}</style></head><body>
<nav><h1>Bash Learning Lab</h1><a id="l-home" onclick="show('home')">Start here</a>%NAV%</nav><main>
<section id="home"><h1>Learn Bash scripting online</h1><p>Read a lesson, test yourself with the quiz, then practise in a real Linux terminal in your browser: no install needed.</p>
<div class="card"><b>Bash terminal, running right here in your browser.</b> No sign-in, no install. Try: <code>echo "Hello"</code>, <code>ls</code>, <code>cat data.csv</code>, <code>cut -d, -f1 data.csv | sort</code>, <code>x=5</code> then <code>echo $((x*2))</code>. Type <code>help-lab</code> for ideas. Files you create stay until you reload.</div>
<div id="term"><pre id="tout">Loading bash...</pre><div id="trow"><span id="tprompt">$</span><input id="tin" autocomplete="off" spellcheck="false" autofocus></div></div>
<div class="card"><b>Step 2.</b> Open a module on the left: read the lesson, answer the quiz, write your script in the built-in editor and press <b>Check answer</b>.</div>
<div class="card"><b>Step 3.</b> Build your own tools from the <a href="https://github.com/%REPO%/tree/main/projects">projects</a> and share them with a pull request.</div></section>
%SECTIONS%</main><script>
const M=%DATA%;
function show(id){document.querySelectorAll('section').forEach(s=>s.hidden=s.id!==id);document.querySelectorAll('nav a').forEach(a=>a.classList.toggle('on',a.id==='l-'+id));scrollTo(0,0);location.hash=id}
function ans(m,i,j,c,el){const r=document.getElementById('r'+m+'_'+i);r.textContent=j===c?'Correct!':'Not quite. Re-read the lesson.';r.className=j===c?'ok':'no'}
show((location.hash||'#home').slice(1)||'home');
</script>%MODJS%</body></html>"""
def plink(p): return '<a id="l-m%s" onclick="show(&quot;m%s&quot;)">%s. %s</a>' % (p["key"], p["key"], p["key"][2:], html.escape(p["title"]))
pnav = "".join('<small style="display:block;margin:12px 8px 4px;opacity:.7">%s</small>' % html.escape(name) + "".join(plink(p) for p in projs if p["track"] == t) for t, name in TRACKS.items())
nav = '<a href="terminal.html" style="font-weight:600">&gt;_ Full terminal</a>' + "".join(f'<a id="l-m{m["num"]}" onclick="show(\'m{m["num"]}\')">{m["num"]}. {html.escape(m["title"].split(": ",1)[-1])}</a>' for m in mods) + pnav
secs = ""
for m in mods:
    q = ""
    for i, (t, opts, c) in enumerate(m["quiz"]):
        o = "".join(f'<label><input type="radio" name="q{m["num"]}_{i}" onclick="ans(\'{m["num"]}\',{i},{j},{c})"> {html.escape(x)}</label>' for j, x in enumerate(opts))
        q += f'<div class="q"><p>{i+1}. {html.escape(t)}</p>{o}<small id="r{m["num"]}_{i}"></small></div>'
    secs += f'''<section id="m{m["num"]}" hidden>{m["body"]}
<div class="card"><b>Quick quiz</b>{q}</div>
<details class="card"><summary>Expected output for the exercise</summary><pre>{m["exp"]}</pre></details>
<details class="card"><summary>Show reference solution (try first!)</summary><pre>{m["sol"]}</pre></details>
<div class="card"><b>Write your script here (answer.sh)</b><br><small>Your script receives this as input: <code>{html.escape(m["raw"]["input"]) or "(nothing)"}</code>{(" and arguments: <code>"+html.escape(m["raw"]["args"])+"</code>") if m["raw"]["args"] else ""}</small>
<textarea id="ed{m["num"]}" rows="9" spellcheck="false">#!/usr/bin/env bash\n# write your solution here\n</textarea>
<p><button class="btn" onclick="runMod('{m["num"]}',false)">Run</button> <button class="btn" onclick="runMod('{m["num"]}',true)">Check answer</button></p><pre class="out" id="out{m["num"]}"></pre></div></section>'''
for p in projs:
    fv = "".join(f"<details><summary><code>{html.escape(f)}</code></summary><pre>{html.escape(c)}</pre></details>" for f, c in p["files"].items())
    secs += f'''<section id="m{p["key"]}" hidden>{p["body"]}
<div class="card"><b>Sample data (already loaded in the editor's sandbox)</b>{fv}</div>
<details class="card"><summary>Expected output</summary><pre>{html.escape(p["expected"])}</pre></details>
<details class="card"><summary>Show reference solution (try first!)</summary><pre>{html.escape(p["sol"])}</pre></details>
<div class="card"><b>Write your script here (answer.sh)</b>
<textarea id="ed{p["key"]}" rows="9" spellcheck="false">#!/usr/bin/env bash\n# the sample files are in the current folder\n</textarea>
<p><button class="btn" onclick="runMod('{p["key"]}',false)">Run</button> <button class="btn" onclick="runMod('{p["key"]}',true)">Check answer</button></p><pre class="out" id="out{p["key"]}"></pre></div></section>'''
import json
MODJS = r'''<script type="module">
let Bash, mountTerminal, bootErr = "";
try { ({ Bash } = await import("./vendor/just-bash.js?v=2")); ({ mountTerminal } = await import("./terminal.js?v=2")); } catch (e) { bootErr = "Terminal failed to start:\n" + (e && e.message || e) + (location.protocol === "file:" ? "\n\nYou opened this as a local file. Use the website (github.io) or run: python -m http.server inside docs." : "\n\nTry Ctrl+F5 (hard refresh)."); }
const D = %DATA%;
const HOME = "/home/user";
window.runMod = async (n, check) => {
  const o = document.getElementById("out" + n), m = D[n];
  o.textContent = "Running...";
  try {
    const files = { [HOME + "/answer.sh"]: document.getElementById("ed" + n).value };
    if (m.files) for (const [f, c] of Object.entries(m.files)) files[HOME + "/" + f] = c;
    else files[HOME + "/input.txt"] = m.input + "\n";
    const sh = new Bash({ files });
    const r = await sh.exec(m.files ? "bash answer.sh" : `bash answer.sh ${m.args} < input.txt`, { cwd: HOME });
    let t = r.stdout + (r.stderr ? "\n[errors]\n" + r.stderr : "");
    if (check) t += r.stdout.trimEnd() === m.expected.trimEnd() ? "\n\u2705 PASS: your output matches!" : "\n\u274c FAIL. Expected:\n" + m.expected;
    o.textContent = t || "(no output)";
  } catch (e) { o.textContent = "Error: " + e.message; }
};
if (bootErr) document.getElementById("tout").textContent = bootErr; else mountTerminal(document.getElementById("tout"), document.getElementById("tin"), document.getElementById("tprompt"), document.getElementById("term"));
</script>'''
TERMJS = r'''import { Bash } from "./vendor/just-bash.js?v=2";
const HOME = "/home/user";
const FILES = %FILES%;
export function mountTerminal(out, inp, pr, box) {
  const files = { ...FILES, ["/tmp/.keep"]: "" };
  let T;
  try { T = new Bash({ files }); } catch (e) { out.textContent = "Could not start bash: " + e.message; return; }
  let cwd = HOME, prelude = [], hist = [], hi = 0;
  const show = s => { out.textContent += s; out.scrollTop = out.scrollHeight; };
  out.textContent = "Welcome! Type a command and press Enter. Try: help-lab\n";
  const DEF = /^\s*([A-Za-z_]\w*(\[[^\]]*\])?\+?=|[A-Za-z_][\w-]*\s*\(\)|function\s|export\s|alias\s)/;
  inp.addEventListener("keydown", async e => {
    if (e.key === "ArrowUp") { if (hi > 0) inp.value = hist[--hi]; e.preventDefault(); return; }
    if (e.key === "ArrowDown") { inp.value = hi < hist.length - 1 ? hist[++hi] : ""; hi = Math.min(hi + 1, hist.length); e.preventDefault(); return; }
    if (e.key !== "Enter") return;
    const line = inp.value; inp.value = ""; show(pr.textContent + " " + line + "\n");
    if (!line.trim()) return;
    hist.push(line); hi = hist.length;
    if (line.trim() === "clear") { out.textContent = ""; return; }
    if (line.trim() === "help-lab") { show("Practice files: data.csv notes.txt hello.sh\nData center: cd projects/datacenter/01-rack-inventory ; cat inventory.csv\nHardware:    cd projects/hardware/01-ipmi-event-triage ; cat sel.txt\nIdeas: ls | grep ERROR notes.txt | wc -l notes.txt | for i in {1..3}; do echo $i; done\nTip: variables and one-line functions are remembered. Reload the page to reset files.\n"); return; }
    const script = "{ " + prelude.join("\n") + "\n} >/dev/null 2>&1\n" + line + '\n__rc=$?; echo "@@CWD@@$PWD" >&2; exit $__rc';
    try {
      const r = await T.exec(script, { cwd });
      let err = r.stderr, m = err.match(/@@CWD@@(.*)\n?/);
      if (m) { cwd = m[1]; err = err.replace(/@@CWD@@.*\n?/, ""); pr.textContent = cwd.replace(HOME, "~") + " $"; }
      show(r.stdout + err);
      if (!r.stdout.endsWith("\n") && r.stdout) show("\n");
      if (DEF.test(line) && r.exitCode === 0) prelude.push(line);
    } catch (e) { show("error: " + e.message + "\n"); }
  });
  box.addEventListener("click", () => inp.focus());
}
'''
DATA = json.dumps({**{m["num"]: m["raw"] for m in mods}, **{p["key"]: dict(files=p["files"], expected=p["expected"].rstrip("\n")) for p in projs}})
out = page.replace("%MODJS%", MODJS.replace("%DATA%", DATA)).replace("%NAV%", nav).replace("%SECTIONS%", secs).replace("%REPO%", repo).replace("%DATA%", "null")
os.makedirs("docs", exist_ok=True)
open("docs/index.html", "w").write(out)
H = "/home/user/"
FILES = {H + "data.csv": "ravi,80\nmeena,90\nkiran,70\n", H + "notes.txt": "linux is fun\nbash scripting is powerful\nERROR disk full\nWARN low memory\nERROR disk full\n", H + "hello.sh": '#!/usr/bin/env bash\necho "Hello from a script"\n'}
for p in projs:
    for f, c in p["files"].items(): FILES[f"{H}projects/{p['track']}/{p['id']}/{f}"] = c
open("docs/terminal.js", "w").write(TERMJS.replace("%FILES%", json.dumps(FILES)))
STYLE = page[page.index("<style>"):page.index("</style>") + 8]
open("docs/terminal.html", "w").write("""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Bash Terminal | Bash Learning Lab</title>""" + IMAP_TAG + STYLE + """<style>body{display:block;padding:16px}#term{max-width:1000px;margin:0 auto;min-height:70vh}#tout{max-height:70vh;min-height:60vh}</style></head><body>
<p style="text-align:center"><a href="index.html">&larr; Back to lessons</a> &nbsp;|&nbsp; Full in-browser bash terminal. Type <code>help-lab</code> for sample data centre and hardware files.</p>
<div id="term"><pre id="tout">Loading bash...</pre><div id="trow"><span id="tprompt">~ $</span><input id="tin" autocomplete="off" spellcheck="false" autofocus></div></div>
<script type="module">async function boot(){const o=document.getElementById("tout");
if(location.protocol==="file:"){o.textContent="This page was opened as a local file (file://). Browsers block the terminal engine there.\\nOpen the website instead: https://<your-username>.github.io/bash-learning-lab/terminal.html\\nOr run: python -m http.server 8000   (inside the docs folder) and open http://localhost:8000/terminal.html";return}
try{const m=await import("./terminal.js?v=2");m.mountTerminal(o,document.getElementById("tin"),document.getElementById("tprompt"),document.getElementById("term"))}
catch(e){o.textContent="Terminal failed to start:\\n"+(e&&e.message||e)+"\\n\\nPlease send this message. Also try Ctrl+F5 (hard refresh) in case the old page is cached."}}
boot();</script></body></html>""")
print("built docs/index.html, terminal.html, terminal.js with", len(mods), "modules and", len(projs), "projects")

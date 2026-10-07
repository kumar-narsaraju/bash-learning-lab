import { Bash } from "./vendor/just-bash.js?v=2";
const HOME = "/home/user";
const FILES = {"/home/user/data.csv": "ravi,80\nmeena,90\nkiran,70\n", "/home/user/notes.txt": "linux is fun\nbash scripting is powerful\nERROR disk full\nWARN low memory\nERROR disk full\n", "/home/user/hello.sh": "#!/usr/bin/env bash\necho \"Hello from a script\"\n", "/home/user/projects/datacenter/01-rack-inventory/inventory.csv": "hostname,rack,u,role,status\nweb01,R01,10,web,online\nweb02,R01,11,web,online\ndb01,R01,20,database,maintenance\ngpu01,R02,5,gpu,online\ngpu02,R02,7,gpu,offline\nstor01,R03,2,storage,online\n", "/home/user/projects/datacenter/02-disk-space-alert/df.txt": "Filesystem      Size  Used Avail Use% Mounted on\n/dev/sda2        50G   41G  9.0G  82% /\n/dev/sdb1       2.0T  1.1T  900G  55% /data\n/dev/sdc1       4.0T  3.8T  200G  95% /backup\ntmpfs           16G     0   16G   0% /dev/shm\n", "/home/user/projects/datacenter/03-failed-ssh-logins/auth.log": "Oct  7 01:02:11 srv sshd[411]: Failed password for root from 203.0.113.9 port 4022 ssh2\nOct  7 01:02:14 srv sshd[411]: Failed password for root from 203.0.113.9 port 4023 ssh2\nOct  7 01:05:40 srv sshd[502]: Accepted password for admin from 10.0.0.5 port 5100 ssh2\nOct  7 01:09:01 srv sshd[611]: Failed password for invalid user test from 198.51.100.7 port 3111 ssh2\nOct  7 01:09:05 srv sshd[611]: Failed password for root from 203.0.113.9 port 4030 ssh2\n", "/home/user/projects/datacenter/04-patch-and-reboot-list/servers.txt": "web01 12 5.15.0-91\nweb02 140 5.15.0-60\ndb01 95 5.15.0-60\ngpu01 30 5.15.0-91\nstor01 400 5.4.0-100\n", "/home/user/projects/hardware/01-ipmi-event-triage/sel.txt": "1 | 10/05/2026 | 02:11:09 | Temperature CPU1 | Upper Critical going high | Asserted\n2 | 10/05/2026 | 02:14:31 | Fan FAN3 | Lower Non-recoverable going low | Asserted\n3 | 10/06/2026 | 11:00:00 | Power Supply PS2 | Presence detected | Deasserted\n4 | 10/06/2026 | 11:00:05 | Memory DIMM_B2 | Uncorrectable ECC | Asserted\n5 | 10/07/2026 | 06:30:12 | Drive Slot Bay4 | Drive Fault | Asserted\n", "/home/user/projects/hardware/02-temperature-and-fans/sensors.txt": "CPU1 Temp | 92.000 | degrees C | cr\nCPU2 Temp | 61.000 | degrees C | ok\nFAN1 | 8400.000 | RPM | ok\nFAN3 | 0.000 | RPM | cr\nPS1 Status | 0x1 | discrete | ok\nInlet Temp | 38.000 | degrees C | nc\n", "/home/user/projects/hardware/03-disk-health-scan/smart.txt": "/dev/sda 0 0 Samsung_PM883\n/dev/sdb 12 0 Seagate_ST4000\n/dev/sdc 0 3 WDC_WD4003\n/dev/sdd 0 0 Samsung_PM883\n", "/home/user/projects/hardware/04-memory-ecc-errors/edac.txt": "DIMM_A1 ce=0 ue=0\nDIMM_A2 ce=250 ue=0\nDIMM_B1 ce=3 ue=0\nDIMM_B2 ce=10 ue=1\n"};
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

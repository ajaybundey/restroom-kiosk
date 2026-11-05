"""python3 tests/autosave_test.py -- a Settings box still being typed in must save on Lock and on a tab switch.
Runs Restroom_Kiosk.html in headless Chrome (macOS path) with a test hook added to a temporary copy."""
import pathlib, re, subprocess, sys, tempfile

CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
src = (pathlib.Path(__file__).parent.parent / 'Restroom_Kiosk.html').read_text()
i = src.rindex('})();')
src = src[:i] + '  window.__k = { mutate, unlockTeacher, lockTeacher, openTab };\n' + src[i:]
test = r"""<script>addEventListener('load', () => setTimeout(() => {
  const k = window.__k, results = [];
  const stored = () => JSON.parse(localStorage.getItem('restroomKiosk.v2')).settings.passLabel;
  const typeLabel = v => {  // type without leaving the box, so no change event fires
    const box = [...document.querySelectorAll('#tBody input[type=text]')].find(x => x.maxLength === 40);
    box.focus(); box.value = v;
  };
  k.mutate(s => { s.setup = { done: true, step: 'roster' }; });
  k.unlockTeacher(); k.openTab('settings'); typeLabel('Lock test'); k.lockTeacher();
  results.push(stored() === 'Lock test' ? 'ok lock' : 'FAIL lock: ' + stored());
  k.unlockTeacher(); k.openTab('settings'); typeLabel('Tab test'); k.openTab('now');
  results.push(stored() === 'Tab test' ? 'ok tab' : 'FAIL tab: ' + stored());
  document.title = 'RESULT ' + results.join(' | ');
}, 500));</script>"""
d = pathlib.Path(tempfile.mkdtemp())
page = d / 'p.html'; page.write_text(src.replace('</body>', test + '</body>', 1))
out = subprocess.run([CHROME, '--headless=new', '--disable-gpu', f'--user-data-dir={d}/p', '--virtual-time-budget=5000', '--dump-dom', page.as_uri()],
                     capture_output=True, text=True, timeout=120).stdout
m = re.search(r'<title>RESULT (.*?)</title>', out)
print(m.group(1) if m else 'FAIL: the test did not finish')
sys.exit(0 if m and 'FAIL' not in m.group(1) else 1)

const form = document.getElementById('checker');
const result = document.getElementById('result');
const clearBtn = document.getElementById('clear');

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const url = document.getElementById('url').value.trim();
  if (!url) return alert('Enter a URL');
  result.classList.add('hidden');
  try {
    const resp = await fetch('/analyze', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ url })
    });
    const data = await resp.json();
    renderResult(data);
  } catch (err) {
    renderResult({ error: 'Request failed' });
  }
});

clearBtn.addEventListener('click', () => {
  document.getElementById('url').value = '';
  result.classList.add('hidden');
});

function badgeColor(verdict) {
  if (verdict === 'Likely Scam') return 'bg-red-100 text-red-700';
  if (verdict === 'Suspicious') return 'bg-amber-100 text-amber-700';
  return 'bg-emerald-100 text-emerald-700';
}

function renderResult(data) {
  if (data.error) {
    result.innerHTML = `<div class='text-red-600'>${data.error}</div>`;
    result.classList.remove('hidden');
    return;
  }
  const { score, verdict, features } = data;
  result.innerHTML = `
    <div class='p-4 border rounded'>
      <div class='flex items-center justify-between'>
        <div class='font-semibold text-lg'>Verdict</div>
        <span class='px-2 py-1 rounded text-sm ${badgeColor(verdict)}'>${verdict}</span>
      </div>
      <div class='mt-2 text-sm text-slate-700'>Score: <span class='font-mono'>${score}</span></div>
      <pre class='mt-3 text-xs bg-slate-50 p-3 rounded overflow-auto'>${JSON.stringify(features, null, 2)}</pre>
    </div>
  `;
  result.classList.remove('hidden');
}



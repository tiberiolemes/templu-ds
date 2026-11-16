// Catálogo local: sem backend, persistência ou envio de dados. Texto livre entra apenas via textContent.
const $ = (selector) => document.querySelector(selector);
const toast = $('#toast');
let noticeTimer;
function notice(message) {
  clearTimeout(noticeTimer);
  toast.textContent = message;
  toast.hidden = false;
  noticeTimer = setTimeout(() => { toast.hidden = true; }, 5000);
}
$('#theme').addEventListener('click', () => {
  const dark = document.documentElement.classList.toggle('dark');
  $('#theme').setAttribute('aria-pressed', String(dark));
  $('#theme').setAttribute('aria-label', dark ? 'Ativar tema claro' : 'Ativar tema escuro');
});
document.querySelectorAll('[data-notice]').forEach(button => {
  button.addEventListener('click', () => notice(button.dataset.notice));
});
document.querySelectorAll('[data-copy]').forEach(button => {
  button.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(button.dataset.copy);
      notice(`Cor ${button.dataset.copy} copiada.`);
    } catch {
      notice(`Cor: ${button.dataset.copy}. Selecione e copie o código exibido.`);
    }
  });
});
const rows = () => [...document.querySelectorAll('#people-body tr')];
function filterPeople() {
  const query = $('#people-search').value.trim().toLocaleLowerCase('pt-BR');
  let visible = 0;
  rows().forEach(row => {
    row.hidden = !row.textContent.toLocaleLowerCase('pt-BR').includes(query);
    if (!row.hidden) visible++;
  });
  $('#people-empty').hidden = visible > 0;
  $('#people-count').textContent = `${visible} ${visible === 1 ? 'pessoa de exemplo' : 'pessoas de exemplo'}`;
}
$('#people-search').addEventListener('input', filterPeople);
$('#example-name').addEventListener('input', () => {
  $('#example-name').removeAttribute('aria-invalid');
  $('#name-error').hidden = true;
});
$('#example-form').addEventListener('submit', event => {
  event.preventDefault();
  const name = $('#example-name').value.trim();
  if (!name) {
    $('#example-name').setAttribute('aria-invalid', 'true');
    $('#name-error').hidden = false;
    $('#example-name').focus();
    return;
  }
  const row = document.createElement('tr');
  const person = document.createElement('td');
  const avatar = document.createElement('span');
  avatar.className = 'avatar violet';
  avatar.textContent = name.split(/\s+/).slice(0, 2).map(word => Array.from(word)[0]).join('').toLocaleUpperCase('pt-BR');
  const details = document.createElement('span');
  details.textContent = name;
  const hint = document.createElement('small');
  hint.textContent = 'Exemplo temporário';
  details.append(hint);
  person.append(avatar, details);
  const group = document.createElement('td');
  group.textContent = $('#example-group').value;
  const status = document.createElement('td');
  const badge = document.createElement('span');
  const member = $('#example-member').checked;
  badge.className = `badge ${member ? 'neutral' : 'info'}`;
  badge.textContent = member ? 'Membro' : 'Visitante';
  status.append(badge);
  row.append(person, group, status);
  $('#people-body').append(row);
  $('#example-form').reset();
  $('#people-search').value = '';
  filterPeople();
  $('#form-status').textContent = 'Exemplo adicionado à tabela acima. Ele desaparece ao recarregar a página.';
  notice('Exemplo adicionado. Nenhum dado foi enviado.');
});
$('.switch').addEventListener('click', event => {
  const button = event.currentTarget;
  const enabled = button.getAttribute('aria-checked') !== 'true';
  button.setAttribute('aria-checked', String(enabled));
  $('#switch-state').textContent = `${enabled ? 'Ativados' : 'Desativados'} nesta demonstração`;
});
const tabs = [...document.querySelectorAll('[role=tab]')];
function selectTab(tab, focus = false) {
  tabs.forEach(item => {
    const selected = item === tab;
    item.setAttribute('aria-selected', String(selected));
    item.tabIndex = selected ? 0 : -1;
    document.getElementById(item.getAttribute('aria-controls')).hidden = !selected;
  });
  if (focus) tab.focus();
}
tabs.forEach((tab, index) => {
  tab.addEventListener('click', () => selectTab(tab));
  tab.addEventListener('keydown', event => {
    const key = event.key;
    if (!['ArrowLeft', 'ArrowRight', 'Home', 'End'].includes(key)) return;
    event.preventDefault();
    const next = key === 'Home' ? 0 : key === 'End' ? tabs.length - 1 : (index + (key === 'ArrowRight' ? 1 : -1) + tabs.length) % tabs.length;
    selectTab(tabs[next], true);
  });
});
const dialog = $('#delete-dialog');
$('#delete-example').addEventListener('click', () => dialog.showModal());
dialog.addEventListener('close', () => {
  if (dialog.returnValue === 'confirm') notice('Confirmação demonstrada. Nenhum registro foi excluído.');
});
const sections = [...document.querySelectorAll('main > section')];
const navLinks = [...document.querySelectorAll('.sidebar nav a')];
if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver(entries => {
    const entry = entries.find(item => item.isIntersecting);
    if (!entry) return;
    navLinks.forEach(link => {
      if (link.hash === `#${entry.target.id}`) link.setAttribute('aria-current', 'location');
      else link.removeAttribute('aria-current');
    });
  }, { rootMargin: '-12% 0px -65% 0px' });
  sections.forEach(section => observer.observe(section));
}

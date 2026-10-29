'use strict';

const langToggle = document.getElementById('langToggle');

langToggle.addEventListener('click', () => {
  const next = document.documentElement.lang === 'zh' ? 'en' : 'zh';
  document.documentElement.lang = next;
  langToggle.textContent = next === 'en' ? '中文' : 'EN';
  langToggle.lang = next === 'en' ? 'zh-CN' : 'en';
  langToggle.setAttribute('aria-label', next === 'en' ? 'Switch to Chinese' : '切换为英文');
});

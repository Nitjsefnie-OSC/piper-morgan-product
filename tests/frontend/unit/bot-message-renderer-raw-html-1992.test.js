/**
 * #1992 RAW-HTML-VISIBLE — renderBotMessage shows angle-bracket text.
 *
 * Alpha c613beabf5 (2026-10-12): 'say "set my timezone to <city>"' served as
 * 'say "set my timezone to "'. marked passed `<city>` through as raw inline
 * HTML and the #1732 DOMPurify step stripped the unknown tag. The renderer
 * now overrides marked's `html` renderer to entity-escape raw HTML, so it
 * renders as visible text; DOMPurify stays as the backstop.
 *
 * Layer: these tests drive the REAL vendored marked (15.0.12) and the REAL
 * vendored DOMPurify (3.2.7) through renderBotMessage in jsdom — the served
 * pipeline minus the browser. The legacy-renderer branch (marked without
 * `use`) is driven with a fake, since no vendored legacy marked exists.
 */

const fs = require('fs');
const path = require('path');

function loadRenderer(markedImpl, purify) {
  const code = fs.readFileSync(
    path.join(__dirname, '../../../web/assets/bot-message-renderer.js'),
    'utf8'
  );
  const wrapped = new Function('marked', 'DOMPurify', `${code}\nreturn { renderBotMessage };`);
  return wrapped(markedImpl, purify).renderBotMessage;
}

function realPurify() {
  let purify = require('../../../web/static/vendor/purify-3.2.7.min.js');
  if (!purify.sanitize && typeof purify === 'function') purify = purify(window);
  return purify;
}

function realMarked() {
  const m = require('../../../web/static/vendor/marked-15.0.12.min.js');
  return m.marked && typeof m.marked.use === 'function' ? m.marked : m;
}

function asElement(html) {
  const div = document.createElement('div');
  div.innerHTML = html;
  return div;
}

describe('#1992 — raw HTML in a bot reply renders as visible text (real marked + DOMPurify)', () => {
  let renderBotMessage;

  beforeEach(() => {
    renderBotMessage = loadRenderer(realMarked(), realPurify());
  });

  test('an inline <city> placeholder survives as text (the alpha incident)', () => {
    const html = renderBotMessage('or say "set my timezone to <city>".');
    expect(html).toContain('&lt;city&gt;');
    expect(html).not.toMatch(/<city>/);
    expect(asElement(html).textContent).toContain('set my timezone to <city>');
  });

  test('a quoted <title> survives as text', () => {
    const html = renderBotMessage('The page <title> is what the tab shows.');
    expect(asElement(html).textContent).toContain('The page <title> is what the tab shows.');
    expect(asElement(html).querySelector('title')).toBeNull();
  });

  test('block-level raw HTML at line start is shown, not parsed', () => {
    const html = renderBotMessage('<div>hello</div>');
    expect(asElement(html).textContent).toContain('<div>hello</div>');
    // the only div is the renderer's own wrapper
    expect(asElement(html).querySelectorAll('div').length).toBe(1);
  });

  test('a <script> in reply text is inert AND visible (security-neutral or better)', () => {
    const html = renderBotMessage('try <script>alert(1)</script> now');
    const el = asElement(html);
    expect(el.querySelector('script')).toBeNull();
    expect(html).not.toMatch(/<script/i);
    expect(el.textContent).toContain('<script>alert(1)</script>');
  });

  test('markdown and the #1123 link renderer are unaffected', () => {
    const html = renderBotMessage('**bold** and [Notion](https://notion.so/abc)');
    expect(html).toMatch(/<strong>bold<\/strong>/);
    expect(html).toMatch(/href="https:\/\/notion\.so\/abc"/);
    expect(html).toMatch(/target="_blank"/);
  });

  test('entities the user could type are not double-escaped into mojibake', () => {
    const html = renderBotMessage('5 &lt; 7');
    expect(asElement(html).textContent).toContain('5 < 7');
  });
});

describe('#1992 — legacy marked (no `use`) gets the same html override', () => {
  test('renderer.html entity-escapes the raw string it is given', () => {
    let captured = null;
    class Renderer {}
    const legacyMarked = {
      Renderer,
      setOptions: (opts) => {
        captured = opts.renderer;
      },
      parse: (text) => text,
    };
    const renderBotMessage = loadRenderer(legacyMarked, realPurify());
    renderBotMessage('anything');
    expect(captured).not.toBeNull();
    expect(typeof captured.html).toBe('function');
    expect(typeof captured.link).toBe('function');
    expect(captured.html('<city>')).toBe('&lt;city&gt;');
    expect(captured.html({ text: '<b>x</b>' })).toBe('&lt;b&gt;x&lt;/b&gt;');
  });
});

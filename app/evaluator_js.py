# JavaScript injection code for auto-filling evaluation forms

def get_evaluator_js(score):
    """Generate JavaScript code with the given score"""
    option_name = "完全同意"
    if score > 80:
        option_name = "完全同意"
    elif score > 60:
        option_name = "同意"
    elif score > 40:
        option_name = "一般"
    elif score > 20:
        option_name = "不太同意"
    else:
        option_name = "完全不同意"

    js = """(function() {
    'use strict';
    var SCORE = """ + str(score) + """;
    var OPTION = '""" + option_name + """';
    var lastFillTime = 0;
    var fillCount = 0;

    console.log('[AutoFill] Start, score=' + SCORE + ', option=' + OPTION);

    function sleep(ms) { return new Promise(function(r) { setTimeout(r, ms); }); }

    function fillRadios() {
        var groups = {};
        var labels = document.querySelectorAll('td label, .form-group label, label, span.radio label');
        for (var l = 0; l < labels.length; l++) {
            var inp = labels[l].querySelector('input[type="radio"]');
            if (!inp) continue;
            var name = inp.name;
            if (!name) continue;
            if (!groups[name]) groups[name] = { items: [] };
            var txt = (labels[l].textContent || '').trim().replace(/\\s+/g, '');
            groups[name].items.push({ text: txt, input: inp, label: labels[l] });
        }
        var filled = 0;
        for (var key in groups) {
            var g = groups[key];
            var skipped = false;
            for (var i = 0; i < g.items.length; i++) {
                if (g.items[i].input && g.items[i].input.checked) { skipped = true; break; }
            }
            if (skipped) continue;
            for (var i = 0; i < g.items.length; i++) {
                var item = g.items[i];
                if (item.text.indexOf(OPTION) !== -1) {
                    item.input.click(); item.input.checked = true;
                    item.input.dispatchEvent(new Event('change', {bubbles: true}));
                    item.input.dispatchEvent(new Event('click', {bubbles: true}));
                    if (item.label) item.label.click();
                    filled++; break;
                }
            }
        }
        return filled;
    }

    function fillInputs() {
        var inputs = document.querySelectorAll('input[type="text"], input[type="number"], input:not([type])');
        var filled = 0;
        for (var i = 0; i < inputs.length; i++) {
            var inp = inputs[i];
            if (inp.readOnly || inp.disabled) continue;
            var ph = (inp.placeholder || inp.title || '').toLowerCase();
            if (ph.indexOf('\u6253\u5206') !== -1 || ph.indexOf('\u8bc4\u5206') !== -1 || ph.indexOf('score') !== -1) {
                inp.value = String(SCORE);
                inp.dispatchEvent(new Event('input', {bubbles: true}));
                inp.dispatchEvent(new Event('change', {bubbles: true}));
                filled++;
            }
        }
        return filled;
    }

    function clickSubmit() {
        var btns = document.querySelectorAll('button, input[type="submit"], a.btn, a.button, input[type="button"]');
        for (var b = 0; b < btns.length; b++) {
            var txt = (btns[b].textContent || btns[b].value || '').trim();
            if (txt.indexOf('\u63d0\u4ea4') !== -1 || txt.indexOf('\u4fdd\u5b58') !== -1 || txt.indexOf('\u786e\u5b9a') !== -1) {
                btns[b].click(); return true;
            }
        }
        return false;
    }

    async function doFill() {
        fillCount++;
        var rf = fillRadios();
        var inf = fillInputs();
        console.log('[AutoFill] Done: radios=' + rf + ', inputs=' + inf);
        if (rf > 0 || inf > 0) {
            await sleep(1000);
            clickSubmit();
        }
    }

    var observer = new MutationObserver(function(mutations) {
        var now = Date.now();
        if (now - lastFillTime < 3000) return;
        var allLabels = document.querySelectorAll('label, td, .form-group');
        var hasEval = false;
        for (var l = 0; l < allLabels.length; l++) {
            var t = (allLabels[l].textContent || '').trim();
            if (t.indexOf('\u5b8c\u5168\u540c\u610f') !== -1 || t.indexOf('\u540c\u610f') !== -1 || t.indexOf('\u4e00\u822c') !== -1) {
                hasEval = true; break;
            }
        }
        if (!hasEval) return;
        lastFillTime = now;
        console.log('[AutoFill] New evaluation detected, filling...');
        doFill();
    });
    observer.observe(document.body, { childList: true, subtree: true });
    console.log('[AutoFill] Observer started');

    setTimeout(function() {
        console.log('[AutoFill] First fill...');
        doFill();
    }, 1500);
})();
"""
    return js

EXAMPLES = [
    "Most popular AI Agent frameworks in 2026",
    "Most commercially successful Agentic AI implementations in 2026",
    "Celebrities who don't like cheese",
]

HEADER_HTML = """
<div class="dr-header">
    <div class="dr-logo">
        <div class="dr-logo-mark">
            <span></span>
            <span></span>
            <span></span>
        </div>
    </div>

    <div class="dr-header-content">
        <div class="dr-eyebrow">AI RESEARCH ENGINE</div>
        <h1>Deep<span>/</span>Research</h1>
        <p>Multi-source web investigation powered by autonomous research agents</p>
    </div>

    <div class="dr-status">
        <div class="status-dot"></div>
        <span>READY</span>
    </div>
</div>
"""


CSS = """
/* =========================================================
   DEEP RESEARCH UI
   ========================================================= */

:root {
    --bg: #f5f6f8;
    --surface: #ffffff;
    --surface-alt: #f8f9fb;

    --text: #111318;
    --text-secondary: #4f5561;
    --muted: #7a808c;

    --border: #dfe2e7;
    --border-strong: #c9cdd4;

    --blue: #2563eb;
    --blue-dark: #1d4ed8;
    --blue-light: #eff6ff;

    --green: #16a34a;
    --green-light: #f0fdf4;

    --shadow-sm:
        0 1px 2px rgba(0, 0, 0, 0.04);

    --shadow:
        0 4px 18px rgba(0, 0, 0, 0.06);

    --shadow-lg:
        0 12px 40px rgba(0, 0, 0, 0.08);
}


/* =========================================================
   MAIN PAGE
   ========================================================= */

.gradio-container {
    max-width: 1180px !important;
    margin: 0 auto !important;

    padding: 28px 32px 70px !important;

    background: var(--bg) !important;
    color: var(--text) !important;

    font-family:
        Inter,
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        Helvetica,
        Arial,
        sans-serif !important;
}


/* Remove unnecessary Gradio backgrounds */

.gradio-container .block,
.gradio-container .form,
.gradio-container .wrap {
    background: transparent !important;
}


/* =========================================================
   HEADER
   ========================================================= */

.dr-header {
    display: flex;
    align-items: center;

    gap: 20px;

    padding: 24px 26px;

    margin-bottom: 28px;

    background: var(--surface);

    border: 1px solid var(--border);

    border-radius: 14px;

    box-shadow: var(--shadow-sm);
}


/* Logo */

.dr-logo {
    width: 52px;
    height: 52px;

    display: flex;
    align-items: center;
    justify-content: center;

    background: #111318;

    border-radius: 12px;

    flex-shrink: 0;
}

.dr-logo-mark {
    display: flex;
    flex-direction: column;

    gap: 4px;

    width: 25px;
}

.dr-logo-mark span {
    height: 4px;

    display: block;

    border-radius: 2px;
}

.dr-logo-mark span:nth-child(1) {
    width: 100%;
    background: #ffffff;
}

.dr-logo-mark span:nth-child(2) {
    width: 72%;
    background: #ffffff;
}

.dr-logo-mark span:nth-child(3) {
    width: 45%;
    background: #ffffff;
}


/* Header text */

.dr-header-content {
    flex: 1;
}

.dr-eyebrow {
    font-family:
        ui-monospace,
        SFMono-Regular,
        Menlo,
        monospace;

    font-size: 10px;

    font-weight: 700;

    letter-spacing: 0.18em;

    color: var(--blue);

    margin-bottom: 5px;
}

.dr-header h1 {
    margin: 0;

    font-size: clamp(2rem, 4vw, 2.7rem);

    line-height: 1;

    font-weight: 850;

    letter-spacing: -0.055em;

    color: var(--text);
}

.dr-header h1 span {
    color: var(--blue);

    font-weight: 400;

    margin: 0 2px;
}

.dr-header p {
    margin: 7px 0 0;

    font-size: 13px;

    color: var(--text-secondary);
}


/* Status */

.dr-status {
    display: flex;

    align-items: center;

    gap: 8px;

    padding: 8px 11px;

    border: 1px solid #d1fae5;

    background: var(--green-light);

    border-radius: 999px;

    font-family:
        ui-monospace,
        SFMono-Regular,
        Menlo,
        monospace;

    font-size: 10px;

    font-weight: 700;

    letter-spacing: 0.12em;

    color: #15803d;
}

.status-dot {
    width: 7px;
    height: 7px;

    border-radius: 50%;

    background: var(--green);

    box-shadow: 0 0 0 3px rgba(22, 163, 74, 0.12);
}


/* =========================================================
   QUERY AREA
   ========================================================= */

.dr-query-row {
    gap: 0 !important;

    align-items: stretch !important;

    margin-bottom: 0 !important;
}


/* Textbox container */

#dr-query,
#dr-query > div,
#dr-query .wrap,
#dr-query .form,
#dr-query .block {
    background: transparent !important;

    border: none !important;

    box-shadow: none !important;

    padding: 0 !important;
}


/* Textbox */

#dr-query textarea,
#dr-query input {
    min-height: 62px !important;

    padding: 17px 19px !important;

    background: var(--surface) !important;

    color: var(--text) !important;

    border: 1px solid var(--border-strong) !important;

    border-right: none !important;

    border-radius: 11px 0 0 11px !important;

    box-shadow: var(--shadow-sm) !important;

    font-size: 15px !important;

    line-height: 1.5 !important;

    font-family: inherit !important;

    resize: none !important;

    transition:
        border-color 0.15s ease,
        box-shadow 0.15s ease !important;
}

#dr-query textarea:hover,
#dr-query input:hover {
    border-color: #aeb4bd !important;
}

#dr-query textarea:focus,
#dr-query input:focus {
    outline: none !important;

    border-color: var(--blue) !important;

    box-shadow:
        0 0 0 3px rgba(37, 99, 235, 0.10) !important;
}

#dr-query textarea::placeholder,
#dr-query input::placeholder {
    color: var(--muted) !important;

    opacity: 1 !important;
}


/* =========================================================
   RUN BUTTON
   ========================================================= */

#dr-run {
    min-width: 155px !important;

    padding: 0 25px !important;

    background: var(--blue) !important;

    color: white !important;

    border: 1px solid var(--blue) !important;

    border-radius: 0 11px 11px 0 !important;

    font-size: 12px !important;

    font-weight: 800 !important;

    letter-spacing: 0.08em !important;

    text-transform: uppercase !important;

    box-shadow: var(--shadow-sm) !important;

    transition:
        background 0.15s ease,
        transform 0.1s ease !important;
}

#dr-run:hover {
    background: var(--blue-dark) !important;
}

#dr-run:active {
    transform: translateY(1px) !important;
}


/* =========================================================
   EXAMPLES
   ========================================================= */

.dr-examples-label {
    display: flex;

    align-items: center;

    gap: 12px;

    margin: 22px 0 10px;

    font-family:
        ui-monospace,
        SFMono-Regular,
        Menlo,
        monospace;

    font-size: 10px;

    font-weight: 700;

    letter-spacing: 0.15em;

    color: var(--muted);

    text-transform: uppercase;
}

.dr-examples-label::after {
    content: "";

    flex: 1;

    height: 1px;

    background: var(--border);
}


#dr-examples,
#dr-examples > div,
#dr-examples .wrap,
#dr-examples .block {
    background: transparent !important;

    border: none !important;

    padding: 0 !important;

    box-shadow: none !important;
}

#dr-examples label,
#dr-examples .label-wrap,
#dr-examples > div > .label-wrap {
    display: none !important;
}

#dr-examples table {
    width: 100% !important;

    border-collapse: separate !important;

    border-spacing: 7px !important;

    margin-left: -7px !important;
}

#dr-examples thead {
    display: none !important;
}

#dr-examples tbody {
    background: transparent !important;
}

#dr-examples tr {
    display: flex !important;

    flex-wrap: wrap !important;

    gap: 8px !important;

    background: transparent !important;
}

#dr-examples td,
#dr-examples button {
    padding: 9px 13px !important;

    background: var(--surface) !important;

    color: var(--text-secondary) !important;

    border: 1px solid var(--border) !important;

    border-radius: 8px !important;

    font-size: 12px !important;

    cursor: pointer !important;

    box-shadow: var(--shadow-sm) !important;

    transition:
        border-color 0.15s ease,
        color 0.15s ease,
        background 0.15s ease !important;
}

#dr-examples td:hover,
#dr-examples button:hover {
    background: var(--blue-light) !important;

    color: var(--blue) !important;

    border-color: #bfdbfe !important;
}


/* =========================================================
   REPORT CONTAINER
   ========================================================= */

#dr-report {
    margin-top: 34px !important;

    padding: 34px 38px !important;

    min-height: 100px;

    background: var(--surface) !important;

    color: var(--text) !important;

    border: 1px solid var(--border) !important;

    border-radius: 14px !important;

    box-shadow: var(--shadow) !important;

    line-height: 1.75 !important;
}

#dr-report > div,
#dr-report .prose {
    background: transparent !important;

    color: var(--text) !important;

    max-width: none !important;
}


/* =========================================================
   REPORT TITLE
   ========================================================= */

#dr-report h1 {
    margin:
        0 0 25px !important;

    padding:
        0 0 18px !important;

    color: var(--text) !important;

    font-size: 30px !important;

    line-height: 1.2 !important;

    font-weight: 850 !important;

    letter-spacing: -0.035em !important;

    border-bottom: 1px solid var(--border) !important;
}


/* =========================================================
   REPORT SECTIONS
   ========================================================= */

#dr-report h2 {
    margin:
        38px 0 14px !important;

    padding:
        0 0 9px !important;

    color: var(--text) !important;

    font-size: 20px !important;

    font-weight: 800 !important;

    line-height: 1.3 !important;

    letter-spacing: -0.025em !important;

    border-bottom: 1px solid var(--border) !important;

    position: relative;
}

#dr-report h2::before {
    content: "";

    display: inline-block;

    width: 4px;

    height: 18px;

    margin-right: 9px;

    vertical-align: -2px;

    background: var(--blue);

    border-radius: 3px;
}


#dr-report h3 {
    margin:
        28px 0 9px !important;

    color: #20242b !important;

    font-size: 16px !important;

    font-weight: 750 !important;

    line-height: 1.4 !important;
}


/* =========================================================
   PARAGRAPHS
   ========================================================= */

#dr-report p {
    margin:
        0 0 16px !important;

    color: var(--text-secondary) !important;

    font-size: 15px !important;

    line-height: 1.78 !important;
}


/* =========================================================
   LINKS / CITATIONS
   ========================================================= */

#dr-report a {
    color: var(--blue) !important;

    text-decoration: none !important;

    font-weight: 550;

    border-bottom: 1px solid rgba(37, 99, 235, 0.25);

    transition:
        color 0.15s ease,
        border-color 0.15s ease;
}

#dr-report a:hover {
    color: var(--blue-dark) !important;

    border-color: var(--blue);
}


/* =========================================================
   LISTS
   ========================================================= */

#dr-report ul,
#dr-report ol {
    margin:
        10px 0 20px !important;

    padding-left: 25px !important;
}

#dr-report li {
    margin:
        7px 0 !important;

    padding-left: 3px;

    color: var(--text-secondary) !important;

    font-size: 15px !important;

    line-height: 1.65 !important;
}

#dr-report li::marker {
    color: var(--blue);
}


/* =========================================================
   TABLES
   ========================================================= */

#dr-report table {
    width: 100% !important;

    margin:
        22px 0 28px !important;

    border-collapse: separate !important;

    border-spacing: 0 !important;

    overflow: hidden;

    background: var(--surface);

    border: 1px solid var(--border) !important;

    border-radius: 9px !important;
}

#dr-report th {
    padding: 12px 14px !important;

    background: var(--surface-alt) !important;

    color: var(--text) !important;

    border-bottom: 1px solid var(--border) !important;

    font-size: 12px !important;

    font-weight: 750 !important;

    text-transform: uppercase;

    letter-spacing: 0.04em;
}

#dr-report td {
    padding: 12px 14px !important;

    color: var(--text-secondary) !important;

    border-bottom: 1px solid var(--border) !important;

    font-size: 13px !important;

    vertical-align: top !important;
}

#dr-report tr:last-child td {
    border-bottom: none !important;
}

#dr-report tr:hover td {
    background: #fafbfc !important;
}


/* =========================================================
   CODE
   ========================================================= */

#dr-report code {
    padding:
        2px 6px !important;

    background: #f1f3f5 !important;

    color: #374151 !important;

    border: 1px solid #e5e7eb !important;

    border-radius: 5px !important;

    font-size: 0.88em !important;

    font-family:
        ui-monospace,
        SFMono-Regular,
        Menlo,
        monospace !important;
}


#dr-report pre {
    margin:
        20px 0 !important;

    padding:
        18px 20px !important;

    overflow-x: auto !important;

    background: #111318 !important;

    color: #f5f5f5 !important;

    border: none !important;

    border-radius: 9px !important;

    box-shadow: var(--shadow-sm) !important;
}

#dr-report pre code {
    padding: 0 !important;

    background: transparent !important;

    color: inherit !important;

    border: none !important;
}


/* =========================================================
   BLOCKQUOTE
   ========================================================= */

#dr-report blockquote {
    margin:
        20px 0 !important;

    padding:
        16px 20px !important;

    background: var(--blue-light) !important;

    color: var(--text-secondary) !important;

    border-left: 4px solid var(--blue) !important;

    border-radius: 0 8px 8px 0 !important;
}


/* =========================================================
   HORIZONTAL RULE
   ========================================================= */

#dr-report hr {
    margin:
        32px 0 !important;

    border: none !important;

    border-top: 1px solid var(--border) !important;
}


/* =========================================================
   STRONG TEXT
   ========================================================= */

#dr-report strong {
    color: var(--text) !important;

    font-weight: 750 !important;
}


/* =========================================================
   DARK MODE
   ========================================================= */

.gradio-container.dark,
.dark .gradio-container,
body.dark .gradio-container,
html.dark .gradio-container {

    --bg: #0d0f12;

    --surface: #15181d;

    --surface-alt: #1b1f25;

    --text: #f1f3f5;

    --text-secondary: #b5bac3;

    --muted: #858b96;

    --border: #2b3038;

    --border-strong: #3a414c;

    --blue: #60a5fa;

    --blue-dark: #3b82f6;

    --blue-light: #172554;
}


.dark #dr-report h3 {
    color: var(--text) !important;
}

.dark #dr-report code {
    background: #1e232a !important;

    color: #d1d5db !important;

    border-color: #303640 !important;
}

.dark #dr-report tr:hover td {
    background: #1a1e24 !important;
}


/* =========================================================
   MOBILE
   ========================================================= */

@media (max-width: 700px) {

    .gradio-container {
        padding:
            16px 12px 45px !important;
    }

    .dr-header {
        padding: 18px;

        gap: 14px;

        border-radius: 11px;
    }

    .dr-logo {
        width: 43px;
        height: 43px;
    }

    .dr-header h1 {
        font-size: 1.8rem;
    }

    .dr-header p {
        font-size: 11px;
    }

    .dr-status {
        display: none;
    }

    .dr-query-row {
        flex-direction: column !important;
    }

    #dr-query textarea,
    #dr-query input {
        border-right: 1px solid var(--border-strong) !important;

        border-radius: 10px 10px 0 0 !important;
    }

    #dr-run {
        width: 100% !important;

        min-height: 54px !important;

        border-radius: 0 0 10px 10px !important;
    }

    #dr-report {
        padding: 22px 18px !important;

        border-radius: 11px !important;
    }

    #dr-report h1 {
        font-size: 24px !important;
    }

    #dr-report h2 {
        font-size: 18px !important;
    }

    #dr-report p,
    #dr-report li {
        font-size: 14px !important;
    }

    #dr-report table {
        display: block !important;

        overflow-x: auto !important;
    }
}


/* =========================================================
   HIDE GRADIO FOOTER
   ========================================================= */

footer {
    display: none !important;
}
"""


JS = """
() => {
    const focus = () => {
        const el = document.querySelector(
            "#dr-query textarea, #dr-query input"
        );

        if (el) {
            el.focus();
            return true;
        }

        return false;
    };

    if (!focus()) {
        let tries = 0;

        const interval = setInterval(() => {
            if (focus() || ++tries > 20) {
                clearInterval(interval);
            }
        }, 100);
    }
}
"""
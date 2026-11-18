// Rajasthani Language Library - Client-Side App
document.addEventListener("DOMContentLoaded", () => {
  // Tab Switching
  const tabBtns = document.querySelectorAll(".tab-btn");
  const tabContents = document.querySelectorAll(".tab-content");

  tabBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      tabBtns.forEach(b => b.classList.remove("active"));
      tabContents.forEach(c => c.classList.remove("active"));

      btn.classList.add("active");
      const targetId = btn.getAttribute("data-tab");
      document.getElementById(targetId).classList.add("active");
    });
  });

  // 1. Translation Handler
  const btnTranslate = document.getElementById("btn-translate");
  const srcText = document.getElementById("src-text");
  const dialectSelect = document.getElementById("dialect-select");
  const transOutput = document.getElementById("trans-output");

  async function handleTranslate() {
    const text = srcText.value.trim();
    if (!text) return;
    const dialect = dialectSelect.value;

    try {
      const res = await fetch(`/api/translate?text=${encodeURIComponent(text)}&dialect=${dialect}`);
      const data = await res.json();
      transOutput.innerHTML = `
        <div class="res-raj">${data.rajasthani}</div>
        <div class="res-roman">${data.romanized}</div>
        <div class="res-details">बोली: ${data.dialect} | माध्यम: ${data.method}</div>
      `;
    } catch (err) {
      console.error(err);
    }
  }

  btnTranslate.addEventListener("click", handleTranslate);
  srcText.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleTranslate();
    }
  });

  // 2. Verb Conjugation Handler
  const btnConjugate = document.getElementById("btn-conjugate");
  const verbInput = document.getElementById("verb-input");
  const tenseSelect = document.getElementById("tense-select");
  const personSelect = document.getElementById("person-select");
  const genderSelect = document.getElementById("gender-select");
  const numberSelect = document.getElementById("number-select");
  const conjugateResult = document.getElementById("conjugate-result");

  btnConjugate.addEventListener("click", async () => {
    const verb = verbInput.value.trim();
    if (!verb) return;
    const tense = tenseSelect.value;
    const person = personSelect.value;
    const gender = genderSelect.value;
    const number = numberSelect.value;

    try {
      const url = `/api/conjugate?verb=${encodeURIComponent(verb)}&tense=${tense}&person=${person}&gender=${gender}&number=${number}`;
      const res = await fetch(url);
      const data = await res.json();
      conjugateResult.innerHTML = `
        <div class="res-raj">${data.conjugated}</div>
        <div class="res-details">मूल क्रिया: ${data.verb} | काल: ${data.tense}</div>
      `;
    } catch (err) {
      console.error(err);
    }
  });

  // 3. Dictionary Search Handler
  const btnSearchDict = document.getElementById("btn-search-dict");
  const dictSearch = document.getElementById("dict-search");
  const dictResults = document.getElementById("dict-results");

  async function handleDictSearch() {
    const q = dictSearch.value.trim();
    try {
      const res = await fetch(`/api/dictionary?q=${encodeURIComponent(q)}`);
      const data = await res.json();
      if (!data.results || data.results.length === 0) {
        dictResults.innerHTML = `<p class="text-muted">कोई शब्द कोनी मिल्यो (No words found).</p>`;
        return;
      }
      dictResults.innerHTML = data.results.map(w => `
        <div class="dict-card">
          <div>
            <span class="dict-raj">${w.rajasthani}</span>
            <span class="dict-pos">${w.pos}</span>
          </div>
          <div class="res-roman">${w.roman}</div>
          <div class="dict-trans"><strong>हिन्दी:</strong> ${w.hindi}</div>
          <div class="dict-trans"><strong>English:</strong> ${w.english}</div>
          ${w.example ? `<div class="dict-ex">"${w.example}"</div>` : ""}
        </div>
      `).join("");
    } catch (err) {
      console.error(err);
    }
  }

  btnSearchDict.addEventListener("click", handleDictSearch);
  dictSearch.addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
      handleDictSearch();
    }
  });

  // Initial dictionary load
  handleDictSearch();

  // 4. Numbers Converter Handler
  const btnConvertNum = document.getElementById("btn-convert-num");
  const numInput = document.getElementById("num-input");
  const numResult = document.getElementById("num-result");

  // 5. Rituals & Ornaments Handler
  const ritualFilter = document.getElementById("ritual-filter");
  const ritualsGrid = document.getElementById("rituals-grid");
  const ornamentFilter = document.getElementById("ornament-filter");
  const ornamentsGrid = document.getElementById("ornaments-grid");

  async function loadRituals() {
    if (!ritualsGrid) return;
    const cat = ritualFilter ? ritualFilter.value : "all";
    const url = cat && cat !== "all" ? `/api/rituals?category=${cat}` : "/api/rituals";
    try {
      const res = await fetch(url);
      const data = await res.json();
      ritualsGrid.innerHTML = data.rituals.map(r => `
        <div class="culture-card">
          <h3>${r.name}</h3>
          <p class="res-roman"><em>${r.roman}</em></p>
          <p><strong>विवरण:</strong> ${r.description}</p>
          <p><strong>रीत-रिवाज:</strong> ${r.customs_and_practices}</p>
          <p><strong>सांस्कृतिक महत्व:</strong> ${r.cultural_significance}</p>
        </div>
      `).join("");
    } catch (e) {
      console.error(e);
    }
  }

  async function loadOrnaments() {
    if (!ornamentsGrid) return;
    const part = ornamentFilter ? ornamentFilter.value : "all";
    const url = part && part !== "all" ? `/api/ornaments?part=${part}` : "/api/ornaments";
    try {
      const res = await fetch(url);
      const data = await res.json();
      ornamentsGrid.innerHTML = data.ornaments.map(o => `
        <div class="culture-card">
          <h3>${o.name}</h3>
          <p class="res-roman"><em>${o.roman}</em></p>
          <p><strong>अंग:</strong> ${o.body_part} | <strong>धातु:</strong> ${o.metal}</p>
          <p>${o.description}</p>
          <p class="text-muted"><em>${o.cultural_context}</em></p>
        </div>
      `).join("");
    } catch (e) {
      console.error(e);
    }
  }

  if (ritualFilter) ritualFilter.addEventListener("change", loadRituals);
  if (ornamentFilter) ornamentFilter.addEventListener("change", loadOrnaments);
  loadRituals();
  loadOrnaments();

  // 6. Corpus Catalog Handler
  const corpusGrid = document.getElementById("corpus-grid");
  async function loadCorpus() {
    if (!corpusGrid) return;
    try {
      const res = await fetch("/api/corpus");
      const data = await res.json();
      corpusGrid.innerHTML = data.books.map(b => `
        <div class="culture-card">
          <h3>${b.title}</h3>
          <p><strong>लेखक/संपादक:</strong> ${b.author} (${b.year || 'N/A'})</p>
          <p><strong>श्रेणी:</strong> ${b.category}</p>
          <p class="text-muted"><small>फ़ाइल: ${b.local_name} | Archive: ${b.archive_id}</small></p>
        </div>
      `).join("");
    } catch (e) {
      console.error(e);
    }
  }
  // 7. Idioms Loader
  const idiomsGrid = document.getElementById("idioms-grid");
  async function loadIdioms() {
    if (!idiomsGrid) return;
    try {
      const res = await fetch("/api/idioms");
      const data = await res.json();
      idiomsGrid.innerHTML = data.idioms.map(i => `
        <div class="culture-card">
          <h3>${i.rajasthani}</h3>
          <p class="res-roman"><em>${i.roman}</em></p>
          <p><strong>अर्थ:</strong> ${i.hindi}</p>
          <p><strong>English:</strong> ${i.english}</p>
          <p class="text-muted"><small>संदर्भ: ${i.cultural_context}</small></p>
          ${i.example ? `<p class="dict-ex mt-2">उदा.: "${i.example}"</p>` : ""}
        </div>
      `).join("");
    } catch (e) {
      console.error(e);
    }
  }
  loadIdioms();
});

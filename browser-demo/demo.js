(function () {
  const universe = window.AXIS_COSMOS_UNIVERSE;
  if (!universe) return;

  const canvas = document.getElementById("universe");
  const ctx = canvas.getContext("2d");
  const modeEl = document.getElementById("mode");
  const densityEl = document.getElementById("density");
  const searchEl = document.getElementById("search");
  const resetEl = document.getElementById("reset");
  const pauseEl = document.getElementById("pause");
  const settleEl = document.getElementById("settle");
  const reheatEl = document.getElementById("reheat");
  const clearEl = document.getElementById("clear");
  const focusEl = document.getElementById("focus");
  const panelToggleEl = document.getElementById("panel-toggle");
  const autosettleEl = document.getElementById("autosettle");
  const energyEl = document.getElementById("energy");
  const statsEl = document.getElementById("stats");
  const detailEl = document.getElementById("detail");
  const pathsEl = document.getElementById("paths");
  const sidePanelEl = document.getElementById("side-panel");

  const fullPdpnNodes = universe.pdpnGraph.nodes.map((n) => ({ ...n }));
  const fullPdpnEdges = universe.pdpnGraph.edges.map((e) => ({ ...e }));
  const conceptNodes = universe.conceptGraph.nodes.map((n) => ({ ...n, label: n.label || n.id }));
  const conceptEdges = universe.conceptGraph.edges.map((e) => ({ ...e }));

  const state = {
    mode: "pdpn",
    density: "260",
    search: "",
    selected: null,
    hover: null,
    dragNode: null,
    panX: 0,
    panY: 0,
    zoom: 1,
    panning: false,
    lastSX: 0,
    lastSY: 0,
    paused: false,
    autoSettle: true,
    nodes: [],
    edges: [],
    alpha: 0.95,
    alphaDecay: 0.007,
    alphaMin: 0.03,
    velocityDamp: 0.86,
    maxVelocity: 4.8,
    maxStep: 6.5,
    settleCounter: 0
  };

  function clamp(v, lo, hi) {
    return Math.max(lo, Math.min(hi, v));
  }

  function resizeCanvasToDisplaySize() {
    const dpr = Math.max(1, window.devicePixelRatio || 1);
    const rect = canvas.getBoundingClientRect();
    const width = Math.max(2, Math.round(rect.width * dpr));
    const height = Math.max(2, Math.round(rect.height * dpr));
    if (canvas.width !== width || canvas.height !== height) {
      canvas.width = width;
      canvas.height = height;
    }
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }

  function centerPan() {
    const rect = canvas.getBoundingClientRect();
    state.panX = rect.width / 2;
    state.panY = rect.height / 2;
  }

  function deterministicPoint(i, groupIndex, groupCount) {
    const bucket = groupCount ? groupIndex % groupCount : 0;
    const ring = 68 + Math.sqrt(i + 1) * 20;
    const base = (bucket / Math.max(1, groupCount)) * Math.PI * 2;
    const jitter = ((i * 0.6180339887) % 1) * 0.85;
    const a = base + jitter + i * 0.045;
    return { x: Math.cos(a) * ring, y: Math.sin(a) * ring };
  }

  function resetLayout(nodes) {
    const groups = [...new Set(nodes.map((n) => (state.mode === "pdpn" ? String(n.id || "").split(".")[0] : (n.cluster || "CONCEPT"))))];
    const gmap = new Map(groups.map((g, i) => [g, i]));
    nodes.forEach((n, i) => {
      const g = state.mode === "pdpn" ? String(n.id || "").split(".")[0] : (n.cluster || "CONCEPT");
      const p = deterministicPoint(i, gmap.get(g), groups.length);
      n.x = p.x;
      n.y = p.y;
      n.vx = 0;
      n.vy = 0;
      n.fx = null;
      n.fy = null;
    });
  }

  function colorFor(node) {
    if (state.mode === "concept") return "#34d399";
    const p = String(node.id || "").split(".")[0] || "XX";
    let h = 0;
    for (let i = 0; i < p.length; i += 1) h = (h * 31 + p.charCodeAt(i)) % 360;
    return `hsl(${h} 70% 60%)`;
  }

  function nodeWeight(node) {
    const pr = Number(node.pagerank || node.gravity || 0);
    if (pr > 0) return pr;
    const deg = Number(node.inDegree || 0) + Number(node.outDegree || 0);
    if (deg > 0) return deg / 1000;
    return 1 / ((node.rank || 50) + 1);
  }

  function nodeRadius(node) {
    const w = nodeWeight(node);
    const r = state.mode === "concept" ? 4 + Math.sqrt(w) * 2.5 : 2.6 + Math.sqrt(w) * 90;
    return Math.max(2.5, Math.min(r, state.mode === "concept" ? 12 : 14));
  }

  function filteredNodesAndEdges() {
    let nodes;
    let edges;
    if (state.mode === "concept") {
      nodes = conceptNodes.map((n) => ({ ...n }));
      edges = conceptEdges.map((e) => ({ ...e }));
    } else {
      const n = state.density === "all" ? fullPdpnNodes.length : Number(state.density);
      nodes = fullPdpnNodes.slice(0, n).map((x) => ({ ...x }));
      const keep = new Set(nodes.map((k) => k.id));
      edges = fullPdpnEdges.filter((e) => keep.has(e.source) && keep.has(e.target)).map((e) => ({ ...e }));
    }
    return { nodes, edges };
  }

  function reheat(alpha) {
    state.alpha = Math.max(state.alpha, alpha || 0.55);
    state.settleCounter = 0;
    state.paused = false;
    pauseEl.textContent = "Pause Physics";
    pauseEl.dataset.paused = "false";
  }

  function rebuildGraph() {
    const data = filteredNodesAndEdges();
    state.nodes = data.nodes;
    state.edges = data.edges;
    const byId = new Map(state.nodes.map((n) => [n.id, n]));
    state.edges = state.edges.filter((e) => byId.has(e.source) && byId.has(e.target));
    resetLayout(state.nodes);
    state.selected = null;
    state.hover = null;
    state.zoom = 1;
    centerPan();
    reheat(0.95);
    updateStats();
    draw();
  }

  function worldToScreen(node) {
    return { x: node.x * state.zoom + state.panX, y: node.y * state.zoom + state.panY };
  }

  function screenToWorld(screenX, screenY) {
    return { x: (screenX - state.panX) / state.zoom, y: (screenY - state.panY) / state.zoom };
  }

  function eventToScreen(evt) {
    const rect = canvas.getBoundingClientRect();
    return { x: evt.clientX - rect.left, y: evt.clientY - rect.top };
  }

  function searchMatch(n) {
    if (!state.search) return true;
    const q = state.search.toLowerCase();
    return String(n.id || "").toLowerCase().includes(q) || String(n.label || "").toLowerCase().includes(q);
  }

  function neighborSet(id) {
    const set = new Set([id]);
    for (const e of state.edges) {
      if (e.source === id) set.add(e.target);
      if (e.target === id) set.add(e.source);
    }
    return set;
  }

  function visibleNode(screenPt, margin) {
    return screenPt.x >= -margin && screenPt.y >= -margin && screenPt.x <= canvas.clientWidth + margin && screenPt.y <= canvas.clientHeight + margin;
  }

  function hitRadiusPx(node) {
    const visual = nodeRadius(node) * state.zoom;
    return clamp(Math.max(visual + 5, 12), 12, 26);
  }

  function findNearestNode(screenX, screenY) {
    let best = null;
    let bestD2 = Infinity;
    for (const n of state.nodes) {
      const p = worldToScreen(n);
      if (!visibleNode(p, 30)) continue;
      const dx = screenX - p.x;
      const dy = screenY - p.y;
      const d2 = dx * dx + dy * dy;
      const hr = hitRadiusPx(n);
      if (d2 <= hr * hr && d2 < bestD2) {
        best = n;
        bestD2 = d2;
      }
    }
    return best;
  }

  function draw() {
    resizeCanvasToDisplaySize();
    ctx.clearRect(0, 0, canvas.clientWidth, canvas.clientHeight);
    const active = state.hover || state.selected;
    const neigh = active ? neighborSet(active.id) : null;
    const byId = new Map(state.nodes.map((n) => [n.id, n]));

    for (const e of state.edges) {
      const s = byId.get(e.source);
      const t = byId.get(e.target);
      if (!s || !t) continue;
      const a = worldToScreen(s);
      const b = worldToScreen(t);
      if (!visibleNode(a, 16) && !visibleNode(b, 16)) continue;
      const highlight = active && (e.source === active.id || e.target === active.id);
      ctx.strokeStyle = highlight ? "rgba(147,197,253,0.80)" : "rgba(148,163,184,0.10)";
      ctx.lineWidth = highlight ? 1.8 : 1;
      ctx.beginPath();
      ctx.moveTo(a.x, a.y);
      ctx.lineTo(b.x, b.y);
      ctx.stroke();
    }

    for (const n of state.nodes) {
      const p = worldToScreen(n);
      if (!visibleNode(p, 24)) continue;
      const r = nodeRadius(n);
      const selected = state.selected && state.selected.id === n.id;
      const hover = state.hover && state.hover.id === n.id;
      const faded = !searchMatch(n) || (neigh && !neigh.has(n.id));
      ctx.globalAlpha = faded ? 0.2 : 1;
      ctx.fillStyle = colorFor(n);
      ctx.beginPath();
      ctx.arc(p.x, p.y, r * state.zoom, 0, Math.PI * 2);
      ctx.fill();

      if (hover || selected) {
        const ring = hover ? 4 : 3;
        ctx.globalAlpha = 1;
        ctx.strokeStyle = hover ? "#f8fafc" : "#93c5fd";
        ctx.lineWidth = hover ? 2.6 : 2.2;
        ctx.beginPath();
        ctx.arc(p.x, p.y, r * state.zoom + ring, 0, Math.PI * 2);
        ctx.stroke();
      }

      const showLabel = hover || selected || n.rank <= 10;
      if (showLabel) {
        ctx.globalAlpha = 0.95;
        ctx.fillStyle = "#e2e8f0";
        ctx.font = "12px Arial";
        ctx.fillText(n.label || n.id, p.x + (r * state.zoom) + 6, p.y + 3);
      }
      ctx.globalAlpha = 1;
    }

    canvas.classList.toggle("dragging", !!state.dragNode || state.panning);
    canvas.style.cursor = state.dragNode || state.panning ? "grabbing" : (state.hover ? "pointer" : "grab");
  }

  function physicsStep() {
    if (state.paused || state.alpha <= state.alphaMin) return;
    const nodes = state.nodes;
    const edges = state.edges;
    const n = nodes.length;
    const alpha = state.alpha;
    const repulsion = (n > 350 ? 1250 : 1800) * alpha;
    const spring = (n > 350 ? 0.0058 : 0.0078) * alpha;
    const center = (n > 350 ? 0.0011 : 0.0014) * alpha;
    const damp = state.velocityDamp;
    const maxPairs = n > 500 ? 42000 : n > 350 ? 65000 : Infinity;
    let pairCount = 0;

    for (let i = 0; i < n; i += 1) {
      const a = nodes[i];
      for (let j = i + 1; j < n; j += 1) {
        pairCount += 1;
        if (pairCount > maxPairs) break;
        const b = nodes[j];
        let dx = b.x - a.x;
        let dy = b.y - a.y;
        let d2 = dx * dx + dy * dy;
        if (d2 < 6) d2 = 6;
        const d = Math.sqrt(d2);
        let f = repulsion / d2;
        f = clamp(f, 0, 0.75);
        dx /= d;
        dy /= d;
        a.vx -= dx * f;
        a.vy -= dy * f;
        b.vx += dx * f;
        b.vy += dy * f;
      }
      if (pairCount > maxPairs) break;
    }

    const byId = new Map(nodes.map((x) => [x.id, x]));
    const edgeLimit = n > 500 ? 5200 : edges.length;
    for (let k = 0; k < edgeLimit; k += 1) {
      const e = edges[k];
      const s = byId.get(e.source);
      const t = byId.get(e.target);
      if (!s || !t) continue;
      const dx = t.x - s.x;
      const dy = t.y - s.y;
      const d = Math.sqrt(dx * dx + dy * dy) + 0.001;
      const targetLen = state.mode === "concept" ? 88 : 54;
      let f = (d - targetLen) * spring;
      f = clamp(f, -0.85, 0.85);
      const ux = dx / d;
      const uy = dy / d;
      s.vx += ux * f;
      s.vy += uy * f;
      t.vx -= ux * f;
      t.vy -= uy * f;
    }

    let kinetic = 0;
    for (const nd of nodes) {
      nd.vx += -nd.x * center;
      nd.vy += -nd.y * center;
      if (nd.fx !== null && nd.fx !== undefined) {
        nd.x = nd.fx;
        nd.y = nd.fy;
        nd.vx *= 0.55;
        nd.vy *= 0.55;
      } else {
        nd.vx *= damp;
        nd.vy *= damp;
        nd.vx = clamp(nd.vx, -state.maxVelocity, state.maxVelocity);
        nd.vy = clamp(nd.vy, -state.maxVelocity, state.maxVelocity);
        const stepX = clamp(nd.vx, -state.maxStep, state.maxStep);
        const stepY = clamp(nd.vy, -state.maxStep, state.maxStep);
        nd.x += stepX;
        nd.y += stepY;
      }
      kinetic += Math.abs(nd.vx) + Math.abs(nd.vy);
    }

    state.alpha *= (1 - state.alphaDecay);
    if (kinetic < n * 0.016) state.settleCounter += 1;
    else state.settleCounter = 0;

    if (state.autoSettle && (state.alpha <= state.alphaMin || state.settleCounter > 24)) {
      state.paused = true;
      pauseEl.textContent = "Resume Physics";
      pauseEl.dataset.paused = "true";
    }
  }

  function tick() {
    physicsStep();
    draw();
    energyEl.textContent = "alpha: " + state.alpha.toFixed(3) + (state.paused ? " (paused)" : "");
    requestAnimationFrame(tick);
  }

  function connectedCount(id) {
    let c = 0;
    for (const e of state.edges) if (e.source === id || e.target === id) c += 1;
    return c;
  }

  function showDetail(node) {
    if (!node) {
      detailEl.textContent = "Click a node to inspect details.";
      return;
    }
    detailEl.innerHTML = [
      "<strong>" + node.id + "</strong>",
      "Label: " + (node.label || node.id),
      "Rank: " + (node.rank || "n/a"),
      "PageRank/Gravity: " + Number(node.pagerank || node.gravity || 0).toFixed(6),
      "In/Out Degree: " + (node.inDegree || 0) + " / " + (node.outDegree || 0),
      "Connected edges: " + connectedCount(node.id),
      "Source type: " + (state.mode === "pdpn" ? "PD#PN archaeology graph" : "concept sample graph")
    ].join("<br>");
  }

  function updateStats() {
    const s = universe.summary;
    statsEl.innerHTML = "";
    const lines = [
      "Mode: " + (state.mode === "pdpn" ? "PD#PN Graph" : "Concept Sample"),
      "Render mode: " + (state.mode === "pdpn" ? (state.density === "all" ? "Full graph experimental" : "Top " + state.density) : "Concept full sample"),
      "Rendered nodes: " + state.nodes.length,
      "Rendered edges: " + state.edges.length,
      "Full PD#PN nodes: " + s.fullPdpnNodeCount,
      "Full PD#PN edges: " + s.fullPdpnEdgeCount,
      "Metric rows: " + s.metricRows,
      "Concept nodes: " + s.conceptNodeCount,
      "Concept edges: " + s.conceptEdgeCount,
      "Paths: " + s.pathCount,
      "Auto-settle: " + (state.autoSettle ? "on" : "off")
    ];
    for (const t of lines) {
      const li = document.createElement("li");
      li.textContent = t;
      statsEl.appendChild(li);
    }
  }

  function renderPaths() {
    pathsEl.innerHTML = "";
    for (const p of universe.conceptGraph.paths.slice(0, 6)) {
      const li = document.createElement("li");
      li.textContent = p.path_id + ": " + (p.sequence || []).join(" -> ");
      pathsEl.appendChild(li);
    }
  }

  canvas.addEventListener("mousedown", (e) => {
    const s = eventToScreen(e);
    const hit = state.hover || findNearestNode(s.x, s.y);
    if (hit) {
      state.dragNode = hit;
      const w = screenToWorld(s.x, s.y);
      hit.fx = w.x;
      hit.fy = w.y;
      state.selected = hit;
      showDetail(hit);
      reheat(0.45);
    } else {
      state.panning = true;
      state.lastSX = s.x;
      state.lastSY = s.y;
    }
  });

  canvas.addEventListener("mousemove", (e) => {
    const s = eventToScreen(e);
    if (state.dragNode) {
      const w = screenToWorld(s.x, s.y);
      state.dragNode.fx = w.x;
      state.dragNode.fy = w.y;
      return;
    }
    if (state.panning) {
      state.panX += s.x - state.lastSX;
      state.panY += s.y - state.lastSY;
      state.lastSX = s.x;
      state.lastSY = s.y;
      return;
    }
    state.hover = findNearestNode(s.x, s.y);
  });

  canvas.addEventListener("mouseup", () => {
    if (state.dragNode) {
      state.dragNode.fx = null;
      state.dragNode.fy = null;
      state.dragNode = null;
      reheat(0.22);
    }
    state.panning = false;
  });

  canvas.addEventListener("mouseleave", () => {
    state.hover = null;
    state.panning = false;
    if (state.dragNode) {
      state.dragNode.fx = null;
      state.dragNode.fy = null;
      state.dragNode = null;
      reheat(0.2);
    }
  });

  canvas.addEventListener("wheel", (e) => {
    e.preventDefault();
    const s = eventToScreen(e);
    const wBefore = screenToWorld(s.x, s.y);
    const factor = e.deltaY < 0 ? 1.1 : 0.9;
    state.zoom = Math.max(0.2, Math.min(4, state.zoom * factor));
    const sAfter = { x: wBefore.x * state.zoom + state.panX, y: wBefore.y * state.zoom + state.panY };
    state.panX += s.x - sAfter.x;
    state.panY += s.y - sAfter.y;
  }, { passive: false });

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") {
      state.selected = null;
      showDetail(null);
    }
  });

  modeEl.addEventListener("change", () => {
    state.mode = modeEl.value;
    densityEl.disabled = state.mode !== "pdpn";
    rebuildGraph();
    showDetail(null);
  });

  densityEl.addEventListener("change", () => {
    state.density = densityEl.value;
    rebuildGraph();
  });

  searchEl.addEventListener("input", () => {
    state.search = searchEl.value.trim();
    if (!state.search) return;
    const q = state.search.toLowerCase();
    const hit = state.nodes.find((n) => String(n.id).toLowerCase().includes(q) || String(n.label || "").toLowerCase().includes(q));
    if (hit) {
      state.selected = hit;
      showDetail(hit);
      const rect = canvas.getBoundingClientRect();
      state.panX = rect.width / 2 - hit.x * state.zoom;
      state.panY = rect.height / 2 - hit.y * state.zoom;
      reheat(0.2);
    }
  });

  resetEl.addEventListener("click", () => {
    state.zoom = 1;
    centerPan();
    resetLayout(state.nodes);
    reheat(0.95);
  });

  pauseEl.addEventListener("click", () => {
    state.paused = !state.paused;
    pauseEl.textContent = state.paused ? "Resume Physics" : "Pause Physics";
    pauseEl.dataset.paused = state.paused ? "true" : "false";
    if (!state.paused) reheat(0.18);
  });

  settleEl.addEventListener("click", () => {
    state.alpha = 0.01;
    state.paused = true;
    pauseEl.textContent = "Resume Physics";
    pauseEl.dataset.paused = "true";
  });

  reheatEl.addEventListener("click", () => reheat(0.62));

  clearEl.addEventListener("click", () => {
    state.selected = null;
    state.hover = null;
    showDetail(null);
  });

  focusEl.addEventListener("click", () => {
    centerPan();
    state.zoom = 1;
  });

  panelToggleEl.addEventListener("click", () => {
    sidePanelEl.classList.toggle("hidden");
    panelToggleEl.textContent = sidePanelEl.classList.contains("hidden") ? "Show Panel" : "Hide Panel";
  });

  autosettleEl.addEventListener("change", () => {
    state.autoSettle = autosettleEl.checked;
    updateStats();
  });

  window.addEventListener("resize", () => {
    resizeCanvasToDisplaySize();
    draw();
  });

  renderPaths();
  rebuildGraph();
  showDetail(null);
  resizeCanvasToDisplaySize();
  requestAnimationFrame(tick);
})();

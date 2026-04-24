## 📄 FRONTEND_GUIDELINES.md — EcoRouter

**Style Direction:** Minimal & Modern  
**Brand Colors:** "Eco-Growth" Green & "Deep Tech" Charcoal  
**Target Audience:** Tech-savvy students and developers who value efficiency and sustainability.

---

### 🏛️ 1. Design Principles
1.  **Efficiency First:** UI should never distract from the prompt. Information density should be low until results are generated.
2.  **Eco-Visuals:** Use greens and soft neutrals to reinforce the environmental mission.
3.  **Performance Transparency:** The routing decision (Local vs. Cloud) and the ESIF score must be the most prominent post-action elements.
4.  **Clarity over Decoration:** Avoid unnecessary shadows or gradients. Use flat, clean surfaces.

---

### 🎨 2. Design Tokens (Tailwind Compatible)

#### **Color Palette**
| Level | Primary (Eco Green) | Neutral (Slate) | Semantic |
| :--- | :--- | :--- | :--- |
| **50** | `#F0FDF4` | `#F8FAFC` | **Success:** `#22C55E` |
| **500** | `#22C55E` | `#64748B` | **Warning:** `#F59E0B` |
| **900** | `#14532D` | `#0F172A` | **Danger:** `#EF4444` |

#### **Typography**
* **Font Family:** Inter (Sans-serif) for body; JetBrains Mono for AI responses/code.
* **Sizes:** * `xs`: 0.75rem | `base`: 1rem | `xl`: 1.25rem | `4xl`: 2.25rem
* **Weights:** Regular (400), Medium (500), Bold (700).

#### **Spacing & Borders**
* **Scale:** 0 to 16 (0px to 64px based on 4px increments).
* **Radius:** `rounded-lg` (8px) for buttons; `rounded-2xl` (16px) for the search bar.
* **Shadow:** `shadow-sm` (subtle elevation for cards).

---

### 📐 3. Layout System
* **Breakpoints:** `sm: 640px`, `md: 768px`, `lg: 1024px`.
* **Grid:** 12-column grid for dashboard analytics; single-column centered for the search experience.

```html
<div class="max-w-3xl mx-auto px-4 py-20 flex flex-col items-center">
  </div>
```

---

### 🧱 4. Component Library (Tailwind CSS)

#### **Buttons**
```html
<button class="px-6 py-2 bg-green-500 text-white font-medium rounded-lg hover:bg-green-600 transition-all">Route Prompt</button>

<button class="px-3 py-1 bg-red-50 text-red-600 border border-red-200 text-sm rounded hover:bg-red-100">Clear Key</button>
```

#### **The "Eco-Search" Bar (As per Sketch)**
```html
<div class="flex items-center w-full max-w-2xl border-2 border-slate-200 rounded-full px-4 py-2 focus-within:border-green-500 transition-colors bg-white">
  <select class="bg-transparent text-sm font-medium text-slate-600 border-none focus:ring-0 cursor-pointer">
    <option>Auto</option>
    <option>Local</option>
    <option>Cloud</option>
  </select>
  <div class="h-6 w-px bg-slate-200 mx-3"></div>
  <input type="text" placeholder="Ask EcoRouter..." class="flex-grow bg-transparent border-none focus:ring-0 text-slate-900">
  <button class="p-2 text-slate-400 hover:text-green-500">
    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
  </button>
</div>
```

#### **Impact Card**
```html
<div class="bg-white p-6 rounded-xl border border-slate-100 shadow-sm">
  <h3 class="text-slate-500 text-xs font-bold uppercase tracking-wider">ESIF Score</h3>
  <p class="text-3xl font-bold text-green-600">92/100</p>
  <p class="text-sm text-slate-500 mt-2">🌱 1.5g CO2 Saved via Local Routing</p>
</div>
```

---

### ♿ 5. Accessibility (WCAG AA)
* **Contrast:** Minimum 4.5:1 ratio for all text elements.
* **Focus States:** All interactive elements must have a visible `ring-2 ring-green-500` focus state.
* **Labels:** Every input must have an associated `aria-label`.

---

### ✨ 6. Animation Guidelines
* **Duration:** 200ms for hover states; 400ms for card expansion.
* **Easing:** `cubic-bezier(0.4, 0, 0.2, 1)` (Standard ease-in-out).
* **Reduced Motion:** Use `motion-safe:` prefix for non-essential animations.

---

### 📍 7. Icon System
* **Library:** Lucide React or Heroicons.
* **Sizes:** * Navigation: 20px (`w-5 h-5`)
    * Action Icons: 24px (`w-6 h-6`)

---

### 📱 8. Responsive Design Rules
* **Mobile-First:** Default classes for mobile, use `md:` for desktop expansion.
* **Touch Targets:** All buttons must have a minimum height/width of **44px** for mobile usability.
* **Sidebar:** Swaps to a bottom-sheet or full-screen overlay on mobile.

---

### 🌐 9. Browser Support
* Chrome (latest 3 versions)
* Firefox (latest 3 versions)
* Safari (latest 2 versions)
* Edge (latest 2 versions)
* *Note: Internet Explorer is not supported.*
document.addEventListener("DOMContentLoaded", () => {
    const textarea = document.querySelector("textarea[name='symptoms']");
    const chips = document.querySelectorAll(".chip");
    const samples = document.querySelectorAll(".sample-case");
    const toggles = document.querySelectorAll(".toggle-button");

    if (textarea) {
        textarea.addEventListener("focus", () => {
            document.body.classList.add("is-writing");
        });

        textarea.addEventListener("blur", () => {
            document.body.classList.remove("is-writing");
        });

        chips.forEach((chip) => {
            chip.addEventListener("click", () => {
                const value = chip.textContent.trim().toLowerCase();
                const current = textarea.value.trim();
                textarea.value = current ? `${current}, ${value}` : value;
                textarea.focus();
            });
        });

        samples.forEach((sample) => {
            sample.addEventListener("click", () => {
                textarea.value = sample.dataset.text || "";
                textarea.focus();
            });
        });
    }

    toggles.forEach((toggle) => {
        toggle.addEventListener("click", () => {
            const nextState = !toggle.classList.contains("is-on");
            toggle.classList.toggle("is-on", nextState);
            toggle.setAttribute("aria-checked", String(nextState));
        });
    });
});

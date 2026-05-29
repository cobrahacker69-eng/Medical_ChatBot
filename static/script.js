document.addEventListener("DOMContentLoaded", () => {
    const textarea = document.querySelector("textarea[name='symptoms']");

    if (!textarea) {
        return;
    }

    textarea.addEventListener("focus", () => {
        document.body.classList.add("is-writing");
    });

    textarea.addEventListener("blur", () => {
        document.body.classList.remove("is-writing");
    });
});

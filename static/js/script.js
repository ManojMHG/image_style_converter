document.addEventListener("DOMContentLoaded", function () {
    const imageInput = document.getElementById("image");
    const preview = document.getElementById("preview");
    const form = document.getElementById("uploadForm");
    const spinner = document.getElementById("spinner");

    imageInput.addEventListener("change", function () {
        const file = this.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function (e) {
                preview.src = e.target.result;
                preview.style.display = "block";
            };
            reader.readAsDataURL(file);
        }
    });

    form.addEventListener("submit", function () {
        spinner.style.display = "block";
    });
});
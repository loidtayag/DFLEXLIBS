let upload_file_label = document.getElementById("upload_file_label")
let upload_file = document.getElementById("upload_file")

upload_file.addEventListener("change", () => {
    upload_file_label.textContent = upload_file.files[0].name;
})

function cancelResults() {
    window.location = "upload"
}

function seeResults() {
    window.location = "results"
}

function seeOptions(index, length) {
    for (let i = 0; i < length; i++) {
        document.getElementById("r_options" + i).style.display = "none";
    }

    document.getElementById("r_options" + index).style.display = "flex";
}

function seeReport(index) {
    window.location = 'results/report?index=' + index
}

function seeAppInfo(index) {
    window.location = 'results/info?index=' + index
}

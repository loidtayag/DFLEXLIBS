document.addEventListener("DOMContentLoaded", () => {
    let upload_file_label = document.getElementById("upload_file_label")
    let upload_file = document.getElementById("upload_file")


    if (upload_file) {
        upload_file.addEventListener("change", () => {
            upload_file_label.textContent = upload_file.files[0].name;
        })
    }

    const param = new URLSearchParams(window.location.search).get('order')
    ascending = document.getElementById('ascending')
    descending = document.getElementById('descending')

    if (ascending && descending) {
        if (param == null) {
            descending.classList.remove('invisible')
            ascending.classList.add('invisible')
        }
        else if (param == 'ascending') {
            descending.classList.remove('invisible')
            ascending.classList.add('invisible')
        }
        else if (param == 'descending') {
            descending.classList.add('invisible')
            ascending.classList.remove('invisible')
        }
    }

    document.getElementById("uploadForm").addEventListener('submit', function (e) {
        e.preventDefault()
        document.getElementById('loading').classList.remove('invisible') 

        var formData = new FormData(this);
        console.log(formData)
        fetch(this.action, {
            method: this.method,
            body: formData,
        }).then(res => { 
            return res.json() 
        }).then(data => {
            document.getElementById('invisible_container').classList.remove('invisible')
        }).finally(() => {
            document.getElementById('loading').classList.add('invisible') 
        });
    })
})

function cancelResults() {
    document.getElementById('invisible_container').classList.add('invisible')
}

function seeResults() {
    window.location = "results"
}

function seeOptions(index, length) {
    for (let i = 0; i < length; i++) {
        if (i != index) {
                        document.getElementById("r_options" + i).style.display = "none";
        }
    }

    selected = document.getElementById("r_options" + index)

    if (selected.style.display == "flex") {
        selected.style.display = "none"
    }
    else {
        selected.style.display = "flex"
    }
}

function seeReport(index) {
    window.location = 'results/report?index=' + index
}

function seeAppInfo(index) {
    window.location = 'results/info?index=' + index
}

function demo() {
    const urlParams = new URLSearchParams(window.location.search);
    const index = urlParams.get('index')
    const name = urlParams.get('name')

    if (index) {
        window.location = '/results/info/description?index=' + index
    }
    else if (name) {
        window.location = '/results/info/description?name=' + name
    }
}

function why() {
    const urlParams = new URLSearchParams(window.location.search);
    const index = urlParams.get('index')
    const name = urlParams.get('name')

    if (index) {
        window.location = '/results/info/flow?index=' + index
    }
    else if (name) {
        window.location = '/results/info/flow?name=' + name
    }
}

function goToPerf() {
    const urlParams = new URLSearchParams(window.location.search);
    const index = urlParams.get('index')
    const name = urlParams.get('name')

    if (index) {
        window.location = '/results/info/performance?index=' + index
    }
    else if (name) {
        window.location = '/results/info/performance?name=' + name
    }
}

function goToReq() {
    const urlParams = new URLSearchParams(window.location.search);
    const index = urlParams.get('index')
    const name = urlParams.get('name')

    if (index) {
        window.location = '/results/info/requirements?index=' + index
    }
    else if (name) {
        window.location = '/results/info/requirements?name=' + name
    }
}

function goToCon() {
    const urlParams = new URLSearchParams(window.location.search);
    const index = urlParams.get('index')
    const name = urlParams.get('name')

    if (index) {
        window.location = '/results/info/configuration?index=' + index
    }
    else if (name) {
        window.location = '/results/info/configuration?name=' + name
    }
}

function downloadCon() {
    const urlParams = new URLSearchParams(window.location.search);
    const index = urlParams.get('index')
    const name = urlParams.get('name')

    // Add logic to get form values and pass to request
    configs = '[]'

    if (index) {
        fetch("/results/info/downloadCon?index=" + index + "&configs=" + configs).then(res => res.blob()).then(blob => {
            console.log(blob)
            const blobUrl = URL.createObjectURL(blob);
            const link = document.createElement('a');
            link.href = blobUrl;
            link.download = 'controls.zip'
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        })
    }
    else if (name) {
        fetch("/results/info/downloadCon?name=" + name + "&configs=" + configs).then(res => res.blob()).then(blob => {
            console.log(blob)
            const blobUrl = URL.createObjectURL(blob);
            const link = document.createElement('a');
            link.href = blobUrl;
            link.download = 'controls.zip'
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        })
    }
}

function downloadd() {
    const urlParams = new URLSearchParams(window.location.search);
    const index = urlParams.get('index')
    const name = urlParams.get('name')

    if (index) {
        fetch("/results/info/download?index=" + index).then(res => res.blob()).then(blob => {
            console.log(blob)
            const blobUrl = URL.createObjectURL(blob);
            const link = document.createElement('a');
            link.href = blobUrl;
            link.download = 'controls.zip'
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        })
    }
    else if (name) {
        fetch("/results/info/download?name=" + name).then(res => res.blob()).then(blob => {
            console.log(blob)
            const blobUrl = URL.createObjectURL(blob);
            const link = document.createElement('a');
            link.href = blobUrl;
            link.download = 'controls.zip'
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        })
    }
}

function download(index) {
    fetch("/results/info/download?index=" + index).then(res => res.blob()).then(blob => {
        console.log(blob)
        const blobUrl = URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.href = blobUrl;
        link.download = 'controls.zip'
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    })
}

function searchResults() {
    const value = document.querySelector('#results_search').value
    const els = document.querySelectorAll('[class^="results_name_"]');
    console.log(els)
    els.forEach(el => {
        const className = el.className;
        const suffix = className.slice("results_name_".length);
        if (!suffix.startsWith(value)) {
            el.style.display = 'none';
        } else {
            el.style.display = '';
        }
    });
}

function filters(selected) {
    params = new URLSearchParams(window.location.search)
    zone = params.get("zone")
    target = params.get("target")
    redirect = window.location.href

    if (!zone && !target) {
        redirect += "?zone=" + selected
    }
    else if (zone && !target) {
        redirect += "&target=" + selected
    }
    else if (zone && target) {
        console.log("results/info?name=" + selected)
        redirect = "results/info?name=" + selected
    }

    window.location.href = redirect
}

function goToArchetype() {
    window.location.href = 'filter'
}

function goToTarget() {
    params = new URLSearchParams(window.location.search)
    zone = params.get("zone")
    window.location.href = 'filter?zone=' + zone
}

function filterResults(order) {
    window.location.href = 'results?order=' + order
}

function filterResultsAll(order) {
    window.location.href = 'applications?order=' + order
}

document.addEventListener("DOMContentLoaded", () => {
    url = document.location.pathname
    params = new URLSearchParams(window.location.search)
    toHighlight = -1

    if (url == "/") {
        toHighlight = 0
        localStorage.setItem('header_on', toHighlight)
    }
    else if (url == "/search") {
        toHighlight = 1
        localStorage.setItem('header_on', toHighlight)

        localStorage.setItem('came_from', 'search')

        window.location.href = '/results'
    }
    else if (url == "/navigate") {
        toHighlight = 2
        localStorage.setItem('header_on', toHighlight)

        archetype = params.get("archetype")
        target = params.get("target")

        if (!archetype && !target) {
            document.getElementById('navigate_headers_0').classList.add('chosen');
            document.getElementById('navigate_headers_0_rule').style.display = "none";
            document.getElementById('navigate_headers_1_rule').style.display = "none";
            document.getElementById('navigate_headers_1').style.display = "none";
            document.getElementById('navigate_headers_2').style.display = "none";
        }
        else if (archetype && !target) {
            document.getElementById('navigate_headers_1').classList.add('chosen');
            document.getElementById('navigate_headers_1_rule').style.display = "none";
            document.getElementById('navigate_headers_2').style.display = "none";
        }
        else if (archetype && target) {
            document.getElementById('navigate_headers_2').classList.add('chosen');
        }
    }
    else if (url == "/validate") {
        toHighlight = 3
        localStorage.setItem('header_on', toHighlight)

        localStorage.setItem('came_from', 'validate')

        let upload_file_label = document.getElementById("upload_file_label")
        let upload_file = document.getElementById("upload_file")

        if (upload_file) {
            upload_file.addEventListener("change", () => {
                upload_file_label.textContent = upload_file.files[0].name;
            })
        }

        document.getElementById("upload_form").addEventListener('submit', function (e) {
            e.preventDefault()
            document.getElementById('upload_prequeue').classList.remove('invisible')
            document.getElementById('upload_error').classList.add('invisible')
            document.getElementById('upload_results').classList.add('invisible')
            var formData = new FormData(this);

            fetch(this.action, {
                method: this.method,
                body: formData,
            }).then(res => {
                return res.text()
            }).then(text => {
                document.getElementById('upload_prequeue').classList.add('invisible')
                document.getElementById('upload_results').classList.remove('invisible')

                // This is for celery but doesn't work on deployment
                // arr = text.split('&')

                // verify(arr[0], arr[1])
            });
        })
    }
    else if (url == "/results") {
        cookies = document.cookie.split(';')
        for (cookie of cookies) {
            cookie = cookie.split('=')
            if (cookie[0].replace(" ", "") == 'data') {
                data = cookie[1].substring(1, cookie[1].length - 1).replaceAll('\\054', ',').replaceAll('\\', '')
                localStorage.setItem('data', data)
            }
        }
        
        cameFrom = localStorage.getItem('came_from')
        
        if (cameFrom == 'search') {
            document.getElementById("base_headers_" + 1).classList.add('chosen')
            document.getElementById("came_from_filter").classList.add('invisible')
            document.getElementById("came_from_-1").classList.add('invisible')

            len = JSON.parse(localStorage.getItem('data'))['validation_table'].length
            
            for (let i = 0; i < len; i++) {
                document.getElementById("came_from_" + i).classList.add('invisible')
                document.getElementById("results_menu" + i).classList.add('results_child_come_from_search')
            }
        }

        if (cameFrom = 'validate') {
            document.getElementById('results_header_header').innerText = 'Model validation results'
        }

        let param = new URLSearchParams(window.location.search).get('order')
        ascending = document.getElementById('ascending')
        descending = document.getElementById('descending')

        if (param == null) {
            ascending.classList.remove('invisible')
            descending.classList.add('invisible')
        }
        else if (param == 'ascending') {
            ascending.classList.add('invisible')
            descending.classList.remove('invisible')
        }
        else if (param == 'descending') {
            ascending.classList.remove('invisible')
            descending.classList.add('invisible')
        }

        param = new URLSearchParams(window.location.search).get('valid')
        valid = document.getElementById('valid')
        invalid = document.getElementById('invalid')

        if (param == null) {
            valid.classList.remove('invisible')
            invalid.classList.add('invisible')
        }
        if (param == 'true') {
            valid.classList.add('invisible')
            invalid.classList.remove('invisible')
        }
        else if (param == 'false') {
            valid.classList.remove('invisible')
            invalid.classList.add('invisible')
        }

        els = document.querySelectorAll('[class^="results_option_"]');
        data = JSON.parse(localStorage.getItem("data"))["validation_table"]
        i = 0

        if (param == 'true') {
            els.forEach(function(el) {
                const className = el.className;
                const suffix = className.slice("results_option_".length);
                if (data[i][1] == false) {
                    el.style.display = 'none';
                } else {
                    el.style.display = '';
                }
                i += 1
            });
        }
        else if (param == 'false') {
            els.forEach(el => {
                const className = el.className;
                const suffix = className.slice("results_option_".length);
                if (data[i][1] == true) {
                    el.style.display = 'none';
                } else {
                    el.style.display = '';
                }
                i += 1
            });
        }

        let value = localStorage.getItem("hackSearch")
        if (value != null) {
            document.querySelector('#results_search').value = value
            searchResults()
        }
    }

    if (toHighlight == -1) {
        toHighlight = localStorage.getItem('header_on', toHighlight)
    }

    for (let i = 0; i < 4; i++) {
        el = document.getElementById("base_headers_" + i)

        if (toHighlight == i) {
            el.classList.add('chosen')
        }
        else {
            el.classList.remove('chosen')
        }
    }
})

function verify(id, token) {
    fetch('checkValidate?id=' + id + '&token=' + token).then(res => {
        return res.json()
    }).then(data => {
        if (data['validation_table'] == 'Error...') {
            document.getElementById('upload_error').classList.remove('invisible')
            document.getElementById('upload_prequeue').classList.add('invisible')
            document.getElementById('upload_queue').classList.add('invisible')
            document.getElementById('upload_loading').classList.add('invisible')
        }
        else if (data['validation_table'] == 'In queue...') {
            document.getElementById('upload_error').classList.add('invisible')
            document.getElementById('upload_prequeue').classList.add('invisible')
            document.getElementById('upload_queue').classList.remove('invisible')
            document.getElementById('upload_queue').innerText = 'In queue position ' + data['place'] + '...'
            
            lastTime = new Date()
            while (new Date() - lastTime < 2000) {}
            
            verify(id, token)
        }
        else if (data['validation_table'] == 'Task is still running...') {
            document.getElementById('upload_error').classList.add('invisible')
            document.getElementById('upload_prequeue').classList.add('invisible')
            document.getElementById('upload_queue').classList.add('invisible')
            document.getElementById('upload_loading').classList.remove('invisible')

            lastTime = new Date()
            while (new Date() - lastTime < 2000) {}

            verify(id, token)
        }
        else {
            document.getElementById('upload_error').classList.add('invisible')
            document.getElementById('upload_loading').classList.add('invisible')
            document.getElementById('upload_results').classList.remove('invisible')
        }
    })
}

/* navigate */
function goToArchetype() {
    window.location.href = 'navigate'
}

function goToTarget() {
    params = new URLSearchParams(window.location.search)
    archetype = params.get("archetype")
    window.location.href = 'navigate?archetype=' + archetype
}

function applyFilterOption(selected) {
    params = new URLSearchParams(window.location.search)
    archetype = params.get("archetype")
    target = params.get("target")
    redirect = window.location.href

    if (!archetype && !target) {
        redirect += "?archetype=" + selected
    }
    else if (archetype && !target) {
        redirect += "&target=" + selected
    }
    else if (archetype && target) {
        redirect = "results/info?name=" + selected
    }

    window.location.href = redirect
}

function hideFilterOptions() {
    el = document.getElementById('navigate_options_icon')
    options = document.getElementById('navigate_options_options')
    promptt = document.getElementById('navigate_options_prompt')
    text = el.innerText

    if (text == 'unfold_less') {
        el.textContent = 'unfold_more'
        options.style.display = "none"
        promptt.style.borderRadius = '2rem'
    }
    else if (text == 'unfold_more') {
        el.textContent = 'unfold_less'
        options.style.display = "block"
        promptt.style.borderRadius = '0'
    }
}

/* validate  */
function cancelResults() {
    document.getElementById('upload_results').classList.add('invisible')
}

function goToResults() {
    window.location = "results"
}

/* results */
function searchResults() {
    const value = document.querySelector('#results_search').value
    const els = document.querySelectorAll('[class^="results_option_"]');

    els.forEach(el => {
        const className = el.className;
        const suffix = className.slice("results_option_".length);
        if (!suffix.startsWith(value)) {
            el.style.display = 'none';
        } else {
            el.style.display = '';
        }
    });

    localStorage.setItem("hackSearch", value);
}

function filterResults(valid) {
    validP = params.get('valid')
    order = params.get('order')

    if (order == null && validP == null) {
        window.location.href = 'results?valid=' + valid;
    }
    else if (order != null && validP == null) {
        window.location.href = 'results?order=' + order + '&valid=' + valid;
    }
    else if (order == null && validP != null) {
        window.location.href = 'results?valid=' + valid;
    }
    else if (order != null && validP != null) {
        window.location.href = 'results?order=' + order + '&valid=' + valid;
    }
}

function orderResults(order) {
    params = new URLSearchParams(window.location.search)
    valid = params.get('valid')
    orderP = params.get('order')

    if (valid == null && orderP == null) {
        window.location.href = 'results?order=' + order;
    }
    else if (valid != null && orderP == null) {
        window.location.href = 'results?valid=' + valid + '&order=' + order;
    }
    else if (valid == null && orderP != null) {
        window.location.href = 'results?order=' + order;
    }
    else if (valid != null && orderP != null) {
        window.location.href = 'results?valid=' + valid + '&order=' + order;
    }
}

function menuAResult(index, length) {
    selected = document.getElementById("results_menu" + index)

    if (selected.classList.contains('invisible')) {
        for (let i = 0; i < length; i++) {
            if (i != index) {
                document.getElementById("results_menu" + i).classList.add('invisible');
            }
        }

        selected.classList.remove('invisible');
        localStorage.setItem("menu", index);
    }
    else {
        selected.classList.add('invisible');
    }
}

function restartResults() {
    localStorage.removeItem('hackSearch')
    window.location.href = 'results'
}

function seeAppInfo(index) {
    window.location = 'results/info?index=' + index
}

function goToReport(index) {
    window.location = 'results/report?index=' + index
}

/* even more for results */
function goToDesc() {
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

function goToFlow() {
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

function goToConn(index) {
    window.location = '/results/info/configuration?index=' + index
}

function showSliderValue(id) {
    input = document.getElementById(id + '_input')
    text = document.getElementById(id)
    text.textContent = input.value
}

function showCheckboxValue(id) {
    input = document.getElementById(id + '_input')
    text = document.getElementById(id)
    console.log(input.checked);

    if (input.checked) {
        text.textContent = 'Yes'
    }
    else {
        text.textContent = 'No'
    }
}

function download(indexOrName) {
    if (!isNaN(parseInt(indexOrName))) {
        fetch("/results/info/download?index=" + indexOrName).then(res => res.blob()).then(blob => {
            const blobUrl = URL.createObjectURL(blob);
            const link = document.createElement('a');
            link.href = blobUrl;
            link.download = 'controls.zip'
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        })
    }
    else {
        fetch("/results/info/download?name=" + indexOrName).then(res => res.blob()).then(blob => {
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

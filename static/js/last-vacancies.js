updateVacancies(new Date())

function updateVacancies(date) {
    date = date.toISOString().split("T")[0]
    let vacanciesQuery = 'https://api.hh.ru/vacancies?per_page=10&' +
        'page=0&order_by=publication_time&date_from='+ date +'&date_to=' + date + '&text=';
    let names = ['engineer', 'инженер+программист', 'інженер', 'it+инженер', 'инженер+разработчик']
    let promises = []
    for (name of names){
        let query = vacanciesQuery + name
        promises.push(fetch(query)
            .then(r => r.json())
            .then(x => x.items))
    }
    let tbody = document.getElementsByTagName('tbody')
    while (tbody[0].rows[0]){
        tbody[0].deleteRow(0)
    }
    Promise.all(promises).then(vacancies =>{
        let listVacancies = []
        for (let vacancy of vacancies){
            listVacancies = listVacancies.concat(vacancy)
        }
        let promises = []
        listVacancies.sort((a, b) => new Date(a).getMilliseconds() - new Date(b).getMilliseconds())
        for (let i = 0; i < 10; i++){
            promises.push(fetch('https://api.hh.ru/vacancies' + '/' + listVacancies[i]['id']).then(r => r.json()))
        }
        Promise.all(promises).then(updateTable)
    })
}

function extractDescription(s) {
    function removeTags(s) {
        return (s.split(new RegExp('<[^>]*>'))).join(' ')
    }
    let description = removeTags(s)
    if (description.length <= 100){
        return description
    }
    return description.slice(0, 100) + '...'
}


function extractKeySkills(keySkillsJSON){
    let keySkills = keySkillsJSON.map(skill => skill['name'])
    return keySkills.join('; ')
}

function extractSalary(salaryJSON){
    if (salaryJSON == null){
        return 'не указано'
    }
    let gross = salaryJSON['gross'] === ' (gross)' ? 'gross' : ''
    let salary = salaryJSON['from'] + ' - ' + salaryJSON['to'] + '\n' + salaryJSON['currency'] + gross
    return salary
}

function updateTable(vacancies){
    let vacancyTable = document.getElementById("vacancyTable")
    let tbody = vacancyTable.getElementsByTagName("tbody")[0]
    for (let i = 0; i < 10; i++){
        let newRow = tbody.insertRow()
        newRow.insertCell().appendChild(document.createTextNode(vacancies[i]['name']))
        newRow.insertCell().appendChild(document.createTextNode(extractDescription(vacancies[i]['description'])))
        newRow.insertCell().appendChild(document.createTextNode(extractKeySkills(vacancies[i]['key_skills'])))
        newRow.insertCell().appendChild(document.createTextNode(vacancies[i]['employer']['name']))
        newRow.insertCell().appendChild(document.createTextNode(extractSalary(vacancies[i]['salary'])))
        newRow.insertCell().appendChild(document.createTextNode(vacancies[i]['area']['name']))
        newRow.insertCell().appendChild(document.createTextNode(vacancies[i]['published_at']))
    }
}

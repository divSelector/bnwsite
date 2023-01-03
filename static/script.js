// Show/Hide Table -- final call inside of EventListener callbacks
const toggleTable = (table, isToggled) => {
    const input = document.querySelector(`#toggle-${table.id}`)
    input.checked = isToggled
    if (!isToggled) table.classList.add('hide')
    else table.classList.remove('hide')
}

// Search Input Handler
document.querySelector('#mainInput').addEventListener('keyup', () => {
    const rows = document.querySelectorAll('#mainTable table tbody tr')
    const filter = document.querySelector('#mainInput').value
    const re = new RegExp(filter, 'i')
    const isFoundInCells = cell => re.test(cell.innerHTML)
    const isFound = childrenArr => childrenArr.some(isFoundInCells)
    const setRowStyleDisplay = ({ style, children }) => {
        style.display = isFound([
            ...children
        ]) ? '' : 'none'
    }

    // Display Row Based Search Query
    rows.forEach(setRowStyleDisplay)

    // Display Table Based on Visible Rows
    const tables = document.querySelectorAll(
        '#mainTable table.outer-table'
    )
    const allAreTrue = arr => arr.every(el => el === true)
    let hide_rows, idx
    for (let t of tables) {
        hide_rows = []
        idx = 0
        for (let r of t.rows) {
            if (r.style.display === 'none') {
                hide_rows.push(true)
            } else {
                if (r.outerHTML.includes('<td>')) {
                    hide_rows.push(false)
                    break
                }
            }
            idx++
        }
        if (allAreTrue(hide_rows)) toggleTable(t, false)
        else toggleTable(t, true)
    }
})

// Make an array of all ID selectors for all display checkboxes
const toggleIds = Array.from(
    document.querySelectorAll(
        'ul.single-table-checkboxes li input'
    )
).map(elem => "#" + elem.id)

// Add event listener to checkbox Paired with table
for (let toggleId of toggleIds) {
    document.querySelector(toggleId).addEventListener('change', () => {
        let tElem = document.querySelector(
            `#${toggleId.split("toggle-")[1]}`
        )
        if (!tElem.classList.contains('hide')) toggleTable(tElem, false)
        else toggleTable(tElem, true)
    })
}

function uncheckAll() {
    for (let toggleId of toggleIds) {
        if (document.querySelector(toggleId).checked == true) {
            toggleTable(document.querySelector(toggleId.replace('toggle-', '')), false)
        }
    }
}

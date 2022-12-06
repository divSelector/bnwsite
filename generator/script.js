function isArray(object) {
    return Object.prototype.toString.call(object) === '[object Array]'
}

const createCellForRow = (r, arr, i, col, j) => {
    let tableCell = r.insertCell(-1)
    // Logic to Determine if Cell is Heading
    if (i === 0) {
        tableCell.outerHTML = `<th scope="col">${arr[i][col[j]]}</th>`

    } else if (j === 0) {
        tableCell.outerHTML = `<th scope="row">${arr[i][col[j]]}</th>`

    } else {
        tableCell.innerHTML = arr[i][col[j]]
    }
    // Logic to Determine if Cell Contains Table
    if (isArray(arr[i][col[j]])) {
        const innerTable = createTableFromData(arr[i][col[j]])
        insertTableToContainer(innerTable, tableCell)
    } else {
        tableCell.innerHTML = arr[i][col[j]]
    }
}

const createRowForTable = (t, arr, i, col, thead) => {
    let row
    if (i === 0) {
        row = thead.insertRow(-1)
    } else {
        row = t.insertRow(-1)
    }
    for (let j = 0; j < col.length; j++) {
        createCellForRow(row, arr, i, col, j)
    }
    return row
}

const createTableFromData = (arr, id) => {
    let table = document.createElement('table')
    if(typeof id !== "undefined") {
        table.id = id.replace(/json\//gi, '')
        table.classList.add("outer-table")
    } else {
        table.classList.add("inner-table")
    }
    let tHead = table.createTHead()
    let tBody = table.createTBody()
    let col = []
    for (let i = 0; i < arr.length; i++) {
        for (let key in arr[i]) {
            if (col.indexOf(key) === -1) {
                col.push(key)
            }
        }
        createRowForTable(tBody, arr, i, col, tHead)
    }
    return table
}

const insertTableToContainer = (tab, con) => {
//     con.innerHTML = ""
    con.appendChild(tab)
}

const getData = (url, sel) => {
  const tableId = url.split('.')[0]
  axios.get(url).then(response => {
      const tab = createTableFromData(response.data, tableId)
      insertTableToContainer(
          tab, document.querySelector(sel)
      )
  })
}

// Tables To Build
const jsonFiles = [
    'json/magic-black.json',
    'json/magic-white.json',
    'json/magic-gray.json',
    'json/esper-summons.json',
    'json/esper-boons.json',
    'json/blitz.json',
    'json/bushido.json',
    'json/dance-actions.json',
    'json/dance-modes.json',
    'json/lore.json',
    'json/rage-actions.json',
    'json/rage-modes.json',
    'json/slots.json',
    'json/thrown.json',
    'json/tools.json',
    'json/characters.json',
    'json/experience-growth.json',
    'json/enemy.json',
    'json/weapons.json',
    'json/legend.json',
    'json/items.json',
    'json/shields.json',
    'json/armor.json',
    'json/helmets.json',
    'json/relics.json',
    'json/towns.json'
] // Insert your json data above


// Wait a full three seconds with each call of getData.
// This ensures that tables generate in the order they are listed in the array above.
const build = endpoint =>
  new Promise(resolve =>
    setTimeout(() => getData(endpoint, '#mainTable'), 3000)
  )

const buildAllTables = async (tables) => {
  for (table of tables) {
    build(table)
  }
}

buildAllTables(jsonFiles)


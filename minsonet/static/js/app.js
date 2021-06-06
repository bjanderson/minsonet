console.log('hello flask')

const userUri = '/user'
fetch(userUri).then(r => r.json()).then(users => {
  console.log('users :>> ', users);
  if (users.length > 0) {
    const columns = Object.keys(users[0])
    buildTable(columns, users)
  }
})

function buildTable(columns, users) {
  const table = createTable()
  const thead = createHeaderRow(columns)
  const tbody = createTableRows(users)
  table.appendChild(thead)
  table.appendChild(tbody)
  document.body.appendChild(table)
}

function createTable() {
  const table = document.createElement('table')
  return table
}

function createHeaderRow(columns) {
  const head = document.createElement('thead')
  const row = document.createElement('tr')
  head.appendChild(row)
  columns.forEach(col => {
    const th = document.createElement('th')
    th.innerText = col
    row.appendChild(th)
  })
  // the buttons column
  const th = document.createElement('th')
  th.className = 'buttons';
  row.appendChild(th)
  return head
}

function createTableRows(users) {
  const body = document.createElement('tbody')
  users.forEach(d => {
    const row = createTableRow(d)
    body.appendChild(row)
  })
  return body
}

function createTableRow(user) {
  const row = document.createElement('tr')
  const values = Object.values(user)
  values.forEach(d => {
    const th = document.createElement('td')
    th.innerText = d
    row.appendChild(th)
  })
  const editButton = createEditButton(user)
  row.appendChild(editButton)
  return row
}

function createEditButton(user) {
  const button = document.createElement('button')
  button.innerText = 'Edit'
  button.addEventListener('click', () => {editUser(user)})
  return button;
}

function editUser(user) {
  console.log('\neditUser');
  console.log('user :>> ', user);
  showEditTemplate(user)
}

function showEditTemplate(user) {
  removeEditUserForm()
  const form = document.querySelector('#editusertemplate').content.firstElementChild.cloneNode(true)
  console.log(form);
  const nameInput = form.querySelector('#name')
  nameInput.value = user.name
  const emailInput = form.querySelector('#email')
  emailInput.value = user.email

  const editButton = form.querySelector('#editbutton')
  editButton.addEventListener('click', () => {save(user)})
  document.body.appendChild(form)
}

function save(user) {
  removeEditUserForm()
}

function removeEditUserForm() {
  const form = document.querySelector('#edituserform')
  if (form != null) {
    document.body.removeChild(form)
  }
}

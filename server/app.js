// load our app server
const express = require('express')
const app = express()
const morgan = require('morgan')
const mysql = require('mysql')

app.use(morgan('combined'))

app.get("/", (req, res) => {
  console.log("Responding to root route.")
  res.send("Hello from root.")
})

app.get("/users", (req, res) => {
  const user1 = {
    firstName: "Huy",
    lastName: "Pham",
    nickname: "front end god"
  }
  const user2 = {
    firstName: "Duy",
    lastName: "Pham",
    what: "the fuck"
  }
  res.json([user1, user2])
})

const pool = mysql.createPool({
  connectionLimit: 10,
  host: '<HOST>',
  user: '<USERNAME>',
  password: '<PASSWORD>',
  database: '<DATABASE>'
})

function getConnection() {
  return pool
}

app.get("/api", (req, res) => {

  const connection = getConnection()

  const queryString = "SELECT * FROM data"

  connection.query(queryString, (err, rows, fields) => {
    if (err) {
      console.log("Failed to query: " + err)
      res.sendStatus(500)
      return
    }
    console.log("Fetched successfully.")
    res.json(rows)
  })

  //res.end()
})

const PORT = process.env.PORT || 35003

// localhost:3003
app.listen(PORT, () => {
  console.log("Server is up and listening on " + PORT)
})

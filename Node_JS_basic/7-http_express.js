const express = require('express');
const fs = require('node:fs/promises');

const app = express();
const port = 1245;
const database = process.argv[2];

async function countStudents(path) {
  let data;

  try {
    data = await fs.readFile(path, 'utf8');
  } catch (err) {
    throw new Error('Cannot load the database');
  }

  const lines = data
    .split('\n')
    .filter((line) => line.trim() !== '');

  const students = lines.slice(1);

  const fields = {};

  students.forEach((line) => {
    const [firstname, , , field] = line.split(',');

    if (!fields[field]) {
      fields[field] = [];
    }

    fields[field].push(firstname);
  });

  let result = `Number of students: ${students.length}`;

  Object.entries(fields).forEach(([field, list]) => {
    result += `\nNumber of students in ${field}: ${list.length}. List: ${list.join(', ')}`;
  });

  return result;
}

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  try {
    const studentsInfo = await countStudents(database);

    res.send(
      `This is the list of our students\n${studentsInfo}`,
    );
  } catch (err) {
    res.send(
      'This is the list of our students\nCannot load the database',
    );
  }
});

app.listen(port);

module.exports = app;

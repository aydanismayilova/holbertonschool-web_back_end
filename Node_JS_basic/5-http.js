const http = require('http');
const fs = require('fs').promises;

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

const app = http.createServer(async (req, res) => {
  res.writeHead(200, {
    'Content-Type': 'text/plain',
  });

  if (req.url === '/') {
    res.end('Hello Holberton School!');
    return;
  }

  if (req.url === '/students') {
    try {
      const studentsInfo = await countStudents(database);

      res.end(
        `This is the list of our students\n${studentsInfo}`,
      );
    } catch (err) {
      res.end(
        'This is the list of our students\nCannot load the database',
      );
    }
    return;
  }

  res.end();
});

app.listen(1245);

module.exports = app;

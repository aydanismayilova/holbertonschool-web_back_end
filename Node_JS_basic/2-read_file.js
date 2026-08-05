const fs = require('node:fs');

function countStudents(path) {
  let data;

  try {
    data = fs.readFileSync(path, 'utf8');
  } catch (err) {
    throw new Error('Cannot load the database');
  }

  const lines = data
    .split('\n')
    .filter((line) => line.trim() !== '');

  const students = lines.slice(1);

  const fields = {};

  for (const line of students) {
    const [firstname, , , field] = line.split(',');

    if (!fields[field]) {
      fields[field] = [];
    }

    fields[field].push(firstname);
  }

  console.log(`Number of students: ${students.length}`);

  for (const [field, list] of Object.entries(fields)) {
    console.log(
      `Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`,
    );
  }
}

module.exports = countStudents;

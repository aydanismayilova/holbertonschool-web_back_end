const fs = require('node:fs/promises');

function readDatabase(path) {
  return fs.readFile(path, 'utf-8')
    .then((data) => {
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

      return fields;
    })
    .catch(() => {
      throw new Error('Cannot load the database');
    });
}

module.exports = readDatabase;

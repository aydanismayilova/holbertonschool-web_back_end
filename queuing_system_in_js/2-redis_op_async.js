import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error.message || error}`);
});
const getAsync = promisify(client.get).bind(client);
function setNewschool(schoolname, value) {
    client.set(schoolname, value, redis.print);
}
function displaySchoolValue(schoolname){
    client.get(schoolname, (err, reply) => {
        console.log(reply);
    });
}
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
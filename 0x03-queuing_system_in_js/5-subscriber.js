import redis from 'redis';
import { createClient } from 'redis';
import util from 'util';

const client = createClient();

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('message', (channel, message) => {
    if (message === 'KILL_SERVER') {
        client.unsubscribe('holberton school channel', () => {
            process.exit(0)
        })
    }
    console.log(message)
})
client.subscribe('holberton school channel')
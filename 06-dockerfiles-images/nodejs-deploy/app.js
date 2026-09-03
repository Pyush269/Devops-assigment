const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Hello World from Node.js Deployment!');
});

app.listen(3000, () => console.log('Node.js deploy running on port 3000'));

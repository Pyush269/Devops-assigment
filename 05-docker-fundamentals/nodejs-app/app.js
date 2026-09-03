const express = require('express');
const app = express();
const PORT = 3000;

app.get('/', (req, res) => {
  res.send('<h1>Hello World from Node.js!</h1><p>Student: PIYUSH PAWAN KUMAR | Enrollment: 2024eb02275</p>');
});

app.listen(PORT, () => {
  console.log(`Node.js app running on port ${PORT}`);
});

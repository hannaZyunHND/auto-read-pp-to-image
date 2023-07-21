const express = require('express');
const { processInput } = require('./mid_journey');
const app = express();
// Middleware để đọc dữ liệu từ body của request dưới dạng JSON
app.use(express.json());
const port = 3000;

app.get('/', async (req, res) => {
    const inputString = "Christmas dinner with spaghetti with family in a cozy house, we see interior details, simple blue&white illustration";
  
    // Gọi hàm processInput với đối số inputString
    let result = await processInput(inputString);
    res.send(result);
});
// API POST nhận tham số imagine dạng chuỗi
app.post('/imagine', async (req, res) => {
  const imagineString = req.body.imagine;

  // Gọi hàm processInput với đối số imagineString
  try {
      let result = await processInput(imagineString);
      res.send(result);
  } catch (error) {
      res.status(500).send("Đã xảy ra lỗi khi xử lý dữ liệu");
  }
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
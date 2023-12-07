const { Midjourney } = require("midjourney");
require('dotenv').config();

async function processInput(inputString) {
  const client = new Midjourney({
    ServerId: process.env.SERVER_ID,
    ChannelId: process.env.CHANNEL_ID,
    SalaiToken: process.env.SALAI_TOKEN,
    Debug: true,
    Ws: true,
  });
  await client.init();
  await client.Connect(); // required
  console.log(client);
  const Imagine = await client.Imagine(inputString, (uri, progress) => {
    console.log("loading", uri, "progress", progress);
  });
  
  console.log(Imagine);
  client.Close();
  return Imagine;
}

module.exports = {
  processInput
};

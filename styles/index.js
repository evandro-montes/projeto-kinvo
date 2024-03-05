const express = require("express");
const cors = require("cors");
const fs = require("fs");
const path = require("path");
const app = express();
const port = 3000;

// Middleware to enable CORS
app.use(cors());

// Welcome route
app.get("/", (req, res) => {
  res.send("Welcome to the Financial Quotes Server!");
});

// Route to serve stock information
app.get("/stockinfo", async (req, res) => {
  try {
    const data = fs.readFileSync(
      path.join(__dirname, "stockinfo.json"),
      "utf8"
    );
    const stocks = JSON.parse(data);
    res.json(stocks);
  } catch (error) {
    console.error("Error reading stockinfo.json:", error);
    res.status(500).send("Error retrieving stock information");
  }
});

// Route for fetching live quote and stock information
app.get("/quote/:symbol", async (req, res) => {
  const symbol = req.params.symbol.toUpperCase();
  try {
    const fetch = (await import("node-fetch")).default;
    const quoteUrl = `https://query1.finance.yahoo.com/v8/finance/chart/${symbol}`;
    const quoteResponse = await fetch(quoteUrl);
    const quoteData = await quoteResponse.json();

    const stockInfoData = fs.readFileSync(
      path.join(__dirname, "stockinfo.json"),
      "utf8"
    );
    const stocks = JSON.parse(stockInfoData);
    const stockInfo = stocks.find((stock) => stock.Ticker === symbol);

    const result = {
      quote: quoteData,
      info: stockInfo || { Name: "Unknown", Exchange: "Unknown" },
    };

    res.json(result);
  } catch (error) {
    console.error("Error fetching quote or stock information:", error);
    res.status(500).send("Error fetching data");
  }
});

// Start server
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
